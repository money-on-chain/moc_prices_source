from ...pairs.simple import BTC_USDT
from .base import EngineBybit, Engines, Decimal, uri



@Engines.register_decorator()
class Engine(EngineBybit):

    _uri = uri(symbol="BTCUSDT")
    _uri_failover = uri(symbol="BTCUSDT", failover=True)
    _coinpair = BTC_USDT
    _max_time_without_price_change = 600 # 10m, zero means infinity

    def _map(self, data):
        data = data['result']['list'][0]        
        return {
            'price': (Decimal(data['bid1Price']) +
                      Decimal(data['ask1Price'])) / Decimal('2')
        }
