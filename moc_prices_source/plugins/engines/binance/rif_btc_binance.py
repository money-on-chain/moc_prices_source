from ...pairs.simple import RIF_BTC
from .base import EngineBinance, Engines, uri



@Engines.register_decorator()
class Engine(EngineBinance):

    _uri = uri(symbol="RIFBTC")
    _uri_failover = uri(symbol="RIFBTC", failover=True)
    _coinpair = RIF_BTC

    def _map(self, data):
        return {
            'price':  data['lastPrice'],
            'volume': data['volume']}
