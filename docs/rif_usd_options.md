# **Options for the `RIF/USD` price source**

Date: **2025-09-17**




## Options

Currently there are **7** options:

* RIF/USD(B)
* RIF/USD(TB)
* RIF/USD(WMTB)
* RIF/USD(T)
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

| Name           | Comment/Description                                                            |
|----------------|--------------------------------------------------------------------------------|
| BTC/USD        |                                                                                |
| BTC/USDT       |                                                                                |
| RIF/BTC        |                                                                                |
| RIF/USD        | Leave this as legacy                                                           |
| RIF/USD(B)     | Passing through Bitcoin                                                        |
| RIF/USD(T)     | Passing through Tether                                                         |
| RIF/USD(TB)    | Passing through Tether & Bitcoin                                               |
| RIF/USD(TMA)   | Passing through Tether, using the magic average algorithm with orderbook depth |
| RIF/USD(WMTB)  | Passing through Tether & Bitcoin usinng weighted_median                        |
| RIF/USDT       |                                                                                |
| RIF/USDT(MA)   | Using the magic average algorithm with orderbook depth                         |
| RIF/USDT(MA2)  |                                                                                |
| RIF/USDT(MA3)  |                                                                                |
| RIF/USDT(mp1%) | To move the price 1 percent                                                    |
| USDT/USD       |                                                                                |


## Formulas used in the computed coinpairs

```
RIF/USD        =  rif_btc * btc_usd
RIF/USD(B)     =  rif_btc * btc_usd
RIF/USD(T)     =  rif_usdt * usdt_usd
RIF/USD(TB)    =  rif_usdt * btc_usd / btc_usdt
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
Bitcoin    Dollar         Bitfinex    $ 115.35000K      0.18   18  0.21s
Bitcoin    Dollar         Bitstamp    $ 115.17100K      0.22   22  0.81s
Bitcoin    Dollar         Coinbase    $ 115.29685K      0.25   25  0.29s
Bitcoin    Dollar         Gemini      $ 115.15000K      0.17   17  1.1s
Bitcoin    Dollar         Kraken      $ 115.22500K      0.18   18  0.3s
Bitcoin    Tether         Binance     ₮ 115.12001K      0.8    80  0.41s
Bitcoin    Tether         Bitfinex    ₮ 115.27000K      0.05    5  0.22s
Bitcoin    Tether         Coinbase    ₮ 115.33606K      0.1    10  0.59s
Bitcoin    Tether         Kraken      ₮ 115.27170K      0.05    5  0.25s
RIF Token  Bitcoin        Binance     ₿ 520.00000p      1     100  0.44s
RIF Token  Tether   MA    Binance     ₮  60.04995m      1     100  0.43s
RIF Token  Tether   MA2   Binance     ₮  60.08309m      1     100  0.46s
RIF Token  Tether   MA3   Binance     ₮  60.10730m      1     100  0.43s
RIF Token  Tether   mp1%  Binance     ₮  23.11523K      1     100  0.38s
RIF Token  Tether         Binance     ₮  60.00000m      1     100  0.42s
Tether     Dollar         Bitstamp    $   1.00035       0.15   15  0.84s
Tether     Dollar         Coinbase    $   1.00032       0.45   45  0.62s
Tether     Dollar         Kraken      $   1.00026       0.4    40  0.4s

    Coin pair               Mediam            Mean    Weighted median   Sources    Ok
--  --------------  --------------  --------------  -----------------  ---------  ----
↓   BTC/USD         115,225.000000  115,238.570000     115,225.000000   5 of 5     ✓
↓   BTC/USDT        115,270.850000  115,249.443750     115,128.932941   4 of 4     ✓
↓   RIF/BTC               0.000001        0.000001           0.000001   1 of 1     ✓
ƒ   RIF/USD               0.059917        0.059924           0.059917     N/A      ✓
ƒ   RIF/USD(B)            0.059917        0.059924           0.059917     N/A      ✓
ƒ   RIF/USD(T)            0.060020        0.060019           0.060020     N/A      ✓
ƒ   RIF/USD(TB)           0.059976        0.059994           0.060050     N/A      ✓
ƒ   RIF/USD(TMA)          0.060069        0.060069           0.060069     N/A      ✓
ƒ   RIF/USD(WMTB)         0.059961        0.059977           0.060017     N/A      ✓
↓   RIF/USDT              0.060000        0.060000           0.060000   1 of 1     ✓
↓   RIF/USDT(MA)          0.060050        0.060050           0.060050   1 of 1     ✓
↓   RIF/USDT(MA2)         0.060083        0.060083           0.060083   1 of 1     ✓
↓   RIF/USDT(MA3)         0.060107        0.060107           0.060107   1 of 1     ✓
↓   RIF/USDT(mp1%)   23,115.234300   23,115.234300      23,115.234300   1 of 1     ✓
↓   USDT/USD              1.000325        1.000312           1.000325   3 of 3     ✓

Response time 1.13s

user@workstation:~$
```

