from .db import db


class CuentaMedica(db.Document):
    doc_id = db.StringField(required=True, unique=True)
    producto = db.StringField(required=True)
    nombreProducto = db.StringField(required=True)
    codigoPlan = db.StringField(required=True)
	nombrePlan = db.StringField(required=True)
	numContrato = db.StringField(required=True)
	tipoIdentificacionTitularContrato = db.StringField(required=True)
	numIdentificacionTitularContrato = db.StringField(required=True)
	nombreTitularContrato =  db.StringField(required=True)
	fechaProceso = db.StringField(required=True)
	fechaCorteDatos = db.StringField(required=True)
	estadoContrato = db.StringField(required=True)
	fechaCorteRecaudos = db.StringField(required=True)
	fechaCorteNovedades = db.StringField(required=True)
	fechaCorteCartera = db.StringField(required=True)
	vigencias = db.StringField(required=True)
	inIcioVigencia = db.StringField(required=True)
	modalidadPagoActual = db.StringField(required=True)
	descuentoActual = db.StringField(required=True)
	saldoAnterior = db.StringField(required=True)
	saldoVigente = db.StringField(required=True)
	totalConsolidado = db.StringField(required=True)
	recaudosPorAplicar = db.StringField(required=True)
	saldoAlaFecha = db.StringField(required=True)
