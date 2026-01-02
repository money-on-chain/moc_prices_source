import sys
from os.path import dirname, abspath
from fnmatch import fnmatch as match
from typing import Callable, Optional
from types import LambdaType
from inspect import getsource

base_dir = dirname(dirname(abspath(__file__)))
bkpath   = sys.path[:]
sys.path.insert(0, dirname(base_dir))

from moc_prices_source.weighing import weighted_median

sys.path = bkpath



class Coin(object):

    def __init__(self, name: str, symbol: str, small_symbol=None):
        self._name = str(name).strip()
        self._symbol =str(symbol).strip().upper()
        self._small_symbol = str(small_symbol).strip() if small_symbol else None

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def small_symbol(self):
        return self._small_symbol

    def get_symbol(self):
        """ Get small symbol or symbol """
        return self.small_symbol or self.symbol

    @property
    def as_dict(self):
        return {
            'name':         self.name,
            'symbol':       self.symbol,
            'small_symbol': self.small_symbol,
        }

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return "<{} Coin object>".format(self.name)

    def __eq__(self, other):
        return str(self).lower()==str(other).strip().lower()

    def __lt__(self, other):
        return str(self).lower()<str(other).strip().lower()

    def __hash__(self):
        return hash(str(self))


BTC = Coin('Bitcoin', 'btc', '₿')
USD = Coin('Dollar', 'usd', '$')
RIF = Coin('RIF Token', 'rif')
MOC = Coin('MOC Token', 'moc')
ETH = Coin('Ether', 'eth', '⟠')
USDT = Coin('Tether', 'usdt', '₮')
BNB = Coin('Binance Coin', 'bnb', 'Ƀ')
ARS = Coin('Peso Argentino', 'ars', '$')
MXN = Coin('Peso Mexicano', 'mxn', '$')
COP = Coin('Peso Colombiano','cop', '$')
GAS = Coin('Gas', 'gas')
BPRO = Coin('Bpro', 'bpro')
DOC = Coin('DOC Token', 'doc')


Coins = [ c for c in locals().values() if isinstance(c, Coin) ]



def get_coin(value):
    value = str(value).strip().lower()
    try:
        return dict([ (str(c.name).strip().lower(), c) for c in Coins])[value]
    except KeyError:
        return dict([ (str(c).strip().lower(), c) for c in Coins])[value]
        


class CoinPair(object):

    def __init__(self,
                 from_: Optional[Coin] = None,
                 to_: Optional[Coin] = None,
                 variant: Optional[str] = None,
                 description: Optional[str] = None,
                 min_ok_sources_count: int = 0,
                 name: Optional[str] = None,
                 requirements: Optional[list] = None,
                 formula: Optional[Callable] = None,
                 formula_desc: Optional[str] = None):
        if (from_ is None or to_ is None) and name is None:
            raise ValueError("if no name is provided, from_ or to_ "
                             "parameters are required")
        def to_str(x):
            if (bool(x) and str(x).strip()):
                return str(x).strip()
            return None            
        self._from = from_
        self._to = to_
        self._variant = to_str(variant)
        self._description = to_str(description)
        self._name = to_str(name)
        self._min_ok_sources_count = \
            int(min_ok_sources_count) if min_ok_sources_count else 0
        self.set_computed(requirements, formula, formula_desc)

    @property
    def is_computed(self) -> bool:
        return self._formula is not None

    def set_computed(self,
                     requirements: Optional[list] = None,
                     formula: Optional[Callable] = None,
                     formula_desc: Optional[str] = None) -> bool:

        self._requirements = requirements
        self._formula = formula

        if formula is not None and formula_desc is None:
            if isinstance(formula, LambdaType):
                formula_desc = ':'.join(getsource(formula).split('lambda'
                    )[-1].strip().split(':')[1:]).strip()
                if formula_desc[-1]==')': # why?
                    formula_desc = formula_desc[:-1].strip() # why?
            else:
                formula_desc = repr(formula)
            formula_desc = '\n'.join(map(str.strip, formula_desc.split('\n')))

        self._formula_desc = formula_desc

        return self.is_computed
    
    @property
    def requirements(self):
        return self._requirements

    @property
    def formula(self):
        return self._formula

    @property
    def formula_desc(self):
        return self._formula_desc

    @property
    def min_ok_sources_count(self):
        return self._min_ok_sources_count
    
    @property
    def description(self):
        return self._description
    
    @property
    def variant(self):
        return self._variant

    @property
    def from_(self):
        return self._from

    @property
    def to_(self):
        return self._to

    @property
    def long_name(self):
        l = []
        if self.from_ is not None:
            l.append(f"from {self.from_.name}")
        if self.to_ is not None:
            l.append(f"to {self.to_.name}")
        if l:
            return f"{self} ({' '.join(l)})"
        return f"{self}"

    @property
    def name(self):
        if self._name is not None:
            if self.variant is None:
                return f"{self._name}"
            else:
                return f"{self._name}({self.variant})"
        name = f"{self.from_.symbol}/{self.to_.symbol}"
        if self.variant is None:
            return f"{name}"
        else:
            return f"{name}({self.variant})"

    @property
    def as_dict(self):
        return {
            'from': self.from_,
            'to': self.to_,
            'variant': self.variant,
            'name': self.name,
            'description': self.description,
            'is_computed': self.is_computed
        }

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return "<{} Coin Pair object>".format(str(self))

    def __eq__(self, other):
        return str(self).lower()==str(other).strip().lower()

    def __lt__(self, other):
        return str(self).lower()<str(other).strip().lower()

    def __hash__(self):
        return hash(str(self))


# BNB/USDT
BNB_USDT = CoinPair(BNB, USDT)

# BPRO/BTC
BPRO_BTC = CoinPair(BPRO, BTC)

# DOC/USD
DOC_USD = CoinPair(DOC, USD, description="Pegged 1:1 to USD")

# BTC/ARS
BTC_ARS = CoinPair(BTC, ARS, min_ok_sources_count=3)

# BTC/COP
BTC_COP = CoinPair(BTC, COP, min_ok_sources_count=2)

# BTC/USD
BTC_USD = CoinPair(BTC, USD)
BTC_USD_OCH = CoinPair(BTC, USD, "och", "Obtained from the blockchain")

# BTC/USDT
BTC_USDT = CoinPair(BTC, USDT)

# ETH/BTC
ETH_BTC = CoinPair(ETH, BTC)

# ETH/USD
ETH_USD = CoinPair(ETH, USD)

# GAS/BTC Rootstock gas price from nodes
GAS_BTC = CoinPair(GAS, BTC, description="Rootstock gas price from nodes")

# MOC/BTC
MOC_BTC_SOV = CoinPair(MOC, BTC, "Sovryn")

# MOC/USD
MOC_USD_OKU = CoinPair(MOC, USD, "Oku")

# RIF/BTC
RIF_BTC = CoinPair(RIF, BTC)
RIF_BTC_MP1P = CoinPair(RIF, BTC, "mp1%", "To move the price 1 percent")

# RIF/USDT
RIF_USDT = CoinPair(RIF, USDT)
RIF_USDT_MA = CoinPair(RIF, USDT, "MA", "Using [WDAP](fundamentals/wdap.md)")
RIF_USDT_MA2 = CoinPair(RIF, USDT, "MA2")
RIF_USDT_MA3 = CoinPair(RIF, USDT, "MA3")
RIF_USDT_MP1P = CoinPair(RIF, USDT, "mp1%", "To move the price 1 percent")

# USD/ARS
USD_ARS = CoinPair(USD, ARS, description="Free, from the news portals")
USD_ARS_CCL = CoinPair(USD, ARS, "CCL")

# USD/COP
USD_COP = CoinPair(USD, COP, description="Free, from the news portals")

# USD/MXN
USD_MXN = CoinPair(USD, MXN)

# USDT/USD
USDT_USD = CoinPair(USDT, USD)


# Computed pairs

# BNB/USD
BNB_USD = CoinPair(BNB, USD,
    requirements = [BNB_USDT, BTC_USD, BTC_USDT],
    formula = lambda bnb_usdt, btc_usd, btc_usdt: bnb_usdt*btc_usd/btc_usdt)

# BPRO/ARS
BPRO_ARS = CoinPair(BPRO, ARS,
    requirements = [BPRO_BTC, BTC_ARS],
    formula = lambda bpro_btc, btc_ars: bpro_btc * btc_ars)

# BPRO/COP
BPRO_COP = CoinPair(BPRO, COP,
    requirements = [BPRO_BTC, BTC_COP],
    formula = lambda bpro_btc, btc_cop: bpro_btc * btc_cop)

# BPRO/USD
BPRO_USD = CoinPair(BPRO, USD, description="Offchain",
    requirements=[BPRO_BTC, BTC_USD],
    formula = lambda bpro_btc, btc_usd: bpro_btc * btc_usd)

# ETH/USD
ETH_USD_B = CoinPair(ETH, USD, "B", "Passing through Bitcoin",
    requirements = [ETH_BTC, BTC_USD],
    formula = lambda eth_btc, btc_usd: eth_btc * btc_usd)

# MOC/BPRO
MOC_BPRO = CoinPair(MOC, BPRO,
    requirements = [MOC_BTC_SOV, BTC_USD, MOC_USD_OKU, BPRO_BTC],
    formula = lambda moc_btc_sov, btc_usd, moc_usd_oku, bpro_btc: weighted_median(
        [moc_btc_sov * btc_usd, moc_usd_oku],
        [1, 1]) / btc_usd * bpro_btc)

# MOC/BTC
MOC_BTC = CoinPair(MOC, BTC,
    requirements = [MOC_BTC_SOV, BTC_USD, MOC_USD_OKU],
    formula = lambda moc_btc_sov, btc_usd, moc_usd_oku: weighted_median(
        [moc_btc_sov * btc_usd, moc_usd_oku],
        [1, 1]) / btc_usd)

# MOC/USD
MOC_USD = CoinPair(MOC, USD, description="Default option, weighted median",
    requirements = [MOC_BTC_SOV, BTC_USD, MOC_USD_OKU],
    formula = lambda moc_btc_sov, btc_usd, moc_usd_oku: weighted_median(
        [moc_btc_sov * btc_usd, moc_usd_oku],
        [1, 1]))
MOC_USD_SOV = CoinPair(MOC, USD, "Sovryn",
    requirements = [MOC_BTC_SOV, BTC_USD],
    formula = lambda moc_btc_sov, btc_usd: moc_btc_sov * btc_usd)
MOC_USD_WM = CoinPair(MOC, USD, "WM", "Weighted median",
    requirements = [MOC_BTC_SOV, BTC_USD, MOC_USD_OKU],
    formula = lambda moc_btc_sov, btc_usd, moc_usd_oku: weighted_median(
        [moc_btc_sov * btc_usd, moc_usd_oku], [1, 1]))

# RIF/USD
RIF_USD = CoinPair(RIF, USD, description="Leave this as legacy",
    requirements = [RIF_BTC, BTC_USD],
    formula = lambda rif_btc, btc_usd: rif_btc * btc_usd)
RIF_USD_B = CoinPair(RIF, USD, "B", "Passing through Bitcoin",
    requirements = [RIF_BTC, BTC_USD],
    formula = lambda rif_btc, btc_usd: rif_btc * btc_usd)
RIF_USD_T = CoinPair(RIF, USD, "T", "Passing through Tether",
    requirements = [RIF_USDT, USDT_USD],
    formula = lambda rif_usdt, usdt_usd: rif_usdt * usdt_usd)
RIF_USD_TB = CoinPair(RIF, USD, "TB", "Passing through Tether & Bitcoin",
    requirements = [RIF_USDT, BTC_USD, BTC_USDT],
    formula = lambda rif_usdt, btc_usd, btc_usdt: rif_usdt * btc_usd / btc_usdt)
RIF_USD_TBMA = CoinPair(RIF, USD, "TBMA", "Passing through Tether & Bitcoin, using [WDAP](fundamentals/wdap.md)",
    requirements = [RIF_USDT_MA, BTC_USD, BTC_USDT],
    formula = lambda rif_usdt_ma, btc_usd, btc_usdt: rif_usdt_ma * btc_usd / btc_usdt)
RIF_USD_TMA = CoinPair(RIF, USD, "TMA", "Passing through Tether, using [WDAP](fundamentals/wdap.md)",
    requirements = [RIF_USDT_MA, USDT_USD],
    formula = lambda rif_usdt_ma, usdt_usd: rif_usdt_ma * usdt_usd)
RIF_USD_WMTB = CoinPair(RIF, USD, "WMTB", "Passing through Tether & Bitcoin using weighted median",
    requirements = [RIF_USDT, BTC_USD, BTC_USDT, RIF_BTC],
    formula = lambda rif_usdt, btc_usd, btc_usdt, rif_btc: weighted_median(
        [(rif_usdt * btc_usd / btc_usdt), (rif_btc * btc_usd)],
        [0.75, 0.25]))

# USD/ARS
USD_ARS_CCB = CoinPair(USD, ARS, "CCB",
    requirements = [BTC_ARS, BTC_USD],
    formula = lambda btc_ars, btc_usd: btc_ars / btc_usd)

# USD/COP
USD_COP_CCB = CoinPair(USD, COP, "CCB",
    requirements = [BTC_COP, BTC_USD],
    formula = lambda btc_cop, btc_usd: btc_cop / btc_usd)

# USDT/USD
USDT_USD_B = CoinPair(USDT, USD, "B", "Passing through Bitcoin",
    requirements = [BTC_USD, BTC_USDT],
    formula = lambda btc_usd, btc_usdt: btc_usd / btc_usdt)


CoinPairs = [ c for c in locals().values() if isinstance(c, CoinPair) ]



def get_coin_pair(value):
    value = str(value).strip().lower()
    return dict([ (str(c).strip().lower(), c) for c in CoinPairs ])[value]


def get_coin_pairs(
        wildcard: str = "*",
        coinpairs_base: list = None
        ) -> list:
    """
    Get all coin pairs that match the wildcard.
    """
    if coinpairs_base is None:
        coinpairs_base =  CoinPairs
    wildcards_base = str(wildcard).lower().replace(" ", ",").split(",")
    wildcards = list(set([w for w in wildcards_base if w]))
    coinpairs = []
    for w in wildcards:
        f = filter(lambda i: match(str(i).lower(), w), coinpairs_base)
        f = list(set(list(f)))
        coinpairs.extend(f)
    coinpairs = list(set(coinpairs))
    return coinpairs


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    print()
    print('Coins:')
    for c in Coins:
        if c.small_symbol:
            print(f'    {c.name} ({c.symbol} or {c.small_symbol})')
        else:
            print(f'    {c.name} ({c.symbol})')
    print()
    print('Coin pairs:')
    for c in CoinPairs:
        if c.variant:
            print(f'    {c} (from {c.from_.name} to {c.to_.name}, {c.variant})')
        else:    
            print(f'    {c} (from {c.from_.name} to {c.to_.name})')
