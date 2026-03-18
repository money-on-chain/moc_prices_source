from ....pairs.simple import USD_MXN
from ....base import Base, Engines



@Engines.register_decorator()
class Engine(Base):

    _description = "CoinMonitor.info"
    _uri = "https://mx.coinmonitor.info/data_ar_chart_DOLAR.json"
    _coinpair = USD_MXN
    _max_age = 3600 # 1hs.
    _max_time_without_price_change = 0 # zero means infinity

    def _map(self, data):
        return {
            'price':  data[0][1]
        }
