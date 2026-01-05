from .pairs import BTC_USDT
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Kraken"
    _uri = "https://api.kraken.com/0/public/Ticker?pair=XBTUSDT"
    _coinpair = BTC_USDT
    _max_time_without_price_change = 600 # 10m, zero means infinity

    def _map(self, data):
        return {
            'price':  data['result']['XBTUSDT']['c'][0],
            'volume': data['result']['XBTUSDT']['v'][1] }
