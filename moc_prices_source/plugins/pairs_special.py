from .base import CoinPair, register_pairs
from .coins import BTC, DOC, RIF, USD, USDT



# Special pairs

#Rootstock block number
BLOCK_RSK = CoinPair(name="BLOCK", variant="RSK",
                     short_description = "Rootstock block number")

# DOC/USD
DOC_USD = CoinPair(DOC, USD, short_description="Pegged 1:1 to USD")

# RIF/BTC
RIF_BTC_MP1P = CoinPair(RIF, BTC, "mp1%",
                        description = "To move the price 1 percent",
                        short_description = "To move the price 1%")

# RIF/USDT
RIF_USDT_MP1P = CoinPair(RIF, USDT, "mp1%",
                        description = "To move the price 1 percent",
                        short_description = "To move the price 1%")

register_pairs()
