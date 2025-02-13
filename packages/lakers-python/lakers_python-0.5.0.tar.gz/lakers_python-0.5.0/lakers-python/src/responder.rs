use lakers::*;
use lakers_crypto::{default_crypto, CryptoTrait};
use log::trace;
use pyo3::{prelude::*, types::PyBytes};

use super::StateMismatch;

#[pyclass(name = "EdhocResponder")]
pub struct PyEdhocResponder {
    r: Vec<u8>,
    cred_r: Credential,
    start: Option<ResponderStart>,
    processing_m1: Option<ProcessingM1>,
    wait_m3: Option<WaitM3>,
    processing_m3: Option<ProcessingM3>,
    processed_m3: Option<ProcessedM3>,
    completed: Option<Completed>,
}

#[pymethods]
impl PyEdhocResponder {
    #[new]
    fn new(r: Vec<u8>, cred_r: super::AutoCredential) -> PyResult<Self> {
        trace!("Initializing EdhocResponder");
        let (y, g_y) = default_crypto().p256_generate_key_pair();

        let cred_r = cred_r.to_credential()?;

        Ok(Self {
            r,
            cred_r,
            start: Some(ResponderStart {
                method: EDHOCMethod::StatStat.into(),
                y,
                g_y,
            }),
            processing_m1: None,
            wait_m3: None,
            processing_m3: None,
            processed_m3: None,
            completed: None,
        })
    }

    fn process_message_1<'a>(
        &mut self,
        py: Python<'a>,
        message_1: Vec<u8>,
    ) -> PyResult<(Bound<'a, PyBytes>, Option<EADItem>)> {
        let message_1 = EdhocMessageBuffer::new_from_slice(message_1.as_slice())?;
        let (state, c_i, ead_1) = r_process_message_1(
            &self.start.take().ok_or(StateMismatch)?,
            &mut default_crypto(),
            &message_1,
        )?;
        self.processing_m1 = Some(state);
        let c_i = PyBytes::new_bound(py, c_i.as_slice());

        Ok((c_i, ead_1))
    }

    #[pyo3(signature = (cred_transfer, c_r=None, ead_2=None))]
    fn prepare_message_2<'a>(
        &mut self,
        py: Python<'a>,
        cred_transfer: CredentialTransfer,
        c_r: Option<Vec<u8>>,
        ead_2: Option<EADItem>,
    ) -> PyResult<Bound<'a, PyBytes>> {
        let c_r = match c_r {
            Some(c_r) => ConnId::from_slice(c_r.as_slice()).ok_or(
                pyo3::exceptions::PyValueError::new_err(format!(
                    "Connection identifier out of range: {:?}",
                    c_r
                )),
            )?,
            None => generate_connection_identifier_cbor(&mut default_crypto()),
        };
        let mut r = BytesP256ElemLen::default();
        r.copy_from_slice(self.r.as_slice());

        match r_prepare_message_2(
            self.processing_m1.as_ref().ok_or(StateMismatch)?,
            &mut default_crypto(),
            self.cred_r,
            &r,
            c_r,
            cred_transfer,
            &ead_2,
        ) {
            Ok((state, message_2)) => {
                self.wait_m3 = Some(state);
                Ok(PyBytes::new_bound(py, message_2.as_slice()))
            }
            Err(error) => Err(error.into()),
        }
    }

    pub fn parse_message_3<'a>(
        &mut self,
        py: Python<'a>,
        message_3: Vec<u8>,
    ) -> PyResult<(Bound<'a, PyBytes>, Option<EADItem>)> {
        let message_3 = EdhocMessageBuffer::new_from_slice(message_3.as_slice())?;
        match r_parse_message_3(
            &mut self.wait_m3.take().ok_or(StateMismatch)?,
            &mut default_crypto(),
            &message_3,
        ) {
            Ok((state, id_cred_i, ead_3)) => {
                self.processing_m3 = Some(state);
                Ok((PyBytes::new_bound(py, id_cred_i.bytes.as_slice()), ead_3))
            }
            Err(error) => Err(error.into()),
        }
    }

    pub fn verify_message_3<'a>(
        &mut self,
        py: Python<'a>,
        valid_cred_i: super::AutoCredential,
    ) -> PyResult<Bound<'a, PyBytes>> {
        let valid_cred_i = valid_cred_i.to_credential()?;
        match r_verify_message_3(
            &mut self.processing_m3.take().ok_or(StateMismatch)?,
            &mut default_crypto(),
            valid_cred_i,
        ) {
            Ok((state, prk_out)) => {
                self.processed_m3 = Some(state);
                Ok(PyBytes::new_bound(py, prk_out.as_slice()))
            }
            Err(error) => Err(error.into()),
        }
    }

    #[pyo3(signature = (ead_4=None))]
    fn prepare_message_4<'a>(
        &mut self,
        py: Python<'a>,
        ead_4: Option<EADItem>,
    ) -> PyResult<Bound<'a, PyBytes>> {
        match r_prepare_message_4(
            &self.processed_m3.take().ok_or(StateMismatch)?,
            &mut default_crypto(),
            &ead_4,
        ) {
            Ok((state, message_4)) => {
                self.completed = Some(state);
                Ok(PyBytes::new_bound(py, message_4.as_slice()))
            }
            Err(error) => Err(error.into()),
        }
    }

    pub fn completed_without_message_4<'a>(&mut self, py: Python<'a>) -> PyResult<()> {
        match r_complete_without_message_4(&self.processed_m3.take().ok_or(StateMismatch)?) {
            Ok(state) => {
                self.completed = Some(state);
                Ok(())
            }
            Err(error) => Err(error.into()),
        }
    }

    pub fn edhoc_exporter<'a>(
        &mut self,
        py: Python<'a>,
        label: u8,
        context: Vec<u8>,
        length: usize,
    ) -> PyResult<Bound<'a, PyBytes>> {
        let mut context_buf: BytesMaxContextBuffer = [0x00u8; MAX_KDF_CONTEXT_LEN];
        context_buf[..context.len()].copy_from_slice(context.as_slice());

        let res = edhoc_exporter(
            self.completed.as_ref().ok_or(StateMismatch)?,
            &mut default_crypto(),
            label,
            &context_buf,
            context.len(),
            length,
        );
        Ok(PyBytes::new_bound(py, &res[..length]))
    }

    pub fn edhoc_key_update<'a>(
        &mut self,
        py: Python<'a>,
        context: Vec<u8>,
    ) -> PyResult<Bound<'a, PyBytes>> {
        let mut context_buf = [0x00u8; MAX_KDF_CONTEXT_LEN];
        context_buf[..context.len()].copy_from_slice(context.as_slice());

        let res = edhoc_key_update(
            self.completed.as_mut().ok_or(StateMismatch)?,
            &mut default_crypto(),
            &context_buf,
            context.len(),
        );
        Ok(PyBytes::new_bound(py, &res[..SHA256_DIGEST_LEN]))
    }
}
