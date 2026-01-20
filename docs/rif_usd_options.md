# **Options for the `RIF/USD` price source**

Date: **2026-01-19**




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

| Symbol   | Name    | Char   |
|----------|---------|--------|
| BTC      | Bitcoin | ₿      |
| RIF      | RIF     |        |
| USD      | Dollar  | $      |
| USDT     | Tether  | ₮      |


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


### For coinpair RIF/BTC (from RIF to Bitcoin)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFBTC)


### For coinpair RIF/USDT (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFUSDT)


### For coinpair RIF/USDT(mp1%) (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA) (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA2) (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA3) (from RIF to Tether)

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

Coinpair    V.    Short description     Exchnage    Response        Weight    %  Time
----------  ----  --------------------  ----------  ------------  --------  ---  ------
BTC/USD           Bitcoin to Dollar     Bitfinex    $  93.12300K      0.18   18  0.72s
BTC/USD           Bitcoin to Dollar     Bitstamp    $  93.09100K      0.22   22  0.5s
BTC/USD           Bitcoin to Dollar     Coinbase    $  93.06000K      0.25   25  0.99s
BTC/USD           Bitcoin to Dollar     Gemini      $  93.05700K      0.17   17  1.09s
BTC/USD           Bitcoin to Dollar     Kraken      $  93.07200K      0.18   18  0.73s
BTC/USDT          Bitcoin to Tether     Binance     ₮  93.14848K      0.65   65  0.93s
BTC/USDT          Bitcoin to Tether     Bybit       ₮  93.14315K      0.1    10  0.94s
BTC/USDT          Bitcoin to Tether     Huobi       ₮  93.15667K      0.05    5  0.44s
BTC/USDT          Bitcoin to Tether     KuCoin      ₮  93.14845K      0.05    5  1.11s
BTC/USDT          Bitcoin to Tether     OKX         ₮  93.14225K      0.15   15  1.13s
RIF/BTC           RIF to Bitcoin        Binance     ₿ 380.00000p      1     100  0.94s
RIF/USDT    MA    RIF to Tether         Binance     ₮  37.11407m      1     100  0.92s
RIF/USDT    MA2   RIF to Tether         Binance     ₮  37.12659m      1     100  0.92s
RIF/USDT    MA3   RIF to Tether         Binance     ₮  37.13406m      1     100  0.92s
RIF/USDT    mp1%  To move the price 1%  Binance     ₮  39.48962K      1     100  0.39s
RIF/USDT          RIF to Tether         Binance     ₮  37.10000m      1     100  0.93s
USDT/USD          Tether to Dollar      Bitstamp    $ 999.39500m      0.15   15  0.93s
USDT/USD          Tether to Dollar      Coinbase    $ 999.48500m      0.35   35  0.9s
USDT/USD          Tether to Dollar      Gemini      $ 999.39500m      0.15   15  1.06s
USDT/USD          Tether to Dollar      Kraken      $ 999.41500m      0.35   35  0.92s

    Coinpair                Value   Sources count    Ok
--  --------------  -------------  ---------------  ----
↓   BTC/USD         93,072.000000      5 of 5        ✓
↓   BTC/USDT        93,148.475000      5 of 5        ✓
↓   RIF/BTC          3.800 × 10⁻⁷      1 of 1        ✓
ƒ   RIF/USD              0.035367        N/A         ✓
ƒ   RIF/USD(B)           0.035367        N/A         ✓
ƒ   RIF/USD(T)           0.037078        N/A         ✓
ƒ   RIF/USD(TB)          0.037070        N/A         ✓
ƒ   RIF/USD(TBMA)        0.037084        N/A         ✓
ƒ   RIF/USD(TMA)         0.037092        N/A         ✓
ƒ   RIF/USD(WMTB)        0.036644        N/A         ✓
↓   RIF/USDT             0.037100      1 of 1        ✓
↓   RIF/USDT(MA)         0.037114      1 of 1        ✓
↓   RIF/USDT(MA2)        0.037127      1 of 1        ✓
↓   RIF/USDT(MA3)        0.037134      1 of 1        ✓
↓   RIF/USDT(mp1%)  39,489.616800      1 of 1        ✓
↓   USDT/USD             0.999409      4 of 4        ✓

Response time 1.34s

user@workstation:~$
```

