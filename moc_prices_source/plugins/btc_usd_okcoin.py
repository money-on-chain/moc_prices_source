from .pairs import BTC_USD
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "OkCoin"
    _uri = "https://www.okcoin.com/api/spot/v3/instruments/BTC-USD/ticker"
    _coinpair = BTC_USD

    def _map(self, data):
        return {
            'price':  data['last'],
            }
