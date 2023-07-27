# **Options for the `RIF/USD` price source**

Date: **2023-07-27**




## Options

Currently there are **4** options:

* RIF/USD(B)
* RIF/USD(TB)
* RIF/USD(WMTB)
* RIF/USD(T)

## Rationale behind the chosen nomenclature

`RIF/USD(B)`: Because it goes through *RIF/**B**itcoin* and ***B**itcoin/Dollar* to reach the desired pair.

`RIF/USD(TB)`: Because it goes through *RIF/**T**ether*, ***B**itcoin/Dollar* and *Bitcoin/**T**ether* to get to the desired pair.

`RIF/USD(T)`: Because it goes through *RIF/**T**ether* and ***T**ether/Dollar* to reach the desired pair.

`RIF/USD(WMTB)`: Because uses a **W**eighted **M**edian between `RIF/USD(B)` and `RIF/USD(TB)` to reach the desired pair.


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
| RIF/USD(B)    | RIF/USD    | B         | Computed |
| RIF/USD(T)    | RIF/USD    | T         | Computed |
| RIF/USD(TB)   | RIF/USD    | TB        | Computed |
| RIF/USD(WMTB) | RIF/USD    | WMTB      | Computed |
| RIF/USDT      | RIF/USDT   |           | Weighted |
| USDT/USD      | USDT/USD   |           | Weighted |

| Method   | Description                                              |
|----------|----------------------------------------------------------|
| Weighted | Weighted median of values ​​obtained from multiple sources |
| Computed | Compute made with previously obtained coinpairs          |


## Formulas used in the computed coinpairs

```
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
sources and if necessary we apply the changes to the parameterization


### For coinpair BTC/USD (from Bitcoin to Dollar)

| Source   |   Weigh | URI                                                  |
|----------|---------|------------------------------------------------------|
| Bitstamp |    0.22 | https://www.bitstamp.net/api/v2/ticker/btcusd/       |
| Bitfinex |    0.18 | https://api-pub.bitfinex.com/v2/ticker/tBTCUSD       |
| Kraken   |    0.18 | https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD |
| Coinbase |    0.25 | https://api.coinbase.com/v2/prices/spot?currency=USD |
| Gemini   |    0.17 | https://api.gemini.com/v1/pubticker/BTCUSD           |


### For coinpair RIF/BTC (from RIF Token to Bitcoin)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFBTC)


### For coinpair RIF/USDT (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFUSDT)


### For coinpair BTC/USDT (from Bitcoin to Tether)

| Source   |   Weigh | URI                                                       |
|----------|---------|-----------------------------------------------------------|
| Binance  |    0.80 | https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT |
| Bitfinex |    0.05 | https://api-pub.bitfinex.com/v2/ticker/tBTCUST            |
| Kraken   |    0.05 | https://api.kraken.com/0/public/Ticker?pair=XBTUSDT       |
| Coinbase |    0.10 | https://api.coinbase.com/v2/exchange-rates?currency=BTC   |


### For coinpair USDT/USD (from Tether to Dollar)

| Source   |   Weigh | URI                                                      |
|----------|---------|----------------------------------------------------------|
| Bitstamp |    0.15 | https://www.bitstamp.net/api/v2/ticker/usdtusd/          |
| Coinbase |    0.45 | https://api.coinbase.com/v2/exchange-rates?currency=USDT |
| Kraken   |    0.40 | https://api.kraken.com/0/public/Ticker?pair=USDTZUSD     |

## The `moc_prices_source_check` tool

There is a tool that comes with the [`moc_prices_source` package](https://github.com/money-on-chain/moc_prices_source) that allows us to run a simulation that queries and calculates all the coinpairs.
This tool is called `moc_prices_source_check` and here you can see an example of its use.

### Example

```
user@workstation:~$ moc_prices_source_check "RIF/USD*"

From       To       V.    Exchnage        Response        Weigh  %      Time
---------  -------  ----  --------------  ------------  -------  -----  ------
Bitcoin    Dollar         Bitfinex        $  29.39700K     0.18  18.0   1.0s
Bitcoin    Dollar         Bitstamp        $  29.35700K     0.22  22.0   1.01s
Bitcoin    Dollar         Coinbase        $  29.35588K     0.25  25.0   0.96s
Bitcoin    Dollar         Gemini          $  29.35139K     0.17  17.0   1.37s
Bitcoin    Dollar         Kraken          $  29.34200K     0.18  18.0   1.37s
Bitcoin    Tether         Binance         ₮  29.36504K     0.8   80.0   1.77s
Bitcoin    Tether         Bitfinex        ₮  29.36200K     0.05  5.0    1.57s
Bitcoin    Tether         Coinbase        ₮  29.35759K     0.1   10.0   0.95s
Bitcoin    Tether         Kraken          ₮  29.34340K     0.05  5.0    1.37s
RIF Token  Bitcoin        Binance         ₿   2.68000µ     1     100.0  1.17s
RIF Token  Bitcoin        BitHumb         ₿   6.30000µ     0     N/A    2.59s
RIF Token  Bitcoin        Coingecko       ₿   2.68000µ     0     N/A    0.95s
RIF Token  Bitcoin        MEXC            ₿   2.68700µ     0     N/A    1.14s
RIF Token  Bitcoin        Sovryn onchain  ₿   2.70030µ     0     N/A    1.59s
RIF Token  Tether         Binance         ₮  78.60000m     1     100.0  1.15s
Tether     Dollar         Bitstamp        $ 999.87000m     0.15  15.0   1.16s
Tether     Dollar         Coinbase        $ 999.83500m     0.45  45.0   0.97s
Tether     Dollar         Kraken          $ 999.68000m     0.4   40.0   1.38s

    Coin pair             Mediam             Mean    Weighted median  Sources
--  -------------  -------------  ---------------  -----------------  ---------
↓   BTC/USD        29355.9        29360.7              29355.9        5
↓   BTC/USDT       29359.8        29357                29363.8        4
↓   RIF/BTC            2.687e-06      3.40946e-06          2.68e-06   5
ƒ   RIF/USD            0.0788792      0.100104             0.0786737  N/A
ƒ   RIF/USD(B)         0.0788792      0.100104             0.0786737  N/A
ƒ   RIF/USD(T)         0.078587       0.0785839            0.078587   N/A
ƒ   RIF/USD(TB)        0.0785895      0.0786098            0.0785789  N/A
ƒ   RIF/USD(WMTB)      0.0786619      0.0839833            0.0786026  N/A
↓   RIF/USDT           0.0786         0.0786               0.0786     1
↓   USDT/USD           0.999835       0.999795             0.999835   3

Response time 2.62s

user@workstation:~$
```

