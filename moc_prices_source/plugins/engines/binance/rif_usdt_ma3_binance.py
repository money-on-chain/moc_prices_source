from ...pairs.simple import RIF_USDT_MA3
from ...base import Decimal, Engines, envs
from .rif_usdt_ma_binance import Engine as Base



max_quantity = Decimal(envs.value_of('RIF_USD_MA3_DEPTH'))

@Engines.register_decorator()
class Engine(Base):

    _coinpair = RIF_USDT_MA3
    _max_quantity = max_quantity
