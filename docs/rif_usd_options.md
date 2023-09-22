# **Options for the `RIF/USD` price source**

Date: **2023-09-22**




## Options

Currently there are **6** options:

* RIF/USD(B)
* RIF/USD(TB)
* RIF/USD(WMTB)
* RIF/USD(T)
* RIF/USDT(MA)
* RIF/USDT

## Rationale behind the chosen nomenclature

`RIF/USD(B)`: Because it goes through *RIF/**B**itcoin* and ***B**itcoin/Dollar* to reach the desired pair.

`RIF/USD(TB)`: Because it goes through *RIF/**T**ether*, ***B**itcoin/Dollar* and *Bitcoin/**T**ether* to get to the desired pair.

`RIF/USD(T)`: Because it goes through *RIF/**T**ether* and ***T**ether/Dollar* to reach the desired pair.

`RIF/USD(WMTB)`: Because uses a **W**eighted **M**edian between `RIF/USD(B)` and `RIF/USD(TB)` to reach the desired pair.

`RIF/USDT(MA)`: Because uses the `RIF/USDT` with the "**M**agic **A**verage" algorithm analyzing the orderbook depth.

`RIF/USDT`: Because uses directly the `RIF/USDT` pair.


## Symbols

| Symbol   | Name      | Char   |
|----------|-----------|--------|
| BTC      | Bitcoin   | ₿      |
| RIF      | RIF Token |        |
| USD      | Dollar    | $      |
| USDT     | Tether    | ₮      |


## Coinpairs

| Name          | Coinpair   | Variant   | Method   |
|---------------|------------|-----------|----------|
| BTC/USD       | BTC/USD    |           | Weighted |
| BTC/USDT      | BTC/USDT   |           | Weighted |
| RIF/BTC       | RIF/BTC    |           | Weighted |
| RIF/USD       | RIF/USD    |           | Computed |
| RIF/USD(B)    | RIF/USD    | B         | Computed |
| RIF/USD(T)    | RIF/USD    | T         | Computed |
| RIF/USD(TB)   | RIF/USD    | TB        | Computed |
| RIF/USD(WMTB) | RIF/USD    | WMTB      | Computed |
| RIF/USDT      | RIF/USDT   |           | Weighted |
| RIF/USDT(MA)  | RIF/USDT   | MA        | Weighted |
| USDT/USD      | USDT/USD   |           | Weighted |

| Method   | Description                                              |
|----------|----------------------------------------------------------|
| Weighted | Weighted median of values ​​obtained from multiple sources |
| Computed | Compute made with previously obtained coinpairs          |


## Formulas used in the computed coinpairs

```
RIF/USD        =  rif_btc * btc_usd
RIF/USD(B)     =  rif_btc * btc_usd
RIF/USD(T)     =  rif_usdt * usdt_usd
RIF/USD(TB)    =  rif_usdt * btc_usd / btc_usdt
RIF/USD(WMTB)  =  weighted_median(
                  [(rif_usdt * btc_usd / btc_usdt), (rif_btc * btc_usd)],
                  [0.75, 0.25])
```


## Weights used for each obtained coinpairs from multiple sources

If a price source is not available, this source is discarded
and the rest of the sources are used but with their weights recalculated
proportionally.
For example, you have 3 sources with 3 weights A:0.2, B:0.5, C:0.3
and if for some reason B would not be available, A:0.4, C:0.6 would
be used.

The weights used are fixed values.
These weightings are related to the historical volume handled by each
price source.
Every established period of time we review the historical volume of the
sources and if necessary we apply the changes to the parameterization.


### For coinpair BTC/USD (from Bitcoin to Dollar)

| Source   |   Weight | URI                                                  |
|----------|----------|------------------------------------------------------|
| Bitstamp |     0.22 | https://www.bitstamp.net/api/v2/ticker/btcusd/       |
| Bitfinex |     0.18 | https://api-pub.bitfinex.com/v2/ticker/tBTCUSD       |
| Kraken   |     0.18 | https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD |
| Coinbase |     0.25 | https://api.coinbase.com/v2/prices/spot?currency=USD |
| Gemini   |     0.17 | https://api.gemini.com/v1/pubticker/BTCUSD           |


### For coinpair RIF/BTC (from RIF Token to Bitcoin)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFBTC)


### For coinpair RIF/USDT (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA) (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair BTC/USDT (from Bitcoin to Tether)

| Source   |   Weight | URI                                                       |
|----------|----------|-----------------------------------------------------------|
| Binance  |     0.80 | https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT |
| Bitfinex |     0.05 | https://api-pub.bitfinex.com/v2/ticker/tBTCUST            |
| Kraken   |     0.05 | https://api.kraken.com/0/public/Ticker?pair=XBTUSDT       |
| Coinbase |     0.10 | https://api.coinbase.com/v2/exchange-rates?currency=BTC   |


### For coinpair USDT/USD (from Tether to Dollar)

| Source   |   Weight | URI                                                      |
|----------|----------|----------------------------------------------------------|
| Bitstamp |     0.15 | https://www.bitstamp.net/api/v2/ticker/usdtusd/          |
| Coinbase |     0.45 | https://api.coinbase.com/v2/exchange-rates?currency=USDT |
| Kraken   |     0.40 | https://api.kraken.com/0/public/Ticker?pair=USDTZUSD     |

## The `moc_prices_source_check` tool

There is a tool that comes with the [`moc_prices_source` package](https://github.com/money-on-chain/moc_prices_source) that allows us to run a simulation that queries and calculates all the coinpairs.
This tool is called `moc_prices_source_check` and here you can see an example of its use.

### Example

```shell
user@workstation:~$ moc_prices_source_check --help
Usage: moc_prices_source_check [OPTIONS] [COINPAIRS_FILTER]

  Description:
      CLI-type tool that shows the data obtained by
      the `moc_price_source` library.   
      Useful for troubleshooting.

  COINPAIRS_FILTER:
      Is a display pairs filter that accepts wildcards.
      Example: "btc*"
      Default value: "*" (all available pairs)

Options:
  -v, --version   Show version and exit.
  -j, --json      Show data in JSON format and exit.
  -w, --weighing  Show the default weighing and exit.
  -c, --computed  Show the computed pairs formula and exit.
  -s, --summary   Show the summary and exit.
  -m, --markdown  Set markdown for the summary format.
  -h, --help      Show this message and exit.

user@workstation:~$ moc_prices_source_check "RIF/USD*"

From       To       V.    Exchnage        Response                Weight  %      Time
---------  -------  ----  --------------  --------------------  --------  -----  ------
Bitcoin    Dollar         Bitfinex        $  26.62700K              0.18  18.0   0.45s
Bitcoin    Dollar         Bitstamp        $  26.59600K              0.22  22.0   0.97s
Bitcoin    Dollar         Coinbase        $  26.59408K              0.25  25.0   0.45s
Bitcoin    Dollar         Gemini          $  26.59234K              0.17  17.0   1.16s
Bitcoin    Dollar         Kraken          $  26.59240K              0.18  18.0   0.34s
Bitcoin    Tether         Binance         ₮  26.60006K              0.8   80.0   0.76s
Bitcoin    Tether         Bitfinex        ₮  26.60400K              0.05  5.0    0.56s
Bitcoin    Tether         Coinbase        ₮  26.59673K              0.1   10.0   0.39s
Bitcoin    Tether         Kraken          ₮  26.60140K              0.05  5.0    0.55s
RIF Token  Bitcoin        Binance         ₿   2.57000µ              1     100.0  0.76s
RIF Token  Bitcoin        BitHumb         HTTPSConnectio [...]      0     N/A    N/A
RIF Token  Bitcoin        Coingecko       ₿   2.56000µ              0     N/A    0.55s
RIF Token  Bitcoin        MEXC            ₿   2.57900µ              0     N/A    0.66s
RIF Token  Bitcoin        Sovryn onchain  ₿   2.57035µ              0     N/A    1.41s
RIF Token  Tether   MA    Binance         ₮  68.26544m              1     100.0  0.75s
RIF Token  Tether         Binance         ₮  68.10000m              1     100.0  0.75s
Tether     Dollar         Bitstamp        $ 999.91000m              0.15  15.0   0.65s
Tether     Dollar         Coinbase        $ 999.94500m              0.45  45.0   0.4s
Tether     Dollar         Kraken          $ 999.79000m              0.4   40.0   0.56s

    Coin pair               Mediam             Mean    Weighted median  Sources
--  -------------  ---------------  ---------------  -----------------  ---------
↓   BTC/USD        26594.1          26600.4              26594.1        5
↓   BTC/USDT       26600.7          26600.5              26600.1        4
↓   RIF/BTC            2.57017e-06      2.56984e-06          2.57e-06   4
ƒ   RIF/USD            0.0683514        0.0683586            0.0683468  N/A
ƒ   RIF/USD(B)         0.0683514        0.0683586            0.0683468  N/A
ƒ   RIF/USD(T)         0.0680939        0.0680919            0.0680939  N/A
ƒ   RIF/USD(TB)        0.068083         0.0680995            0.0680845  N/A
ƒ   RIF/USD(WMTB)      0.0681501        0.0681643            0.0681501  N/A
↓   RIF/USDT           0.0681           0.0681               0.0681     1
↓   RIF/USDT(MA)       0.0682654        0.0682654            0.0682654  1
↓   USDT/USD           0.99991          0.999882             0.99991    3

Response time 1.44s

user@workstation:~$
```

