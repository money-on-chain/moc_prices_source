from .pairs import ETH_USD
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Kraken"
    _uri = "https://api.kraken.com/0/public/Ticker?pair=XETHZUSD"
    _coinpair = ETH_USD

    def _map(self, data):
        return {
            'price': data['result']['XETHZUSD']['c'][0],
            'volume': data['result']['XETHZUSD']['v'][1] }
