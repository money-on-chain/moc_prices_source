from ...types import Decimal, FancyDecimal, Any
from ..base import CoinPair, CoinPairType, Formula, register_pairs
# from .onchain import AAA_BBB, CCC_DDD
# from .computed import EEE_FFF, GGG_HHH



# Pairs to invert
pairs_to_invert = [] #[AAA_BBB, CCC_DDD, EEE_FFF, GGG_HHH]

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
                formula_desc = f"({base_pair.formula_desc})⁻¹",
                type_ = CoinPairType.INVERTED)
        elif issubclass(base_pair.formula, Formula):
            InvertedClass = make_inverted_class(base_pair.formula)
            return CoinPair(*args,
                requirements = base_pair.requirements,
                formula = InvertedClass,
                formula_desc = f"({base_pair.formula_desc})⁻¹",
                type_ = CoinPairType.INVERTED)
        else:
            raise TypeError("Unsupported formula type for inversion")
    else:
        return CoinPair(*args,
            requirements = [base_pair],
            formula = inverted_formula,
            formula_desc = \
                f"({base_pair.name_base.lower().replace('/', '_')})⁻¹",
            type_ = CoinPairType.INVERTED)

def make_inverted_name(base_pair: CoinPair) -> str:
    args = [base_pair.to_, base_pair.from_, base_pair.variant]
    return '_'.join([str(obj) for obj in args if obj is not None])

if pairs_to_invert:
    for pair in pairs_to_invert:
        locals()[make_inverted_name(pair)] = make_inverted_pair(pair)
    register_pairs()
