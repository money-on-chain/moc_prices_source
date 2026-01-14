# **Options for the `RIF/USD` price source**

Date: **2026-01-14**




## Options

Currently there are **8** options:

* RIF/USD(B)
* RIF/USD(T)
* RIF/USD(TB)
* RIF/USD(TBMA)
* RIF/USD(TMA)
* RIF/USD(WMTB)
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

| Name           | Comment/Description                                                  |
|----------------|----------------------------------------------------------------------|
| BTC/USD        |                                                                      |
| BTC/USDT       |                                                                      |
| RIF/BTC        |                                                                      |
| RIF/USD        | Leave this as legacy                                                 |
| RIF/USD(B)     | Passing through Bitcoin                                              |
| RIF/USD(T)     | Passing through Tether                                               |
| RIF/USD(TB)    | Passing through Tether & Bitcoin                                     |
| RIF/USD(TBMA)  | Passing through Tether & Bitcoin, using [WDAP](fundamentals/wdap.md) |
| RIF/USD(TMA)   | Passing through Tether, using [WDAP](fundamentals/wdap.md)           |
| RIF/USD(WMTB)  | Passing through Tether & Bitcoin using weighted median               |
| RIF/USDT       |                                                                      |
| RIF/USDT(MA)   | Using [WDAP](fundamentals/wdap.md)                                   |
| RIF/USDT(MA2)  |                                                                      |
| RIF/USDT(MA3)  |                                                                      |
| RIF/USDT(mp1%) | To move the price 1 percent                                          |
| USDT/USD       |                                                                      |


## Formulas used in the computed coinpairs

```
RIF/USD        =  rif_btc × btc_usd
RIF/USD(B)     =  rif_btc × btc_usd
RIF/USD(T)     =  rif_usdt × usdt_usd
RIF/USD(TB)    =  rif_usdt × btc_usd / btc_usdt
RIF/USD(TBMA)  =  rif_usdt_ma × btc_usd / btc_usdt
RIF/USD(TMA)   =  rif_usdt_ma × usdt_usd
RIF/USD(WMTB)  =  Weighted(
                    (rif_usdt × btc_usd / btc_usdt) at 75%,
                    (rif_btc × btc_usd) at 25%
                  )
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
Bitcoin    Dollar         Bitfinex    $  97.09200K      0.18   18  0.11s
Bitcoin    Dollar         Bitstamp    $  97.27600K      0.22   22  0.31s
Bitcoin    Dollar         Coinbase    $  97.27414K      0.25   25  0.29s
Bitcoin    Dollar         Gemini      $  97.25560K      0.17   17  0.74s
Bitcoin    Dollar         Kraken      $  97.24360K      0.18   18  0.22s
Bitcoin    Tether         Binance     ₮  97.28348K      0.65   65  0.42s
Bitcoin    Tether         Bybit       ₮  97.27945K      0.1    10  0.48s
Bitcoin    Tether         Huobi       ₮  97.26786K      0.05    5  0.38s
Bitcoin    Tether         KuCoin      ₮  97.28005K      0.05    5  0.43s
Bitcoin    Tether         OKX         ₮  97.27485K      0.15   15  0.45s
RIF Token  Bitcoin        Binance     ₿ 380.00000p      1     100  0.39s
RIF Token  Tether   MA    Binance     ₮  37.45000m      1     100  0.37s
RIF Token  Tether   MA2   Binance     ₮  37.44656m      1     100  0.39s
RIF Token  Tether   MA3   Binance     ₮  37.44311m      1     100  0.4s
RIF Token  Tether   mp1%  Binance     ₮  50.99398K      1     100  0.36s
RIF Token  Tether         Binance     ₮  37.50000m      1     100  0.39s
Tether     Dollar         Bitstamp    $ 999.85500m      0.15   15  0.78s
Tether     Dollar         Coinbase    $ 999.91000m      0.35   35  0.41s
Tether     Dollar         Gemini      $ 999.92500m      0.15   15  0.75s
Tether     Dollar         Kraken      $ 999.88000m      0.35   35  0.27s

    Coin pair               Value   Sources count    Ok
--  --------------  -------------  ---------------  ----
↓   BTC/USD         97,255.600000      5 of 5        ✓
↓   BTC/USDT        97,283.485000      5 of 5        ✓
↓   RIF/BTC          3.800 × 10⁻⁷      1 of 1        ✓
ƒ   RIF/USD              0.036957        N/A         ✓
ƒ   RIF/USD(B)           0.036957        N/A         ✓
ƒ   RIF/USD(T)           0.037496        N/A         ✓
ƒ   RIF/USD(TB)          0.037489        N/A         ✓
ƒ   RIF/USD(TBMA)        0.037439        N/A         ✓
ƒ   RIF/USD(TMA)         0.037446        N/A         ✓
ƒ   RIF/USD(WMTB)        0.037356        N/A         ✓
↓   RIF/USDT             0.037500      1 of 1        ✓
↓   RIF/USDT(MA)         0.037450      1 of 1        ✓
↓   RIF/USDT(MA2)        0.037447      1 of 1        ✓
↓   RIF/USDT(MA3)        0.037443      1 of 1        ✓
↓   RIF/USDT(mp1%)  50,993.980800      1 of 1        ✓
↓   USDT/USD             0.999894      4 of 4        ✓

Response time 0.85s

user@workstation:~$
```

