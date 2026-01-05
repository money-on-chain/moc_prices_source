from .pairs import BTC_COP
from .base import Base, engine_register, Decimal



@engine_register()
class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "cryptomkt.com"
    _uri         = "https://api.exchange.cryptomkt.com/api/3/public/ticker/BTCCOP"
    _coinpair    = BTC_COP
    
    _max_age                       = 3600 # 1hs.
    _max_time_without_price_change = 0    # zero means infinity

    def _map(self, data):
        return {
            'price': (Decimal(data['ask']) + Decimal(data['bid'])) / Decimal('2'),
            'volume': data['volume']
        }
