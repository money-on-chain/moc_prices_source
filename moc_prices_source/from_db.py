import sys, json
from datetime import datetime, timedelta
from os.path import dirname, abspath, basename, expanduser
from tabulate import tabulate
from fnmatch import fnmatch as match
from redis import Redis
from json.decoder import JSONDecodeError
from sys import stderr
from collections import namedtuple


bkpath   = sys.path[:]
base_dir = dirname(abspath(__file__))
sys.path.insert(0, dirname(base_dir))

from moc_prices_source import ALL, BTC_USD
from moc_prices_source.cli import command, cli

sys.path = bkpath
app_name = 'moc_prices_source'



Price = namedtuple('Price', 'value timestamp')


class FromDB(object):

    def __init__(self, max_age=None):

        if max_age is not None:
            if isinstance(max_age, (int, float)):
                max_age = timedelta(seconds=max_age)
            if not isinstance(max_age, timedelta):
                raise TypeError('max_age')

        self._default_max_age = max_age
        
        app_dir  = dirname(abspath(__file__))
        app_name = basename(app_dir)
        redis_conf_files = [
            expanduser("~") + '/.' + app_name + '/redis.json',
            expanduser("~") + '/.' + app_name + '/redis_default.json',
            app_dir + '/data/redis.json',
            app_dir + '/data/redis_default.json']
        redis_conf = {}
        for file_ in redis_conf_files:
            try:
                with open(file_, 'r') as f:
                    redis_conf = json.load(f)
            except JSONDecodeError as e:
                print(f'Error in "{file_}", {str(e)}', file=stderr)
                exit(1)
            except Exception as e:
                redis_conf = {}
            if redis_conf:
                break

        if not redis_conf.get('enable', False):
            print(f'Error, Redis not enabled in config (File: {file_})',
                  file=stderr)
            exit(1)

        redis_connection = {}

        for key, type_ in [('host', str),
                           ('port', int),
                           ('db', int),
                           ('unix_socket_path', str)]:
            if key in redis_conf:
                try:
                    redis_connection[key] = type_(redis_conf[key])
                except Exception as e:
                    print(f'Error in "{file_}", {str(e)}', file=stderr)
                    exit(1)

        try:
            self._redis = Redis(**redis_connection)
            self._redis.ping()
        except Exception as e:
            print(f'Error in "{file_}", {str(e)}', file=stderr)
            exit(1)

    def __call__(self, *coinpairs, max_age=None):

        if max_age is None:
            max_age = self._default_max_age

        if not coinpairs:
            coinpairs = ALL

        coinpairs = list(coinpairs)

        only_one=False
        if len(coinpairs)==1:
            if isinstance(coinpairs[0], (tuple, list)):
                coinpairs = coinpairs[0]
            else:
                only_one= True

        now = None
        if max_age is not None:
            if isinstance(max_age, (int, float)):
                max_age = timedelta(seconds=max_age)
            if not isinstance(max_age, timedelta):
                raise TypeError('max_age')
        if max_age==timedelta(0):
            max_age = None
        if max_age is not None:
            now = datetime.now()

        out = {}
        for coinpair in coinpairs:
            key = f"{app_name}/{str(coinpair).replace('/', '_')}_ok_value" 
            key_timestamp = f"{key}/timestamp"
            timestamp_raw = (self._redis.get(key_timestamp))
            if timestamp_raw is None:
                continue
            value_raw = (self._redis.get(key))
            if value_raw is None:
                continue
            timestamp = datetime.fromtimestamp(json.loads(timestamp_raw))
            if max_age is not None:
                age = now - timestamp
                if age > max_age:
                    continue
            value = json.loads(value_raw)
            out[coinpair] = Price(value, timestamp)

        if len(out)==1 and only_one:
            return list(out.values())[0]

        return out


@command()
@cli.argument('coinpairs_filter', required=False)
def cli_values_from_db(coinpairs_filter = None):
    """\b
Description:
    CLI-type tool that see the data obtained by
    the `moc_price_source` library from RedisDB.
\n\b
COINPAIRS_FILTER:
    Is a display pairs filter that accepts wildcards.
    Example: "btc*"
    Default value: "*" (all available pairs)
"""
    from_db = FromDB()
    if coinpairs_filter:
        coinpairs = list(filter(
            lambda i: match(str(i).lower(), str(coinpairs_filter).lower()),
            ALL))
    else:
        coinpairs = ALL
    if not coinpairs:
        print(
            f"The {repr(coinpairs_filter)} filter did not return any results.",
            file=stderr)
        return 1
    
    data = from_db(coinpairs)
    table = [[str(c), p.value, p.timestamp] for (c, p) in data.items()]
    
    print(tabulate(table, headers=['CoinPair', 'Value', 'Last date/time']))



if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    from_db = FromDB()
    print(from_db(BTC_USD, max_age=None))
    
