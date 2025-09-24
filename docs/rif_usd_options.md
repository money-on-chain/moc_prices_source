# **Options for the `RIF/USD` price source**

Date: **2025-09-24**




## Options

Currently there are **8** options:

* RIF/USD(B)
* RIF/USD(TB)
* RIF/USD(WMTB)
* RIF/USD(T)
* RIF/USD(TBMA)
* RIF/USD(TMA)
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

| Name           | Coinpair   | Variant   | Method   |
|----------------|------------|-----------|----------|
| BTC/USD        | BTC/USD    |           | Weighted |
| BTC/USDT       | BTC/USDT   |           | Weighted |
| RIF/BTC        | RIF/BTC    |           | Weighted |
| RIF/USD        | RIF/USD    |           | Computed |
| RIF/USD(B)     | RIF/USD    | B         | Computed |
| RIF/USD(T)     | RIF/USD    | T         | Computed |
| RIF/USD(TB)    | RIF/USD    | TB        | Computed |
| RIF/USD(TBMA)  | RIF/USD    | TBMA      | Computed |
| RIF/USD(TMA)   | RIF/USD    | TMA       | Computed |
| RIF/USD(WMTB)  | RIF/USD    | WMTB      | Computed |
| RIF/USDT       | RIF/USDT   |           | Weighted |
| RIF/USDT(MA)   | RIF/USDT   | MA        | Weighted |
| RIF/USDT(MA2)  | RIF/USDT   | MA2       | Weighted |
| RIF/USDT(MA3)  | RIF/USDT   | MA3       | Weighted |
| RIF/USDT(mp1%) | RIF/USDT   | mp1%      | Weighted |
| USDT/USD       | USDT/USD   |           | Weighted |

| Method   | Description                                              |
|----------|----------------------------------------------------------|
| Weighted | Weighted median of values ​​obtained from multiple sources |
| Computed | Compute made with previously obtained coinpairs          |

| Name           | Comment/Description                                                 |
|----------------|---------------------------------------------------------------------|
| BTC/USD        |                                                                     |
| BTC/USDT       |                                                                     |
| RIF/BTC        |                                                                     |
| RIF/USD        | Leave this as legacy                                                |
| RIF/USD(B)     | Passing through Bitcoin                                             |
| RIF/USD(T)     | Passing through Tether                                              |
| RIF/USD(TB)    | Passing through Tether & Bitcoin                                    |
| RIF/USD(TBMA)  | Passing through Tether & Bitcoin, using [WDAP](fudamentals/wdap.md) |
| RIF/USD(TMA)   | Passing through Tether, using [WDAP](fudamentals/wdap.md)           |
| RIF/USD(WMTB)  | Passing through Tether & Bitcoin usinng weighted_median             |
| RIF/USDT       |                                                                     |
| RIF/USDT(MA)   | Using [WDAP](fudamentals/wdap.md)                                   |
| RIF/USDT(MA2)  |                                                                     |
| RIF/USDT(MA3)  |                                                                     |
| RIF/USDT(mp1%) | To move the price 1 percent                                         |
| USDT/USD       |                                                                     |


## Formulas used in the computed coinpairs

```
RIF/USD        =  rif_btc * btc_usd
RIF/USD(B)     =  rif_btc * btc_usd
RIF/USD(T)     =  rif_usdt * usdt_usd
RIF/USD(TB)    =  rif_usdt * btc_usd / btc_usdt
RIF/USD(TBMA)  =  rif_usdt_ma * btc_usd / btc_usdt
RIF/USD(TMA)   =  rif_usdt_ma * usdt_usd
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
| Coinbase |     0.25 | https://api.coinbase.com/v2/prices/spot?currency=USD |
| Bitstamp |     0.22 | https://www.bitstamp.net/api/v2/ticker/btcusd/       |
| Bitfinex |     0.18 | https://api-pub.bitfinex.com/v2/ticker/tBTCUSD       |
| Kraken   |     0.18 | https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD |
| Gemini   |     0.17 | https://api.gemini.com/v1/pubticker/BTCUSD           |


### For coinpair RIF/BTC (from RIF Token to Bitcoin)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFBTC)


### For coinpair RIF/USDT (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFUSDT)


### For coinpair RIF/USDT(mp1%) (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA) (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA2) (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA3) (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair BTC/USDT (from Bitcoin to Tether)

| Source   |   Weight | URI                                                                   |
|----------|----------|-----------------------------------------------------------------------|
| Binance  |     0.65 | https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT       |
| OKX      |     0.15 | https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT              |
| Bybit    |     0.10 | https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT  |
| Huobi    |     0.05 | https://api.huobi.pro/market/detail/merged?symbol=btcusdt             |
| KuCoin   |     0.05 | https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT |


### For coinpair USDT/USD (from Tether to Dollar)

| Source   |   Weight | URI                                                        |
|----------|----------|------------------------------------------------------------|
| Bitstamp |     0.15 | https://www.bitstamp.net/api/v2/ticker/usdtusd/            |
| Coinbase |     0.35 | https://api.exchange.coinbase.com/products/USDT-USD/ticker |
| Gemini   |     0.15 | https://api.gemini.com/v1/pubticker/usdtusd                |
| Kraken   |     0.35 | https://api.kraken.com/0/public/Ticker?pair=USDTUSD        |

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
  -v, --version                   Show version and exit.
  -j, --json                      Show data in JSON format and exit.
  -w, --weighing                  Show the default weighing and exit.
  -c, --computed                  Show the computed pairs formula and exit.
  -s, --summary                   Show the summary and exit.
  -m, --markdown                  Set markdown for the summary format.
  -n, --not-ignore-zero-weighing  Not ignore sources with zero weighing.
  -h, --help                      Show this message and exit.

user@workstation:~$ moc_prices_source_check "RIF/USD*"

From       To       V.    Exchnage    Response        Weight    %  Time
---------  -------  ----  ----------  ------------  --------  ---  ------
Bitcoin    Dollar         Bitfinex    $ 113.85000K      0.18   18  0.47s
Bitcoin    Dollar         Bitstamp    $ 113.67200K      0.22   22  0.5s
Bitcoin    Dollar         Coinbase    $ 113.67884K      0.25   25  0.89s
Bitcoin    Dollar         Gemini      $ 113.67177K      0.17   17  0.88s
Bitcoin    Dollar         Kraken      $ 113.67110K      0.18   18  0.94s
Bitcoin    Tether         Binance     ₮ 113.63980K      0.65   65  1.12s
Bitcoin    Tether         Bybit       ₮ 113.63425K      0.1    10  0.61s
Bitcoin    Tether         Huobi       ₮ 113.63100K      0.05    5  0.77s
Bitcoin    Tether         KuCoin      ₮ 113.62295K      0.05    5  1.45s
Bitcoin    Tether         OKX         ₮ 113.63015K      0.15   15  0.79s
RIF Token  Bitcoin        Binance     ₿ 520.00000p      1     100  0.56s
RIF Token  Tether   MA    Binance     ₮  59.23051m      1     100  0.56s
RIF Token  Tether   MA2   Binance     ₮  59.22099m      1     100  0.58s
RIF Token  Tether   MA3   Binance     ₮  59.27884m      1     100  0.59s
RIF Token  Tether   mp1%  Binance     ₮  29.28746K      1     100  0.36s
RIF Token  Tether         Binance     ₮  59.30000m      1     100  0.53s
Tether     Dollar         Bitstamp    $   1.00036       0.15   15  0.51s
Tether     Dollar         Coinbase    $   1.00042       0.35   35  0.73s
Tether     Dollar         Gemini      $   1.00038       0.15   15  0.89s
Tether     Dollar         Kraken      $   1.00024       0.35   35  0.5s

    Coin pair               Mediam            Mean    Weighted median   Sources    Ok
--  --------------  --------------  --------------  -----------------  ---------  ----
↓   BTC/USD         113,672.000000  113,708.742000     113,672.000000   5 of 5     ✓
↓   BTC/USDT        113,631.005000  113,631.630000     113,639.795000   5 of 5     ✓
↓   RIF/BTC               0.000001        0.000001           0.000001   1 of 1     ✓
ƒ   RIF/USD               0.059109        0.059129           0.059109     N/A      ✓
ƒ   RIF/USD(B)            0.059109        0.059129           0.059109     N/A      ✓
ƒ   RIF/USD(T)            0.059322        0.059321           0.059322     N/A      ✓
ƒ   RIF/USD(TB)           0.059321        0.059340           0.059317     N/A      ✓
ƒ   RIF/USD(TBMA)         0.059252        0.059271           0.059247     N/A      ✓
ƒ   RIF/USD(TMA)          0.059253        0.059251           0.059253     N/A      ✓
ƒ   RIF/USD(WMTB)         0.059268        0.059287           0.059265     N/A      ✓
↓   RIF/USDT              0.059300        0.059300           0.059300   1 of 1     ✓
↓   RIF/USDT(MA)          0.059231        0.059231           0.059231   1 of 1     ✓
↓   RIF/USDT(MA2)         0.059221        0.059221           0.059221   1 of 1     ✓
↓   RIF/USDT(MA3)         0.059279        0.059279           0.059279   1 of 1     ✓
↓   RIF/USDT(mp1%)   29,287.460000   29,287.460000      29,287.460000   1 of 1     ✓
↓   USDT/USD              1.000375        1.000352           1.000375   4 of 4     ✓

Response time 1.48s

user@workstation:~$
```

