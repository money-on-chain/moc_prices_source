from .base import CoinPair, register_pairs
from .coins import BPRO, BTC, GAS, MOC, RIF, USD



# Onchain pairs 

# BPRO/BTC
BPRO_BTC = CoinPair(BPRO, BTC,
                    description = "Obtained from MOC onchain")

# BTC/USD
BTC_USD_OCH = CoinPair(BTC, USD, "och",
                       description = "Obtained from the blockchain")

# GAS/BTC Rootstock gas price from nodes
GAS_BTC = CoinPair(GAS, BTC,
                   description = "Rootstock gas price from nodes",
                   short_description = "Rootstock gas price")

# MOC/BTC
MOC_BTC_SOV = CoinPair(MOC, BTC, "sov",
                       description = "Obtained from Sovryn onchain")

# MOC/USD
MOC_USD_OKU = CoinPair(MOC, USD, "Oku")

register_pairs()
