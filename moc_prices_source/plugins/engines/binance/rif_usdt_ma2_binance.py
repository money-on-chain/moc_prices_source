from ...pairs.simple import RIF_USDT_MA2
from ...base import get_env, Decimal, Engines
from .rif_usdt_ma_binance import Engine as Base



max_quantity = Decimal(get_env('MA_MAX2_QUANTITY', 200000, int))

@Engines.register_decorator()
class Engine(Base):

    _coinpair = RIF_USDT_MA2
    _max_quantity = max_quantity
