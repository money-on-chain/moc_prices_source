__version__ = '0.1.0'

import sys, json, datetime
from os.path import dirname, abspath
from decimal import Decimal

sys.path.append(dirname(abspath(__file__)))

from engines      import get_coinpair_list, get_engines_names, get_prices
from engines.base import BTC_USD, RIF_BTC
from weighing     import weighing, weighted_median, median, mean



def get_price(
    coinpairs     = None,
    engines_names = None,
    detail        = {},
    weighing      = weighing,
    serializable  = False):

    start_time = datetime.datetime.now()

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

    detail['values'] = coinpair_prices

    out = {}

    for key, value in coinpair_prices.items():
        out[key] = value['weighted_median_price']

    if len(out)==1:
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
                d[k] = [ float(x) for x in d[k] ]
            for k in ['median_price', 'mean_price', 'weighted_median_price']:
                d[k] = float(d[k])

    if not out:
        return None

    return out



if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    detail = {}
    output = get_price(detail=detail, serializable=True)
    print()
    print(json.dumps(detail, indent=4, sort_keys=True))
    print()
    print('output = {}'.format(repr(output)))
