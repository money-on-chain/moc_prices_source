from ...pairs.simple import RIF_USDT
from .base import EngineBinance, Engines, uri



@Engines.register_decorator()
class Engine(EngineBinance):

    _uri = uri(symbol="RIFUSDT")
    _coinpair = RIF_USDT

    def _map(self, data):
        return {
            'price':  data['lastPrice'],
            'volume': data['volume']}
