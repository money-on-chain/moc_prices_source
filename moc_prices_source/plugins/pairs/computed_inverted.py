from ...types import Decimal, FancyDecimal, Any
from ...pairs import get_coin_pairs
from ..base import CoinPairs, CoinPair, CoinPairType, Formula, \
    RegistryCoinPairs



# Pairs to invert
wildcard_pairs_to_invert_include = ""
wildcard_pairs_to_invert_exclude = ""


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

def callback(self: RegistryCoinPairs, key, value):
    if (wildcard_pairs_to_invert_exclude and
        get_coin_pairs(wildcard_pairs_to_invert_exclude,
                       coinpairs_base=[value])):
        return
    if not(wildcard_pairs_to_invert_include and
           get_coin_pairs(wildcard_pairs_to_invert_include,
                          coinpairs_base=[value])):
        return
    if value.type == CoinPairType.INVERTED:
        return
    inverted_name = make_inverted_name(value)
    if inverted_name in self:
        return
    try:
        inverted_pair = make_inverted_pair(value)
    except TypeError as e:
        self._logger.warning(
            f"Cannot create inverted pair for {value}: {e}")
        return
    self[inverted_name] = inverted_pair
    self._logger.info(f"Adds inverted pair {inverted_pair} from {value}")

if wildcard_pairs_to_invert_include or \
   wildcard_pairs_to_invert_exclude:
    CoinPairs.register_callback(callback)
