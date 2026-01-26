from ..base import CoinPair, register_pairs, get_env
from ..coins import ARS, BNB, BTC, COP, ETH, MXN, RIF, USD, USDT



# Pairs

# BNB/USDT
BNB_USDT = CoinPair(BNB, USDT)

# BTC/ARS
BTC_ARS = CoinPair(BTC, ARS,
    min_ok_sources_count=get_env('BTC_ARS_MIN_OK_SOURCES_COUNT', 3, int))

# BTC/COP
BTC_COP = CoinPair(BTC, COP,
    min_ok_sources_count=get_env('BTC_COP_MIN_OK_SOURCES_COUNT', 2, int))

# BTC/USD
BTC_USD = CoinPair(BTC, USD)

# BTC/USDT
BTC_USDT = CoinPair(BTC, USDT)

# ETH/BTC
ETH_BTC = CoinPair(ETH, BTC)

# ETH/USD
ETH_USD = CoinPair(ETH, USD)

# RIF/BTC
RIF_BTC = CoinPair(RIF, BTC)

# RIF/USDT
RIF_USDT = CoinPair(RIF, USDT)
RIF_USDT_MA = CoinPair(RIF, USDT, "MA", "Using [WDAP](fundamentals/wdap.md)")
RIF_USDT_MA2 = CoinPair(RIF, USDT, "MA2")
RIF_USDT_MA3 = CoinPair(RIF, USDT, "MA3")

# USD/ARS
USD_ARS = CoinPair(USD, ARS, description="Free, from the news portals")
USD_ARS_CCL = CoinPair(USD, ARS, "CCL")

# USD/COP
USD_COP = CoinPair(USD, COP, description="Free, from the news portals")

# USD/MXN
USD_MXN = CoinPair(USD, MXN)

# USDT/USD
USDT_USD = CoinPair(USDT, USD)

register_pairs()
