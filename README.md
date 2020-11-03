# MoC prices source

Prices source for MoC projects


## Requirements

* Python 3.6+ support


## Installation

Download from [Github](https://github.com/money-on-chain/moc_prices_source)

Standing inside the folder, run:

```
$ pip3 install -r requirements.txt 
```

For install the dependencies and then run:

```
$ pip3 install .
```

Finally run:

```
$ moc_prices_source_check --version
```

To verify that it has been installed correctly



## Check that all is working ok

```
user@host:~$ moc_prices_source_check 

Coin pair    Exchnage        Response    Weigh     %  Time
-----------  ----------  ------------  -------  ----  ------
BTC/USD      Bitfinex    13349            0.15  15.4  0.41s
BTC/USD      Bitstamp    13361.8          0.23  22.6  0.25s
BTC/USD      Coinbase    13369.3          0.4   40.3  0.31s
BTC/USD      Gemini      13361.3          0.06   6.4  0.88s
BTC/USD      Kraken      13365            0.15  15.2  0.39s
RIF/BTC      BitHumb         7.8e-06      0.25  25    1.91s
RIF/BTC      Bitfinex        6.36e-06     0.25  25    0.44s
RIF/BTC      Coinbene        5.83e-06     0.25  25    0.84s
RIF/BTC      Kucoin          7.58e-06     0.25  25    1.01s

Coin pair           Mediam            Mean    Weighted median  Sources
-----------  -------------  --------------  -----------------  ---------
BTC/USD      13361.8        13361.3             13365          5
RIF/BTC          6.97e-06       6.8925e-06          6.36e-06   4
RIF/USD          0.0931315      0.0920926           0.0850014  N/A

Response time 1.92s

user@host:~$
```

More options

```
user@host:~$ moc_prices_source_check --help
Usage: moc_prices_source_check [OPTIONS]

Options:
  -v, --version   Show version and exit.
  -j, --json      Show data in JSON format and exit.
  -w, --weighing  Show the default weighing and exit.
  -h, --help      Show this message and exit.
user@host:~$ 
```


## Usage

Do some imports first

```
user@host:~$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from moc_prices_source import get_price, BTC_USD, RIF_BTC, ALL
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
>>> values = get_price(ALL, detail = d, serializable = True)
>>>
>>> values
{'RIF/BTC': Decimal('0.00000636'), 'BTC/USD': Decimal('13380.07'), 'RIF/USD': Decimal('0.0850972452')}
>>>
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
            "time": 0.520118,
            "timeout": 10,
            "timestamp": "2020-10-27 11:44:36",
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
            "price": 13385.48,
            "time": 0.331992,
            "timeout": 10,
            "timestamp": "2020-10-27 14:44:34",
            "uri": "https://www.bitstamp.net/api/v2/ticker/btcusd/",
            "volume": 8629.96055351,
            "weighing": 0.226189632
        },
        {
            "coinpair": "RIF/BTC",
            "description": "Coinbene",
            "error": null,
            "name": "rif_btc_coinbene",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 5.87e-06,
            "time": 0.923952,
            "timeout": 10,
            "timestamp": "2020-10-27 11:44:36",
            "uri": "http://api.coinbene.com/v1/market/ticker?symbol=RIFBTC",
            "volume": 502351.35,
            "weighing": 0.25
        },
        {
            "coinpair": "BTC/USD",
            "description": "Bitfinex",
            "error": null,
            "name": "btc_usd_bitfinex",
            "ok": true,
            "percentual_weighing": 0.15377828681076447,
            "price": 13377.0,
            "time": 0.509504,
            "timeout": 10,
            "timestamp": "2020-10-27 11:44:36",
            "uri": "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD",
            "volume": 5274.6920961,
            "weighing": 0.1537782868
        },
        {
            "coinpair": "BTC/USD",
            "description": "Gemini",
            "error": null,
            "name": "btc_usd_gemini",
            "ok": true,
            "percentual_weighing": 0.06432022093450242,
            "price": 13380.27,
            "time": 1.120871,
            "timeout": 10,
            "timestamp": "2020-10-27 11:44:36",
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
            "price": 13380.07,
            "time": 0.29592,
            "timeout": 10,
            "timestamp": "2020-10-27 11:44:35",
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
            "price": 13386.6,
            "time": 0.335535,
            "timeout": 10,
            "timestamp": "2020-10-27 11:44:35",
            "uri": "https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD",
            "volume": 5985.07438025,
            "weighing": 0.1523461274
        },
        {
            "coinpair": "RIF/BTC",
            "description": "Kucoin",
            "error": null,
            "name": "rif_btc_kucoin",
            "ok": true,
            "percentual_weighing": 0.25,
            "price": 7.32e-06,
            "time": 0.927223,
            "timeout": 10,
            "timestamp": "2020-10-27 11:44:36",
            "uri": "https://openapi-v2.kucoin.com/api/v1/market/orderbook/level1?symbol=RIF-BTC",
            "volume": 511.2108,
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
            "time": 1.741697,
            "timeout": 10,
            "timestamp": "2020-10-27 11:44:37",
            "uri": "https://global-openapi.bithumb.pro/openapi/v1/spot/ticker?symbol=RIF-BTC",
            "volume": 39874.55,
            "weighing": 0.25
        }
    ],
    "time": 1.773495,
    "values": {
        "BTC/USD": {
            "mean_price": 13381.884,
            "median_price": 13380.27,
            "prices": [
                13385.48,
                13377.0,
                13380.27,
                13380.07,
                13386.6
            ],
            "weighings": [
                0.22618963201583328,
                0.15377828681076447,
                0.06432022093450242,
                0.4033657328282356,
                0.15234612741066422
            ],
            "weighted_median_price": 13380.07
        },
        "RIF/BTC": {
            "mean_price": 6.8325e-06,
            "median_price": 6.84e-06,
            "prices": [
                6.36e-06,
                5.87e-06,
                7.32e-06,
                7.78e-06
            ],
            "weighings": [
                0.25,
                0.25,
                0.25,
                0.25
            ],
            "weighted_median_price": 6.36e-06
        },
        "RIF/USD": {
            "mean_price": 0.09143172243,
            "median_price": 0.0915210468,
            "requirements": [
                "RIF/BTC",
                "BTC/USD"
            ],
            "weighted_median_price": 0.0850972452
        }
    }
}
>>> 
```
