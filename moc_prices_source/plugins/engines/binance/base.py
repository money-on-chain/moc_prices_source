from ...base import BaseWithFailover, Engines, Decimal, envs

base_uri = "https://{host}/{path}?{query}"
host = "api.binance.com"
host_failover = "moc-proxy-api-binance.moneyonchain.com"
default_path = "api/v3/ticker/24hr"
query = "symbol={symbol}"

base_uri = envs(
    'binance_api_base_uri', base_uri, str,
    description = "URI template to get the price data")

host = envs(
    'binance_api_host', host, str,
    description = "Host to get the price data")

host_failover = envs(
    'binance_api_host_failover', host_failover, str,
    description = "Host to get the price data in case of failover")

default_path = envs(
    'binance_api_default_path', default_path, str,
    description = "Path to get the price data")

query = envs(
    'binance_api_query', query, str,
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

class EngineBinance(BaseWithFailover):

    _description = "Binance"
    _max_time_without_price_change = 0 # zero means infinity
