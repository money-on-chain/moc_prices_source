__version__ = '0.1.3b'

import sys, json, datetime
from os.path import dirname, abspath
from decimal import Decimal

bkpath   = sys.path[:]
base_dir = dirname(abspath(__file__))
sys.path.append(base_dir)

from engines      import get_coinpair_list, get_engines_names, get_prices
from engines.base import BTC_USD, RIF_BTC
from weighing     import weighing, weighted_median, median, mean

sys.path = bkpath



RIF_USD = 'RIF/USD'

ALL = [BTC_USD, RIF_BTC, RIF_USD]

computed_pairs = {
    RIF_USD: {
        'requirements': [RIF_BTC, BTC_USD],
        'formula': lambda rif_btc, btc_usd: rif_btc * btc_usd
    }
}



def get_price(
    coinpairs     = None,
    engines_names = None,
    detail        = {},
    weighing      = weighing,
    serializable  = False):

    start_time = datetime.datetime.now()

    requested = coinpairs

    if coinpairs:

        if not isinstance(coinpairs, list):
            coinpairs = [coinpairs]

        requested = coinpairs

        new_coinpairs = []
        for c in coinpairs:
            if c in computed_pairs:
                for r in computed_pairs[c]['requirements']:
                    new_coinpairs.append(r)
        coinpairs = list(set(new_coinpairs))

    if 'as_dict' in dir(weighing):
        weighing = weighing.as_dict
    else:
        for key, value in weighing.items():
            weighing[key] = Decimal(str(value))

    if engines_names==None:
        engines_names = list(weighing.keys())

    prices = get_prices(
        coinpairs     = coinpairs,
        engines_names = engines_names)

    for value in prices:
        value['weighing'] = weighing.get(value['name'], Decimal('0.0'))

    detail['prices'] = prices

    coinpair_prices = {}
    for value in prices:
        value['percentual_weighing'] = None
        if value['ok']:
            if not value['coinpair'] in coinpair_prices:
                coinpair_prices[value['coinpair']] = {
                    'data': [],
                    'sum_weighing': Decimal('0.0')}
            coinpair_prices[value['coinpair']]['data'].append(value)
            coinpair_prices[value['coinpair']]['sum_weighing'] += value['weighing']

    for d in coinpair_prices.values():
        sum_weighing = d['sum_weighing']
        for v in d['data']:
            weighing = v['weighing']
            if not weighing:
                percentual_weighing = 0
            elif not sum_weighing:
                percentual_weighing = 0
            else:
                percentual_weighing = weighing / sum_weighing
            v['percentual_weighing'] = percentual_weighing

    for d in coinpair_prices.values():
        if not 'weighings' in d:
            d['weighings'] = []
        if not 'prices' in d:
            d['prices'] = []
        for v in d['data']:
            d['weighings'].append(v['percentual_weighing'])
            d['prices'].append(v['price'])
        del d['data']
        del d['sum_weighing']
        d['median_price'] = median(d['prices'])
        d['mean_price'] = mean(d['prices'])
        d['weighted_median_price'] = weighted_median(d['prices'], d['weighings'])

    if requested:
        for r in [r for r in requested if (
            (r in computed_pairs) and (not r in coinpair_prices)) ]:
            requirements = computed_pairs[r]['requirements']
            if set(requirements).issubset(set(coinpair_prices.keys())):
                coinpair_prices[r] = {}
                coinpair_prices[r]['requirements'] = requirements
                formula = computed_pairs[r]['formula']
                for k in ['median_price', 'mean_price', 'weighted_median_price']:
                    args = [ coinpair_prices[q][k] for q in requirements ]
                    try:
                        coinpair_prices[r][k] = formula(*args)
                    except:
                        coinpair_prices[r][k] = None

    detail['values'] = coinpair_prices

    out = {}

    for key, value in coinpair_prices.items():
        if requested:
            if key in requested:
                if value['weighted_median_price']:
                    out[key] = value['weighted_median_price']
        else:
            if value['weighted_median_price']:
                out[key] = value['weighted_median_price']

    if requested and len(requested)==1:
        if requested[0] in out:
            out = out[requested[0]]
        else:
            out = None

    if not(requested) and  len(out)==1:
        out = list(out.values())[0]

    detail['time'] = datetime.datetime.now() - start_time

    if serializable:
        detail['time'] = detail['time'].seconds + detail['time'].microseconds/1000000
        for p in prices:
            if p['time']:
                p['time'] = p['time'].seconds + p['time'].microseconds/1000000
            p['timestamp'] = str(p['timestamp'])
            if p['error']:
                p['error'] = str(p['error'])
            for k in ['price', 'weighing', 'percentual_weighing', 'volume']:
                p[k] = float(p[k])
        for d in coinpair_prices.values():
            for k in ['weighings', 'prices']:
                if k in d:
                    d[k] = [ float(x) for x in d[k] ]
            for k in ['median_price', 'mean_price', 'weighted_median_price']:
                if d[k]:
                    d[k] = float(d[k])

    if not out:
        return None

    return out



if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    detail = {}
    output = get_price(ALL, detail=detail, serializable=True)
    print()
    print(json.dumps(detail, indent=4, sort_keys=True))
    print()
    print('output = {}'.format(repr(output)))
