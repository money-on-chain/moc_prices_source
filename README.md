# MoC prices source

Prices source for MoC projects

## Requirements

* Python 3.6+ support

## Installation

```
pip3 install .
```

## Check that all is working ok

```
$ ./moc_prices_source_check 

Coin pair    Exchnage        Response    Weigh     %  Time
-----------  ----------  ------------  -------  ----  ------
BTC/USD      Bitfinex    13073            0.15  15.4  0.57s
BTC/USD      Bitstamp    13082.6          0.23  22.6  0.96s
BTC/USD      Coinbase    13080.1          0.4   40.3  0.32s
BTC/USD      Gemini      13084.7          0.06   6.4  1.14s
BTC/USD      Kraken      13083.8          0.15  15.2  0.57s
RIF/BTC      BitHumb         8.26e-06     0.25  25    1.96s
RIF/BTC      Bitfinex        6.36e-06     0.25  25    0.57s
RIF/BTC      Coinbene        7.09e-06     0.25  25    0.56s
RIF/BTC      Kucoin          7.86e-06     0.25  25    1.57s

Coin pair           Mediam            Mean    Weighted median    Sources
-----------  -------------  --------------  -----------------  ---------
BTC/USD      13082.6        13080.8              13080.1               5
RIF/BTC          7.475e-06      7.3925e-06           7.09e-06          4

Response time 1.96s

$ 
```

More options

```
$ moc_prices_source_check --help
Usage: moc_prices_source_check [OPTIONS]

Options:
  -v, --version   Show version and exit.
  -j, --json      Show data in JSON format and exit.
  -w, --weighing  Show the default weighing and exit.
  -h, --help      Show this message and exit.
$ 
```

## Usage

Do some imports first

```
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from moc_prices_source import get_price, BTC_USD, RIF_BTC
>>>
```

Get de BTC USD coin pair

```
>>> get_price(BTC_USD)
Decimal('13089.82')
>>> 
```

Get de RIF BTC coin pair

```
>>> get_price(RIF_BTC)
Decimal('0.00000713')
>>> 
```

Get errors detail (forced errors for example)

```
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

```
>>> from moc_prices_source.weighing import weighing
>>> print(weighing)
Engine                  Weigh
------------------  ---------
btc_usd_bitstamp    0.22619
btc_usd_bitfinex    0.153778
btc_usd_kraken      0.152346
btc_usd_coinbase    0.403366
btc_usd_gemini      0.0643202
rif_btc_bitfinex    0.25
rif_btc_bithumbpro  0.25
rif_btc_kucoin      0.25
rif_btc_coinbene    0.25
>>> weighing.as_dict
{'btc_usd_bitstamp': Decimal('0.226189632'), 'btc_usd_bitfinex': Decimal('0.1537782868'), 'btc_usd_kraken': Decimal('0.1523461274'), 'btc_usd_coinbase': Decimal('0.4033657328'), 'btc_usd_gemini': Decimal('0.06432022093'), 'rif_btc_bitfinex': Decimal('0.25'), 'rif_btc_bithumbpro': Decimal('0.25'), 'rif_btc_kucoin': Decimal('0.25'), 'rif_btc_coinbene': Decimal('0.25')}
>>> 
```

Override the default weighing

```
>>> w = {"btc_usd_bitstamp": 0.2, "btc_usd_bitfinex": 0.8}
>>> get_price(weighing = w)
Decimal('13070')
>>> 
```

Show all details of the coin pair obtained

```
>>> import json
>>> d = {}
>>> values = get_price(detail = d, serializable = True)
>>> values
{'RIF/BTC': Decimal('0.00000716'), 'BTC/USD': Decimal('13074.22')}
>>> print(json.dumps(d, indent=4, sort_keys=True))
{
    "prices": [
        {
            "coinpair": "RIF/BTC",
            "description": "Bitfinex",
            "error": null,
            "name": "rif_btc_bitfinex",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 6.36e-06,
            "time": 0.429792,
            "timeout": 10,
            "timestamp": "2020-10-26 20:51:09",
            "uri": "https://api-pub.bitfinex.com/v2/ticker/tRIFBTC",
            "volume": 199741.08473236,
            "weighing": 0.25
        },
        {
            "coinpair": "BTC/USD",
            "description": "Bitstamp",
            "error": null,
            "name": "btc_usd_bitstamp",
            "ok": true,
            "percentual_weighing": 0.22618963201583328,
            "price": 13080.65,
            "time": 0.251088,
            "timeout": 10,
            "timestamp": "2020-10-26 23:51:07",
            "uri": "https://www.bitstamp.net/api/v2/ticker/btcusd/",
            "volume": 5713.48411002,
            "weighing": 0.226189632
        },
        {
            "coinpair": "RIF/BTC",
            "description": "Coinbene",
            "error": null,
            "name": "rif_btc_coinbene",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 7.16e-06,
            "time": 1.239262,
            "timeout": 10,
            "timestamp": "2020-10-26 20:51:10",
            "uri": "http://api.coinbene.com/v1/market/ticker?symbol=RIFBTC",
            "volume": 503652.44,
            "weighing": 0.25
        },
        {
            "coinpair": "BTC/USD",
            "description": "Bitfinex",
            "error": null,
            "name": "btc_usd_bitfinex",
            "ok": true,
            "percentual_weighing": 0.15377828681076447,
            "price": 13072.0,
            "time": 0.265143,
            "timeout": 10,
            "timestamp": "2020-10-26 20:51:09",
            "uri": "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD",
            "volume": 3672.97820899,
            "weighing": 0.1537782868
        },
        {
            "coinpair": "BTC/USD",
            "description": "Gemini",
            "error": null,
            "name": "btc_usd_gemini",
            "ok": true,
            "percentual_weighing": 0.06432022093450242,
            "price": 13084.25,
            "time": 0.912977,
            "timeout": 10,
            "timestamp": "2020-10-26 20:51:10",
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
            "price": 13074.22,
            "time": 0.290297,
            "timeout": 10,
            "timestamp": "2020-10-26 20:51:09",
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
            "price": 13082.6,
            "time": 0.353133,
            "timeout": 10,
            "timestamp": "2020-10-26 20:51:09",
            "uri": "https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD",
            "volume": 4652.36723363,
            "weighing": 0.1523461274
        },
        {
            "coinpair": "RIF/BTC",
            "description": "Kucoin",
            "error": null,
            "name": "rif_btc_kucoin",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 7.91e-06,
            "time": 1.1693310000000001,
            "timeout": 10,
            "timestamp": "2020-10-26 20:51:10",
            "uri": "https://openapi-v2.kucoin.com/api/v1/market/orderbook/level1?symbol=RIF-BTC",
            "volume": 1.5133,
            "weighing": 0.25
        },
        {
            "coinpair": "RIF/BTC",
            "description": "BitHumb",
            "error": null,
            "name": "rif_btc_bithumbpro",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 8.26e-06,
            "time": 1.7340659999999999,
            "timeout": 10,
            "timestamp": "2020-10-26 20:51:11",
            "uri": "https://global-openapi.bithumb.pro/openapi/v1/spot/ticker?symbol=RIF-BTC",
            "volume": 46691.13,
            "weighing": 0.25
        }
    ],
    "time": 1.854053,
    "values": {
        "BTC/USD": {
            "mean_price": 13078.744,
            "median_price": 13080.65,
            "prices": [
                13080.65,
                13072.0,
                13084.25,
                13074.22,
                13082.6
            ],
            "weighings": [
                0.22618963201583328,
                0.15377828681076447,
                0.06432022093450242,
                0.4033657328282356,
                0.15234612741066422
            ],
            "weighted_median_price": 13074.22
        },
        "RIF/BTC": {
            "mean_price": 7.4225e-06,
            "median_price": 7.535e-06,
            "prices": [
                6.36e-06,
                7.16e-06,
                7.91e-06,
                8.26e-06
            ],
            "weighings": [
                0.25,
                0.25,
                0.25,
                0.25
            ],
            "weighted_median_price": 7.16e-06
        }
    }
}
>>> 
```