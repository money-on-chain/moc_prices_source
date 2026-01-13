from .pairs import BTC_COP
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Coinbase"
    _uri = "https://api.coinbase.com/v2/prices/BTC-COP/spot"
    _coinpair = BTC_COP

    def _map(self, data):
        return {
            'price':  data['data']['amount']
            }
