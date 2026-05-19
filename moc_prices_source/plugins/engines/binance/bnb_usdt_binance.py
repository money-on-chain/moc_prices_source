from ...pairs.simple import BNB_USDT
from .base import EngineBinance, Engines, uri



@Engines.register_decorator()
class Engine(EngineBinance):

    _uri = uri(symbol="BNBUSDT")
    _uri_failover = uri(symbol="BNBUSDT", failover=True)
    _coinpair = BNB_USDT

    def _map(self, data):
        return {
            'price':  data['lastPrice'],
            'volume': data['volume']}
