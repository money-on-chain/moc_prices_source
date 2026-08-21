from ...base import Base, Engines, Decimal, envs

base_uri = "https://{host}/{path}?{query}"
host = "api.binance.com"
default_path = "api/v3/ticker/24hr"
query = "symbol={symbol}"
api_proxy = None

base_uri = envs(
    'binance_api_base_uri', base_uri, str,
    description = "URI template to get the price data")

host = envs(
    'binance_api_host', host, str,
    description = "Host to get the price data")

default_path = envs(
    'binance_api_default_path', default_path, str,
    description = "Path to get the price data")

query = envs(
    'binance_api_query', query, str,
    description = "Query template to get the price data")

proxy = envs(
    'binance_api_proxy', api_proxy, str,
    description = "Proxy for Binance")


class SafeDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"


def uri(**kwargs):
    base = base_uri.format_map(SafeDict(query=query))
    if not "path" in kwargs:
        kwargs["path"] = default_path
    if not "host" in kwargs:
        kwargs["host"] = host
    out = base.format_map(SafeDict(kwargs))
    return out 

class EngineBinance(Base):

    _description = "Binance"
    _max_time_without_price_change = 0 # zero means infinity
    _url_proxy = proxy
