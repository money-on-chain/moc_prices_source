from ...pairs.simple import BTC_ARS
from .base import EngineBinance, Engines, uri



@Engines.register_decorator()
class Engine(EngineBinance):

    _uri = uri(symbol="BTCARS")
    _coinpair = BTC_ARS
    _max_age = 3600 # 1hs.

    def _map(self, data):
        return {
            'price':  data['lastPrice'],
            'volume': data['volume']}
