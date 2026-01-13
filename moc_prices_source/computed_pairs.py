from .plugins import CoinPairs
from .cli import tabulate



ComputedCoinPairs = dict(
    [ (name, obj) for name, obj in CoinPairs.items() if obj.is_computed ])


computed_pairs = {}
for c in ComputedCoinPairs.values():
    computed_pairs[c] = {
        'requirements': c.requirements,
        'formula': c.formula,
        'formula_desc': c.formula_desc
    }


for name, coinpair in ComputedCoinPairs.items():
    locals()[name] = coinpair
del name, coinpair


def show_computed_pairs_fromula():
    print()
    print("Computed pairs formula")
    print("-------- ----- -------")
    print("")
    table = [[str(pair), '=', data['formula_desc']] for pair,
             data in computed_pairs.items()]
    print(tabulate(table, tablefmt='plain'))
    print("")
