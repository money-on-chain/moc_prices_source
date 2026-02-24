from ..base import CoinPairs, CoinPair, envs
from ..coins import ARS, BNB, BTC, COP, ETH, MXN, RIF, USD, USDT



# Pairs

# BNB/USDT
BNB_USDT = CoinPair(BNB, USDT)

# BTC/ARS
BTC_ARS = CoinPair(BTC, ARS,
    min_ok_sources_count=envs('BTC_ARS_MIN_OK_SOURCES_COUNT', 3,
        envs.types.positive_integer,
        description = "Minimum number of sources to consider BTC/ARS valid"))

# BTC/COP
BTC_COP = CoinPair(BTC, COP,
    min_ok_sources_count=envs('BTC_COP_MIN_OK_SOURCES_COUNT', 2,
        envs.types.positive_integer,
        description = "Minimum number of sources to consider BTC/COP valid"))

# BTC/USD
BTC_USD = CoinPair(BTC, USD, min_ok_sources_count=1)

# BTC/USDT
BTC_USDT = CoinPair(BTC, USDT, min_ok_sources_count=1)

# ETH/BTC
ETH_BTC = CoinPair(ETH, BTC, min_ok_sources_count=1)

# ETH/USD
ETH_USD = CoinPair(ETH, USD, min_ok_sources_count=1)

# RIF/BTC
RIF_BTC = CoinPair(RIF, BTC)

# RIF/USDT
RIF_USDT = CoinPair(RIF, USDT)

depth = envs('RIF_USD_MA_DEPTH', 100000, int,
             description = "Depth in RIF for RIF/USDT(MA) or RIF/USD(MA)")
depth_2 = envs('RIF_USD_MA2_DEPTH', 200000, int,
               description = "Depth in RIF for RIF/USDT(MA2) or RIF/USD(MA2)")
depth_3 = envs('RIF_USD_MA3_DEPTH', 600000, int,
               description = "Depth in RIF for RIF/USDT(MA3) or RIF/USD(MA3)")

depth = f"{int(depth/1000)}k"
depth_2 = f"{int(depth_2/1000)}k"
depth_3 = f"{int(depth_3/1000)}k"

RIF_USDT_MA = CoinPair(RIF, USDT, "MA",
    f"Using [DWAP](fundamentals/dwap.md), {depth} depth")

RIF_USDT_MA2 = CoinPair(RIF, USDT, "MA2",
    f"Using [DWAP](fundamentals/dwap.md), {depth_2} depth")

RIF_USDT_MA3 = CoinPair(RIF, USDT, "MA3",
    f"Using [DWAP](fundamentals/dwap.md), {depth_3} depth")

# USD/ARS
USD_ARS = CoinPair(USD, ARS, min_ok_sources_count=1,
                   description="Free, from press portals")
USD_ARS_CCL = CoinPair(USD, ARS, "CCL", min_ok_sources_count=1)

# USD/COP
USD_COP = CoinPair(USD, COP, min_ok_sources_count=1,
                   description="Free, from press portals")

# USD/MXN
USD_MXN = CoinPair(USD, MXN, min_ok_sources_count=1)

# USDT/USD
USDT_USD = CoinPair(USDT, USD, min_ok_sources_count=1)

CoinPairs.register()
