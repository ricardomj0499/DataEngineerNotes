use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct Transferencia {
    #[serde(rename = "Estado")]
    estado: String,
    #[serde(rename = "Fecha")]
    fecha: String,
    #[serde(rename = "Referencia")]
    referencia: String,
    #[serde(rename = "Cuenta Origen")]
    cuenta_origen: String,
    #[serde(rename = "Cuenta Destino")]
    cuenta_destino: String,
    #[serde(rename = "Monto")]
    monto: String,
    #[serde(rename = "Moneda")]
    moneda: String,
}
