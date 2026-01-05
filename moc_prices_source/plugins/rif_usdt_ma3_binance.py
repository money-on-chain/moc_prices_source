from .pairs import RIF_USDT_MA3
from .base import get_env, Decimal, engine_register
from .rif_usdt_ma_binance import Engine as Base



max_quantity = Decimal(get_env('MA_MAX3_QUANTITY', '600000'))

@engine_register()
class Engine(Base):

    _coinpair = RIF_USDT_MA3
    _max_quantity = max_quantity
