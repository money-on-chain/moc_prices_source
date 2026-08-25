from ...pairs.simple import ETH_BTC
from .base import EngineBinance, Engines, uri



@Engines.register_decorator()
class Engine(EngineBinance):

    _uri = uri(symbol="ETHBTC")
    _coinpair = ETH_BTC
    _max_time_without_price_change = 600 # 10m, zero means infinity


    def _map(self, data):
        return {
            'price':  data['lastPrice'],
            'volume': data['volume']}
