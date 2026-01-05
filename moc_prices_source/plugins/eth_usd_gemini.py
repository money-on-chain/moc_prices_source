from .pairs import ETH_USD
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "Gemini"
    _uri         = "https://api.gemini.com/v1/pubticker/ETHUSD"
    _coinpair    = ETH_USD

    def _map(self, data):
        return {
            'price':  data['last'],
            }
