from .client import CuentaMedicaApi


def initialize_routes(api):
    api.add_resource(CuentaMedicaApi, '/api/consultarestadocuenta')
    
