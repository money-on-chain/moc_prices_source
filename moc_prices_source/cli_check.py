#!/usr/bin/env python3
import json, sys
from os.path  import dirname, abspath
from cli      import command, option, tabulate, trim
from weighing import weighing

sys.path.append(dirname(dirname(abspath(__file__))))

from moc_prices_source import __version__ as version
from moc_prices_source import get_price



@command()
@option('-v', '--version', 'show_version', is_flag=True,
        help='Show version and exit.')
@option('-j', '--json', 'show_json', is_flag=True,
        help='Show data in JSON format and exit.')
@option('-w', '--weighing', 'show_weighing', is_flag=True,
        help='Show the default weighing and exit.')
def cli_check(show_version=False, show_json=False, show_weighing=False):

    if show_version:
        print(version)
        return

    if show_weighing:
        print()
        print(weighing)
        print()
        return

    data = {}
    
    get_price(detail=data)

    if show_json:
        print(json.dumps(data, indent=4, sort_keys=True))
        return

    time   = data['time']
    prices = data['prices']
    values = data['values']

    table=[]
    for p in prices:
        row = []
        row.append(p["coinpair"])
        row.append(p["description"])
        if p["ok"]:
            row.append(p["price"])
        else:
            row.append(trim(p["error"], 25))
        row.append(round(p["weighing"], 2))
        if p["percentual_weighing"]:
            row.append(round(p[
                "percentual_weighing"]*100, 1))
        else:
            row.append(None)
        if p["time"]:
            row.append(round(p["time"], 2))
        else:
            row.append(None)
        table.append(row)
    if table:
        table.sort()
        print()
        print(tabulate(table, headers=[
            'Coin pair', 'Exchnage', 'Response', 'Weigh', '%', 'Time (s)'
        ]))

    table=[]
    for coinpair, d in values.items():
        row = []
        row.append(coinpair)
        row.append(d['median_price'])
        row.append(d['mean_price'])
        row.append(d['weighted_median_price'])
        row.append(len(d['prices']))
        table.append(row)
    if table:
        table.sort()
        print()
        print(tabulate(table, headers=[
            'Coin pair', 'Mediam', 'Mean', 'Weighted median', 'Sources'
        ]))
    
    print()
    print('Response time {}s'.format(round(time, 2)))
    print()



if __name__ == '__main__':
    cli_check()
