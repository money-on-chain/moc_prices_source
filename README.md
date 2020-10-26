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
$ moc_prices_source_check 

Coin pair    Exchnage        Response    Weigh     %    Time (s)
-----------  ----------  ------------  -------  ----  ----------
BTC/USD      Bitfinex    13024            0.15  15.4        0.4
BTC/USD      Bitstamp    13027            0.23  22.6        0.24
BTC/USD      Coinbase    13027.9          0.4   40.3        0.26
BTC/USD      Gemini      13031.6          0.06   6.4        0.88
BTC/USD      Kraken      13026.1          0.15  15.2        0.33
RIF/BTC      BitHumb         7.78e-06     0.25  25          1.68
RIF/BTC      Bitfinex        6.36e-06     0.25  25          0.41
RIF/BTC      Coinbene        8.1e-06      0.25  25          0.54
RIF/BTC      Kucoin          7.82e-06     0.25  25          1.38

Coin pair         Mediam           Mean    Weighted median    Sources
-----------  -----------  -------------  -----------------  ---------
BTC/USD      13027        13027.3              13027                5
RIF/BTC          7.8e-06      7.515e-06            7.8e-06          4

Response time 1.69s

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
13025.3
```

Get de RIF BTC coin pair

```
>>> get_price(RIF_BTC)
7.8e-06
```

Get errors detail (example)

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
```

Override the default weighing

```
>>> w = {"btc_usd_bitstamp": 0.2, "btc_usd_bitfinex": 0.8}
>>> get_price(weighing = w)
13024.0
```

Show all details of the coin pair obtained

```
>>> import json
>>> d = {}
>>> values = get_price(detail = d)
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
            "time": 0.309006,
            "timeout": 10,
            "timestamp": "2020-10-26 16:28:23",
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
            "price": 13022.8,
            "time": 0.062697,
            "timeout": 10,
            "timestamp": "2020-10-26 19:28:22",
            "uri": "https://www.bitstamp.net/api/v2/ticker/btcusd/",
            "volume": 3715.32295051,
            "weighing": 0.226189632
        },
        {
            "coinpair": "RIF/BTC",
            "description": "Coinbene",
            "error": null,
            "name": "rif_btc_coinbene",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 7.91e-06,
            "time": 0.487901,
            "timeout": 10,
            "timestamp": "2020-10-26 16:28:23",
            "uri": "http://api.coinbene.com/v1/market/ticker?symbol=RIFBTC",
            "volume": 498517.13,
            "weighing": 0.25
        },
        {
            "coinpair": "BTC/USD",
            "description": "Bitfinex",
            "error": null,
            "name": "btc_usd_bitfinex",
            "ok": true,
            "percentual_weighing": 0.15377828681076447,
            "price": 13024.0,
            "time": 0.287354,
            "timeout": 10,
            "timestamp": "2020-10-26 16:28:23",
            "uri": "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD",
            "volume": 3678.95877958,
            "weighing": 0.1537782868
        },
        {
            "coinpair": "BTC/USD",
            "description": "Gemini",
            "error": null,
            "name": "btc_usd_gemini",
            "ok": true,
            "percentual_weighing": 0.06432022093450242,
            "price": 13022.7,
            "time": 0.274085,
            "timeout": 10,
            "timestamp": "2020-10-26 16:28:23",
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
            "percentual_weighing": 0.40336573282823557,
            "price": 13028.72,
            "time": 0.040915,
            "timeout": 10,
            "timestamp": "2020-10-26 16:28:23",
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
            "price": 13025.3,
            "time": 0.272388,
            "timeout": 10,
            "timestamp": "2020-10-26 16:28:23",
            "uri": "https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD",
            "volume": 3628.17876177,
            "weighing": 0.1523461274
        },
        {
            "coinpair": "RIF/BTC",
            "description": "Kucoin",
            "error": null,
            "name": "rif_btc_kucoin",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 7.82e-06,
            "time": 0.958732,
            "timeout": 10,
            "timestamp": "2020-10-26 16:28:24",
            "uri": "https://openapi-v2.kucoin.com/api/v1/market/orderbook/level1?symbol=RIF-BTC",
            "volume": 1.3437,
            "weighing": 0.25
        },
        {
            "coinpair": "RIF/BTC",
            "description": "BitHumb",
            "error": null,
            "name": "rif_btc_bithumbpro",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 7.78e-06,
            "time": 1.649875,
            "timeout": 10,
            "timestamp": "2020-10-26 16:28:24",
            "uri": "https://global-openapi.bithumb.pro/openapi/v1/spot/ticker?symbol=RIF-BTC",
            "volume": 33072.22,
            "weighing": 0.25
        }
    ],
    "time": 1.706895,
    "values": {
        "BTC/USD": {
            "mean_price": 13024.704,
            "median_price": 13024.0,
            "prices": [
                13022.8,
                13024.0,
                13022.7,
                13028.72,
                13025.3
            ],
            "weighings": [
                0.22618963201583328,
                0.15377828681076447,
                0.06432022093450242,
                0.40336573282823557,
                0.15234612741066422
            ],
            "weighted_median_price": 13025.3
        },
        "RIF/BTC": {
            "mean_price": 7.4675e-06,
            "median_price": 7.8e-06,
            "prices": [
                6.36e-06,
                7.91e-06,
                7.82e-06,
                7.78e-06
            ],
            "weighings": [
                0.25,
                0.25,
                0.25,
                0.25
            ],
            "weighted_median_price": 7.8e-06
        }
    }
}
```