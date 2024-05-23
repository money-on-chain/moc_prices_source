# **Options for the `RIF/USD` price source**

Date: **2024-05-23**




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

| Name           | Coinpair   | Variant   | Method   |
|----------------|------------|-----------|----------|
| BTC/USD        | BTC/USD    |           | Weighted |
| BTC/USDT       | BTC/USDT   |           | Weighted |
| RIF/BTC        | RIF/BTC    |           | Weighted |
| RIF/USD        | RIF/USD    |           | Computed |
| RIF/USD(B)     | RIF/USD    | B         | Computed |
| RIF/USD(T)     | RIF/USD    | T         | Computed |
| RIF/USD(TB)    | RIF/USD    | TB        | Computed |
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

| Name           | Comment/Description                                     |
|----------------|---------------------------------------------------------|
| BTC/USD        |                                                         |
| BTC/USDT       |                                                         |
| RIF/BTC        |                                                         |
| RIF/USD        | Leave this as legacy                                    |
| RIF/USD(B)     | Passing through Bitcoin                                 |
| RIF/USD(T)     | Passing through Tether                                  |
| RIF/USD(TB)    | Passing through Tether & Bitcoin                        |
| RIF/USD(WMTB)  | Passing through Tether & Bitcoin usinng weighted_median |
| RIF/USDT       |                                                         |
| RIF/USDT(MA)   | Using the magic average algorithm with orderbook depth  |
| RIF/USDT(MA2)  |                                                         |
| RIF/USDT(MA3)  |                                                         |
| RIF/USDT(mp1%) | To move the price 1 percent                             |
| USDT/USD       |                                                         |


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
Bitcoin    Dollar         Bitfinex    $  67.14200K      0.18   18  1.17s
Bitcoin    Dollar         Bitstamp    $  67.03900K      0.22   22  2.29s
Bitcoin    Dollar         Coinbase    $  67.02841K      0.25   25  0.96s
Bitcoin    Dollar         Gemini      $  67.02645K      0.17   17  1.56s
Bitcoin    Dollar         Kraken      $  67.01880K      0.18   18  1.97s
Bitcoin    Tether         Binance     ₮  67.09889K      0.8    80  1.83s
Bitcoin    Tether         Bitfinex    ₮  67.08600K      0.05    5  1.17s
Bitcoin    Tether         Coinbase    ₮  67.08416K      0.1    10  0.96s
Bitcoin    Tether         Kraken      ₮  67.10070K      0.05    5  1.17s
RIF Token  Bitcoin        Binance     ₿   2.28000µ      1     100  1.84s
RIF Token  Tether   MA    Binance     ₮ 152.52785m      1     100  1.82s
RIF Token  Tether   MA2   Binance     ₮ 152.52229m      1     100  1.85s
RIF Token  Tether   MA3   Binance     ₮ 152.41438m      1     100  1.85s
RIF Token  Tether   mp1%  Binance     ₮  53.38290K      1     100  3.0s
RIF Token  Tether         Binance     ₮ 152.40000m      1     100  1.82s
Tether     Dollar         Bitstamp    $ 999.18000m      0.15   15  1.83s
Tether     Dollar         Coinbase    $ 999.17500m      0.45   45  1.19s
Tether     Dollar         Kraken      $ 999.12000m      0.4    40  1.38s

    Coin pair             Mediam          Mean    Weighted median  Sources    Ok
--  --------------  ------------  ------------  -----------------  ---------  ----
↓   BTC/USD         67028.4       67050.9            67028.4       5 of 5     ✓
↓   BTC/USDT        67092.4       67092.4            67099         4 of 4     ✓
↓   RIF/BTC             2.28e-06      2.28e-06           2.28e-06  1 of 1     ✓
ƒ   RIF/USD             0.152825      0.152876           0.152825  N/A        ✓
ƒ   RIF/USD(B)          0.152825      0.152876           0.152825  N/A        ✓
ƒ   RIF/USD(T)          0.152274      0.152272           0.152274  N/A        ✓
ƒ   RIF/USD(TB)         0.152255      0.152306           0.15224   N/A        ✓
ƒ   RIF/USD(WMTB)       0.152397      0.152448           0.152386  N/A        ✓
↓   RIF/USDT            0.1524        0.1524             0.1524    1 of 1     ✓
↓   RIF/USDT(MA)        0.152528      0.152528           0.152528  1 of 1     ✓
↓   RIF/USDT(MA2)       0.152522      0.152522           0.152522  1 of 1     ✓
↓   RIF/USDT(MA3)       0.152414      0.152414           0.152414  1 of 1     ✓
↓   RIF/USDT(mp1%)  53382.9       53382.9            53382.9       1 of 1     ✓
↓   USDT/USD            0.999175      0.999158           0.999175  3 of 3     ✓

Response time 4.39s

user@workstation:~$
```

