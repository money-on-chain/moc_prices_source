from .pairs import BTC_ARS
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "MatbaRofex.com.ar"
    _uri = "https://api.matbarofex.com.ar/v1/rest/indices/I.BTC"
    _coinpair = BTC_ARS
    _max_age = 3600 # 1hs.
    _max_time_without_price_change = 0 # zero means infinity

    def _map(self, data):
        return {
            'price': data['indexValue']
        }
