from .pairs import ETH_BTC
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Bitstamp"
    _uri = "https://www.bitstamp.net/api/v2/ticker/ethbtc/"
    _coinpair = ETH_BTC

    def _map(self, data):
        return {
            'price':  data['last'],
            'volume': data['volume']}
