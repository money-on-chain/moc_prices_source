from .pairs import BTC_ARS
from .base import Base, engine_register, Decimal



@engine_register()
class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "ArgenBTC"
    _uri         = "https://argenbtc.com/cotizacion"
    _coinpair    = BTC_ARS
    
    _max_age                       = 3600 # 1hs.
    _max_time_without_price_change = 0    # zero means infinity

    def _map(self, data):
        value = {}
        value['price'] = (Decimal(data['precio_compra']) +
                          Decimal(data['precio_venta'])) / Decimal('2')
        return value
