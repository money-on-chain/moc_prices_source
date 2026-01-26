from .base import CoinPair, register_pairs, Formula
from ..types import Decimal, FancyDecimal, Any
from .pairs_onchain import BPRO_BTC
from .pairs_computed import RIF_USD_WMTB, BPRO_ARS



# Pairs to invert
pairs_to_invert = [BPRO_BTC, RIF_USD_WMTB, BPRO_ARS]

def is_lambda(obj: Any) -> bool:
    return callable(obj) and getattr(obj, "__name__", None) == "<lambda>"

def inverted_formula(value) -> FancyDecimal:
    if value == 0:
        raise ZeroDivisionError("Cannot invert zero value")
    return FancyDecimal(Decimal(1) / Decimal(value))

def make_inverted_class(base):
    class Inverted_Formula(base):
        def return_value(self):
            self.value = inverted_formula(self.value)
            return self.value
    return Inverted_Formula

def make_inverted_pair(base_pair: CoinPair) -> CoinPair:
    args = [base_pair.to_, base_pair.from_, base_pair.variant]
    if base_pair.is_computed:
        if is_lambda(base_pair.formula) or \
                base_pair.formula is inverted_formula:
            inverted_func = lambda *args, **kwargs: inverted_formula(
                base_pair.formula(*args, **kwargs))
            return CoinPair(*args,
                requirements = base_pair.requirements,
                formula = inverted_func,
                formula_desc = f"({base_pair.formula_desc})⁻¹")
        elif issubclass(base_pair.formula, Formula):
            InvertedClass = make_inverted_class(base_pair.formula)
            return CoinPair(*args,
                requirements = base_pair.requirements,
                formula = InvertedClass,
                formula_desc = f"({base_pair})⁻¹")
        else:
            raise TypeError("Unsupported formula type for inversion")
    else:
        return CoinPair(*args,
            requirements = [base_pair],
            formula = inverted_formula,
            formula_desc = f"({base_pair})⁻¹")

def make_inverted_name(base_pair: CoinPair) -> str:
    args = [base_pair.to_, base_pair.from_, base_pair.variant]
    return '_'.join([str(obj) for obj in args if obj is not None])

for pair in pairs_to_invert:
    locals()[make_inverted_name(pair)] = make_inverted_pair(pair)

register_pairs()
