from .pairs import BTC_USD
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Coinbase"
    _uri = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    _coinpair = BTC_USD

    def _map(self, data):
        return {
            'price':  data['data']['amount']
            }
