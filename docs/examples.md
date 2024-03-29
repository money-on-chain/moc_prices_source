# **MoC prices source**

This is the python package used in [**Money on Chain**](https://moneyonchain.com/) projects where it is required to get the coinpair values directly from the sources.
This package includes a CLI tool that allows you to query the coinpair values in the same way that [**Money on Chain**](https://moneyonchain.com/) projects do.



## Examples

Do some imports first

```python
user@host:~$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from moc_prices_source import get_price, BTC_USD, RIF_BTC, ALL
>>>
```

Get de `BTC/USD` coin pair

```python
>>> get_price(BTC_USD)
Decimal('13089.82')
>>> 
```

Get de `RIF/BTC` coin pair

```python
>>> get_price(RIF_BTC)
Decimal('0.00000713')
>>> 
```

Get errors detail (forced errors for example)

```python
>>> d = {}
>>> values = get_price(detail = d)
>>> for e in d['prices']:
...     if not e["ok"]:
...         print('{}: {}'.format(e["name"], e["error"]))
...
btc_usd_kraken: HTTPSConnectionPool(host='api.bad_uri.com', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f2c48700b50>: Failed to establish a new connection: [Errno -2] Name or service not known'))
>>>
```

Show the default weighing

```python
>>> from moc_prices_source.weighing import weighing
>>> print(weighing)
Engine                  Weigh
------------------  ---------
btc_usd_bitstamp    0.22619
btc_usd_bitfinex    0.153778
btc_usd_kraken      0.152346
btc_usd_coinbase    0.403366
btc_usd_gemini      0.0643202
rif_btc_bithumbpro  0.333333
rif_btc_kucoin      0.333333
rif_btc_coinbene    0.333333
>>> weighing.as_dict
{'btc_usd_bitstamp': Decimal('0.226189632'), 'btc_usd_bitfinex': Decimal('0.1537782868'), 'btc_usd_kraken': Decimal('0.1523461274'), 'btc_usd_coinbase': Decimal('0.4033657328'), 'btc_usd_gemini': Decimal('0.06432022093'), 'rif_btc_bithumbpro': Decimal('0.333333333'), 'rif_btc_kucoin': Decimal('0.333333333'), 'rif_btc_coinbene': Decimal('0.333333333')}
>>> 
```

Override the default weighing

```python
>>> w = {"btc_usd_bitstamp": 0.2, "btc_usd_bitfinex": 0.8}
>>> get_price(weighing = w)
Decimal('13070')
>>> 
```

Show all details of the coin pair obtained

```python
>>> import json
>>> d = {}
>>> values = get_price(ALL, detail = d, serializable = True)
>>>
>>> values
{<BTC/USD Coin Pair object>: Decimal('15250.00000'), <RIF/BTC Coin Pair object>: Decimal('0.00000637'), <RIF/USD Coin Pair object>: Decimal('0.0971425000000')}
>>>
>>> print(json.dumps(d, indent=4, sort_keys=True))
{
    "prices": [
        {
            "coinpair": "BTC/USD",
            "description": "Bitstamp",
            "error": null,
            "name": "btc_usd_bitstamp",
            "ok": true,
            "percentual_weighing": 0.22618963201583328,
            "price": 15248.38,
            "time": 0.279066,
            "timeout": 10,
            "timestamp": "2020-11-08 14:23:02",
            "uri": "https://www.bitstamp.net/api/v2/ticker/btcusd/",
            "volume": 10835.66006591,
            "weighing": 0.226189632
        },
        {
            "coinpair": "RIF/BTC",
            "description": "Coinbene",
            "error": null,
            "name": "rif_btc_coinbene",
            "ok": true,
            "percentual_weighing": 0.3333333333333333,
            "price": 5.8e-06,
            "time": 1.571258,
            "timeout": 10,
            "timestamp": "2020-11-08 11:23:04",
            "uri": "http://api.coinbene.com/v1/market/ticker?symbol=RIFBTC",
            "volume": 806810.93,
            "weighing": 0.333333333
        },
        {
            "coinpair": "BTC/USD",
            "description": "Bitfinex",
            "error": null,
            "name": "btc_usd_bitfinex",
            "ok": true,
            "percentual_weighing": 0.15377828681076447,
            "price": 15248.22269385,
            "time": 0.267649,
            "timeout": 10,
            "timestamp": "2020-11-08 11:23:02",
            "uri": "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD",
            "volume": 14362.55862314,
            "weighing": 0.1537782868
        },
        {
            "coinpair": "BTC/USD",
            "description": "Gemini",
            "error": null,
            "name": "btc_usd_gemini",
            "ok": true,
            "percentual_weighing": 0.06432022093450242,
            "price": 15254.3,
            "time": 0.952623,
            "timeout": 10,
            "timestamp": "2020-11-08 11:23:03",
            "uri": "https://api.gemini.com/v1/pubticker/BTCUSD",
            "volume": 0.0,
            "weighing": 0.06432022093
        },
        {
            "coinpair": "BTC/USD",
            "description": "Coinbase",
            "error": null,
            "name": "btc_usd_coinbase",
            "ok": true,
            "percentual_weighing": 0.4033657328282356,
            "price": 15251.88,
            "time": 0.246729,
            "timeout": 10,
            "timestamp": "2020-11-08 11:23:02",
            "uri": "https://api.coinbase.com/v2/prices/spot?currency=USD",
            "volume": 0.0,
            "weighing": 0.4033657328
        },
        {
            "coinpair": "BTC/USD",
            "description": "Kraken",
            "error": null,
            "name": "btc_usd_kraken",
            "ok": true,
            "percentual_weighing": 0.15234612741066422,
            "price": 15250.0,
            "time": 0.265883,
            "timeout": 10,
            "timestamp": "2020-11-08 11:23:02",
            "uri": "https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD",
            "volume": 8018.38037875,
            "weighing": 0.1523461274
        },
        {
            "coinpair": "RIF/BTC",
            "description": "Kucoin",
            "error": null,
            "name": "rif_btc_kucoin",
            "ok": true,
            "percentual_weighing": 0.3333333333333333,
            "price": 6.37e-06,
            "time": 0.932421,
            "timeout": 10,
            "timestamp": "2020-11-08 11:23:03",
            "uri": "https://openapi-v2.kucoin.com/api/v1/market/orderbook/level1?symbol=RIF-BTC",
            "volume": 963.5025,
            "weighing": 0.333333333
        },
        {
            "coinpair": "RIF/BTC",
            "description": "BitHumb",
            "error": null,
            "name": "rif_btc_bithumbpro",
            "ok": true,
            "percentual_weighing": 0.3333333333333333,
            "price": 6.67e-06,
            "time": 1.836675,
            "timeout": 10,
            "timestamp": "2020-11-08 11:23:04",
            "uri": "https://global-openapi.bithumb.pro/openapi/v1/spot/ticker?symbol=RIF-BTC",
            "volume": 27932.67,
            "weighing": 0.333333333
        }
    ],
    "time": 1.882155,
    "values": {
        "BTC/USD": {
            "mean_price": 15250.55653877,
            "median_price": 15250.0,
            "prices": [
                15248.38,
                15248.22269385,
                15254.3,
                15251.88,
                15250.0
            ],
            "weighings": [
                0.22618963201583328,
                0.15377828681076447,
                0.06432022093450242,
                0.4033657328282356,
                0.15234612741066422
            ],
            "weighted_median_price": 15250.0
        },
        "RIF/BTC": {
            "mean_price": 6.28e-06,
            "median_price": 6.37e-06,
            "prices": [
                5.8e-06,
                6.37e-06,
                6.67e-06
            ],
            "weighings": [
                0.3333333333333333,
                0.3333333333333333,
                0.3333333333333333
            ],
            "weighted_median_price": 6.37e-06
        },
        "RIF/USD": {
            "mean_price": 0.0957734950634756,
            "median_price": 0.0971425,
            "requirements": [
                "RIF/BTC",
                "BTC/USD"
            ],
            "weighted_median_price": 0.0971425
        }
    }
}
>>> 
```

`Coin object` and `Coin Pair object` usage:

```python
>>> BTC_USD
<BTC/USD Coin Pair object>
>>> str(BTC_USD)
'BTC/USD'
>>> BTC_USD.from_
<Bitcoin Coin object>
>>> str(BTC_USD.from_)
'BTC'
>>> BTC_USD.to_
<Dollar Coin object>
>>> str(BTC_USD.to_)
'USD'
>>> BTC_USD.from_.symbol
'BTC'
>>> BTC_USD.from_.name
'Bitcoin'
>>> BTC_USD.from_.small_symbol
'₿'
>>>
```