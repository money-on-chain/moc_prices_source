from ...base import BaseWithFailover, Engines, Decimal, envs

base_uri = "https://{host}/{path}?{query}"
host = "api.bybit.com"
host_failover = "moc-proxy-api-bybit.moneyonchain.com"
default_path = "v5/market/tickers"
query = "category=spot&symbol={symbol}"

base_uri = envs(
    'bybit_api_base_uri', base_uri, str,
    description = "URI template to get the price data")

host = envs(
    'bybit_api_host', host, str,
    description = "Host to get the price data")

host_failover = envs(
    'bybit_api_host_failover', host_failover, str,
    description = "Host to get the price data in case of failover")

default_path = envs(
    'bybit_api_default_path', default_path, str,
    description = "Path to get the price data")

query = envs(
    'bybit_api_query', query, str,
    description = "Query template to get the price data")


class SafeDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"


def uri(failover=False, **kwargs):
    base = base_uri.format_map(SafeDict(query=query))
    if not "path" in kwargs:
        kwargs["path"] = default_path
    if not "host" in kwargs:
        kwargs["host"] = host if not failover else host_failover
    out = base.format_map(SafeDict(kwargs))
    return out 

class EngineBybit(BaseWithFailover):

    _description = "Bybit"
    _max_time_without_price_change = 0 # zero means infinity
