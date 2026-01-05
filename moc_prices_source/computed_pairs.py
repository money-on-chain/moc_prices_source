from .plugins import CoinPairs
from .cli import tabulate



ComputedCoinPairs = [ c for c in CoinPairs if c.is_computed ]
computed_pairs = {}
for c in ComputedCoinPairs:
    computed_pairs[c] = {
        'requirements': c.requirements,
        'formula': c.formula,
        'formula_desc': c.formula_desc
    }

def show_computed_pairs_fromula():
    print()
    print("Computed pairs formula")
    print("-------- ----- -------")
    print("")
    table = [[str(pair), '=', data['formula_desc']] for pair,
             data in computed_pairs.items()]
    print(tabulate(table, tablefmt='plain'))
    print("")
