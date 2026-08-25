from ...base import Base, Engines, Decimal, envs

base_uri = "https://{host}/{path}?{query}"
host = "api.bybit.com"
default_path = "v5/market/tickers"
query = "category=spot&symbol={symbol}"
api_proxy = None

base_uri = envs(
    'bybit_api_base_uri', base_uri, str,
    description = "URI template to get the price data")

host = envs(
    'bybit_api_host', host, str,
    description = "Host to get the price data")

default_path = envs(
    'bybit_api_default_path', default_path, str,
    description = "Path to get the price data")

query = envs(
    'bybit_api_query', query, str,
    description = "Query template to get the price data")

proxy = envs(
    'bybit_api_proxy', api_proxy, envs.types.url,
    description = "Proxy for Bybit")


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

class EngineBybit(Base):

    _description = "Bybit"
    _max_time_without_price_change = 0 # zero means infinity
    _url_proxy = proxy
