from .pairs import BTC_USD
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "ItBit"
    _uri = "https://api.itbit.com/v1/markets/XBTUSD/ticker"
    _coinpair  = BTC_USD

    def _map(self, data):
        return {
            'price':  data['lastPrice'],
            }
