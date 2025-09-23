# **Options for the `RIF/USD` price source**

Date: **2025-09-23**




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

| Name           | Comment/Description                                                                      |
|----------------|------------------------------------------------------------------------------------------|
| BTC/USD        |                                                                                          |
| BTC/USDT       |                                                                                          |
| RIF/BTC        |                                                                                          |
| RIF/USD        | Leave this as legacy                                                                     |
| RIF/USD(B)     | Passing through Bitcoin                                                                  |
| RIF/USD(T)     | Passing through Tether                                                                   |
| RIF/USD(TB)    | Passing through Tether & Bitcoin                                                         |
| RIF/USD(TBMA)  | Passing through Tether & Bitcoin, using the magic average algorithm with orderbook depth |
| RIF/USD(TMA)   | Passing through Tether, using the magic average algorithm with orderbook depth           |
| RIF/USD(WMTB)  | Passing through Tether & Bitcoin usinng weighted_median                                  |
| RIF/USDT       |                                                                                          |
| RIF/USDT(MA)   | Using the magic average algorithm with orderbook depth                                   |
| RIF/USDT(MA2)  |                                                                                          |
| RIF/USDT(MA3)  |                                                                                          |
| RIF/USDT(mp1%) | To move the price 1 percent                                                              |
| USDT/USD       |                                                                                          |


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
Bitcoin    Dollar         Bitfinex    $ 112.10000K      0.18   18  0.25s
Bitcoin    Dollar         Bitstamp    $ 111.93500K      0.22   22  0.37s
Bitcoin    Dollar         Coinbase    $ 111.92238K      0.25   25  0.63s
Bitcoin    Dollar         Gemini      $ 111.92007K      0.17   17  1.01s
Bitcoin    Dollar         Kraken      $ 111.93070K      0.18   18  0.18s
Bitcoin    Tether         Binance     ₮ 111.91594K      0.65   65  0.4s
Bitcoin    Tether         Bybit       ₮ 111.88505K      0.1    10  0.53s
Bitcoin    Tether         Huobi       ₮ 111.91862K      0.05    5  1.3s
Bitcoin    Tether         KuCoin      ₮ 111.91805K      0.05    5  1.22s
Bitcoin    Tether         OKX         ₮ 111.90795K      0.15   15  0.82s
RIF Token  Bitcoin        Binance     ₿ 530.00000p      1     100  0.38s
RIF Token  Tether   MA    Binance     ₮  59.04660m      1     100  0.37s
RIF Token  Tether   MA2   Binance     ₮  59.05730m      1     100  0.42s
RIF Token  Tether   MA3   Binance     ₮  59.13350m      1     100  0.43s
RIF Token  Tether   mp1%  Binance     ₮  20.31000K      1     100  0.35s
RIF Token  Tether         Binance     ₮  59.00000m      1     100  0.37s
Tether     Dollar         Bitstamp    $   1.00025       0.15   15  0.36s
Tether     Dollar         Coinbase    $   1.00033       0.35   35  1.05s
Tether     Dollar         Gemini      $   1.00054       0.15   15  1.01s
Tether     Dollar         Kraken      $   1.00008       0.35   35  0.51s

    Coin pair               Mediam            Mean    Weighted median   Sources    Ok
--  --------------  --------------  --------------  -----------------  ---------  ----
↓   BTC/USD         111,930.700000  111,961.629000     111,930.700000   5 of 5     ✓
↓   BTC/USDT        111,915.945000  111,909.124000     111,915.945000   5 of 5     ✓
↓   RIF/BTC               0.000001        0.000001           0.000001   1 of 1     ✓
ƒ   RIF/USD               0.059323        0.059340           0.059323     N/A      ✓
ƒ   RIF/USD(B)            0.059323        0.059340           0.059323     N/A      ✓
ƒ   RIF/USD(T)            0.059017        0.059018           0.059023     N/A      ✓
ƒ   RIF/USD(TB)           0.059008        0.059028           0.059008     N/A      ✓
ƒ   RIF/USD(TBMA)         0.059054        0.059074           0.059054     N/A      ✓
ƒ   RIF/USD(TMA)          0.059064        0.059064           0.059070     N/A      ✓
ƒ   RIF/USD(WMTB)         0.059087        0.059106           0.059087     N/A      ✓
↓   RIF/USDT              0.059000        0.059000           0.059000   1 of 1     ✓
↓   RIF/USDT(MA)          0.059047        0.059047           0.059047   1 of 1     ✓
↓   RIF/USDT(MA2)         0.059057        0.059057           0.059057   1 of 1     ✓
↓   RIF/USDT(MA3)         0.059134        0.059134           0.059134   1 of 1     ✓
↓   RIF/USDT(mp1%)   20,309.995000   20,309.995000      20,309.995000   1 of 1     ✓
↓   USDT/USD              1.000290        1.000300           1.000398   4 of 4     ✓

Response time 1.34s

user@workstation:~$
```

