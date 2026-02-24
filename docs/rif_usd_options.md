# **Options for the `RIF/USD` price source**

Date: **2026-02-19**




## Options

Currently there are **10** options:

* RIF/USD(B)
* RIF/USD(T)
* RIF/USD(TB)
* RIF/USD(TBMA)
* RIF/USD(TMA)
* RIF/USD(TMA2)
* RIF/USD(TMA3)
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
| RIF/BTC        | RIF/BTC    |           | Direct   |
| RIF/USD        | RIF/USD    |           | Computed |
| RIF/USD(B)     | RIF/USD    | B         | Computed |
| RIF/USD(T)     | RIF/USD    | T         | Computed |
| RIF/USD(TB)    | RIF/USD    | TB        | Computed |
| RIF/USD(TBMA)  | RIF/USD    | TBMA      | Computed |
| RIF/USD(TMA)   | RIF/USD    | TMA       | Computed |
| RIF/USD(TMA2)  | RIF/USD    | TMA2      | Computed |
| RIF/USD(TMA3)  | RIF/USD    | TMA3      | Computed |
| RIF/USD(WMTB)  | RIF/USD    | WMTB      | Computed |
| RIF/USDT       | RIF/USDT   |           | Direct   |
| RIF/USDT(MA)   | RIF/USDT   | MA        | Direct   |
| RIF/USDT(MA2)  | RIF/USDT   | MA2       | Direct   |
| RIF/USDT(MA3)  | RIF/USDT   | MA3       | Direct   |
| RIF/USDT(mp1%) | RIF/USDT   | mp1%      | Direct   |
| USDT/USD       | USDT/USD   |           | Weighted |

| Method   | Description                                              |
|----------|----------------------------------------------------------|
| Computed | Compute made with previously obtained coinpairs          |
| Direct   | Direct value from a single source                        |
| Weighted | Weighted median of values obtained from multiple sources |

| Name           | Comment/Description                                                    |
|----------------|------------------------------------------------------------------------|
| BTC/USD        |                                                                        |
| BTC/USDT       |                                                                        |
| RIF/BTC        |                                                                        |
| RIF/USD        | Leave this as legacy                                                   |
| RIF/USD(B)     | Passing through Bitcoin                                                |
| RIF/USD(T)     | Passing through Tether                                                 |
| RIF/USD(TB)    | Passing through Tether & Bitcoin                                       |
| RIF/USD(TBMA)  | Passing through Tether & Bitcoin, using [DWAP](fundamentals/dwap.md)   |
| RIF/USD(TMA)   | Passing through Tether, using [DWAP](fundamentals/dwap.md), 100k depth |
| RIF/USD(TMA2)  | Passing through Tether, using [DWAP](fundamentals/dwap.md), 200k depth |
| RIF/USD(TMA3)  | Passing through Tether, using [DWAP](fundamentals/dwap.md), 600k depth |
| RIF/USD(WMTB)  | Passing through Tether & Bitcoin using weighted median                 |
| RIF/USDT       |                                                                        |
| RIF/USDT(MA)   | Using [DWAP](fundamentals/dwap.md), 100k depth                         |
| RIF/USDT(MA2)  | Using [DWAP](fundamentals/dwap.md), 200k depth                         |
| RIF/USDT(MA3)  | Using [DWAP](fundamentals/dwap.md), 600k depth                         |
| RIF/USDT(mp1%) | To move the price 1 percent                                            |
| USDT/USD       |                                                                        |


## Formulas used in the computed coinpairs

```
RIF/USD        =  rif_btc × btc_usd
RIF/USD(B)     =  rif_btc × btc_usd
RIF/USD(T)     =  rif_usdt × usdt_usd
RIF/USD(TB)    =  rif_usdt × btc_usd / btc_usdt
RIF/USD(TBMA)  =  rif_usdt_ma × btc_usd / btc_usdt
RIF/USD(TMA)   =  rif_usdt_ma × usdt_usd
RIF/USD(TMA2)  =  rif_usdt_ma2 × usdt_usd
RIF/USD(TMA3)  =  rif_usdt_ma3 × usdt_usd
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
  -v, --verbose                   Verbose mode.
  --version                       Show version and exit.
  -j, --json                      Show data in JSON format and exit.
  -w, --weighing                  Show the default weighing and exit.
  -c, --computed                  Show the computed pairs formula and exit.
  -e, --show-envs                 Show used ENV variables used and exit.
  -s, --summary                   Show the summary and exit.
  -m, --markdown                  Set markdown for the summary format.
  -n, --not-ignore-zero-weighing  Not ignore sources with zero weighing.
  -h, --help                      Show this message and exit.

user@workstation:~$ moc_prices_source_check "RIF/USD*"

Coinpair    V.    Short description     Exchnage    Response        Weight    %  Time
----------  ----  --------------------  ----------  ------------  --------  ---  ------
BTC/USD           Bitcoin to Dollar     Bitfinex    $  66.80000K      0.18   18  384ms
BTC/USD           Bitcoin to Dollar     Bitstamp    $  66.67400K      0.22   22  311ms
BTC/USD           Bitcoin to Dollar     Coinbase    $  66.68054K      0.25   25  1.03s
BTC/USD           Bitcoin to Dollar     Gemini      $  66.66932K      0.17   17  1.02s
BTC/USD           Bitcoin to Dollar     Kraken      $  66.68000K      0.18   18  656ms
BTC/USDT          Bitcoin to Tether     Binance     ₮  66.70712K      0.65   65  690ms
BTC/USDT          Bitcoin to Tether     Bybit       ₮  66.71285K      0.1    10  661ms
BTC/USDT          Bitcoin to Tether     Huobi       ₮  66.69838K      0.05    5  629ms
BTC/USDT          Bitcoin to Tether     KuCoin      ₮  66.71045K      0.05    5  791ms
BTC/USDT          Bitcoin to Tether     OKX         ₮  66.71575K      0.15   15  1.01s
RIF/BTC           RIF to Bitcoin        Binance     ₿ 380.00000p      1     100  690ms
RIF/USDT    MA    RIF to Tether         Binance     ₮  33.23568m      1     100  699ms
RIF/USDT    MA2   RIF to Tether         Binance     ₮  33.23451m      1     100  664ms
RIF/USDT    MA3   RIF to Tether         Binance     ₮  33.26227m      1     100  656ms
RIF/USDT    mp1%  To move the price 1%  Binance     ₮  40.51633K      1     100  610ms
RIF/USDT          RIF to Tether         Binance     ₮  33.20000m      1     100  682ms
USDT/USD          Tether to Dollar      Bitstamp    $ 999.63000m      0.15   15  671ms
USDT/USD          Tether to Dollar      Coinbase    $ 999.64000m      0.35   35  819ms
USDT/USD          Tether to Dollar      Gemini      $ 999.49500m      0.15   15  1.01s
USDT/USD          Tether to Dollar      Kraken      $ 999.68500m      0.35   35  650ms

    Coinpair                Value   Sources count    Ok   Time
--  --------------  -------------  ---------------  ----  ------
⇓   BTC/USD         66,680.000000      5 of 5        ✓    1.03s
⇓   BTC/USDT        66,707.125000      5 of 5        ✓    1.01s
↓   RIF/BTC          3.800 × 10⁻⁷      1 of 1        ✓    690ms
ƒ   RIF/USD              0.025338        N/A         ✓    <10ms
ƒ   RIF/USD(B)           0.025338        N/A         ✓    <10ms
ƒ   RIF/USD(T)           0.033187        N/A         ✓    <10ms
ƒ   RIF/USD(TB)          0.033186        N/A         ✓    <10ms
ƒ   RIF/USD(TBMA)        0.033222        N/A         ✓    <10ms
ƒ   RIF/USD(TMA)         0.033222        N/A         ✓    <10ms
ƒ   RIF/USD(TMA2)        0.033221        N/A         ✓    <10ms
ƒ   RIF/USD(TMA3)        0.033249        N/A         ✓    <10ms
ƒ   RIF/USD(WMTB)        0.031224        N/A         ✓    <10ms
↓   RIF/USDT             0.033200      1 of 1        ✓    682ms
↓   RIF/USDT(MA)         0.033236      1 of 1        ✓    699ms
↓   RIF/USDT(MA2)        0.033235      1 of 1        ✓    664ms
↓   RIF/USDT(MA3)        0.033262      1 of 1        ✓    656ms
↓   RIF/USDT(mp1%)  40,516.325400      1 of 1        ✓    610ms
⇓   USDT/USD             0.999596      4 of 4        ✓    1.01s

Response time 1.28s

user@workstation:~$
```

