from .pairs import ETH_BTC
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Gemini"
    _uri = "https://api.gemini.com/v1/pubticker/ETHBTC"
    _coinpair = ETH_BTC

    def _map(self, data):
        return {
            'price': data['last'],
            }
