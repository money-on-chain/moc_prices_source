from ...pairs.simple import BTC_USDT
from .base import EngineBinance, Engines, Decimal, uri



@Engines.register_decorator()
class Engine(EngineBinance):

    _uri = uri(symbol="BTCUSDT", path="api/v3/ticker/bookTicker")
    _coinpair = BTC_USDT
    _max_time_without_price_change = 600 # 10m, zero means infinity


    def _map(self, data):
        return {
            'price': (Decimal(data['askPrice']) +
                      Decimal(data['bidPrice'])) / Decimal('2')
        }
