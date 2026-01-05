from .pairs import BTC_USD
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Bittrex"
    _uri = "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC"
    _coinpair = BTC_USD

    def _map(self, data):
        return {
            'price':  data['result']['Last'],
            }
