from .pairs import USD_COP
from .base import Base, engine_register 



@engine_register()
class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "BanRep"
    _uri         = "https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario"
    _coinpair    = USD_COP

    def _map(self, data):
        return {'price': data[-1][1]}
