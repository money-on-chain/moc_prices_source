import sys
from os.path import dirname, abspath



base_dir = dirname(abspath(__file__))

bkpath   = sys.path[:]
sys.path.insert(0, dirname(base_dir), )

from moc_prices_source.engines.coins import CoinPairs
from moc_prices_source.cli import tabulate

sys.path = bkpath


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



if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    show_computed_pairs_fromula()
