from .pairs import BTC_USD
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Kucoin"
    _uri = "https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT"
    _coinpair = BTC_USD

    def _map(self, data):
        return {
            'price':  data['data']['last'],
            'volume': data['data']['vol'] }
