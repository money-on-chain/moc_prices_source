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
Bitcoin    Dollar         Bitfinex        $  29.40600K     0.18  18.0   0.49s
Bitcoin    Dollar         Bitstamp        $  29.36500K     0.22  22.0   0.45s
Bitcoin    Dollar         Coinbase        $  29.36514K     0.25  25.0   0.28s
Bitcoin    Dollar         Gemini          $  29.36707K     0.17  17.0   0.97s
Bitcoin    Dollar         Kraken          $  29.34280K     0.18  18.0   0.68s
Bitcoin    Tether         Binance         ₮  29.36649K     0.8   80.0   1.03s
Bitcoin    Tether         Bitfinex        ₮  29.36600K     0.05  5.0    0.52s
Bitcoin    Tether         Coinbase        ₮  29.35978K     0.1   10.0   0.27s
Bitcoin    Tether         Kraken          ₮  29.36670K     0.05  5.0    0.72s
RIF Token  Bitcoin        Binance         ₿   2.68000µ     1     100.0  0.47s
RIF Token  Bitcoin        BitHumb         ₿   6.30000µ     0     N/A    3.26s
RIF Token  Bitcoin        Coingecko       ₿   2.68000µ     0     N/A    0.41s
RIF Token  Bitcoin        MEXC            ₿   2.67500µ     0     N/A    0.61s
RIF Token  Bitcoin        Sovryn onchain  ₿   2.70030µ     0     N/A    1.2s
RIF Token  Tether         Binance         ₮  78.50000m     1     100.0  0.47s
Tether     Dollar         Bitstamp        $ 999.89000m     0.15  15.0   0.47s
Tether     Dollar         Coinbase        $ 999.87500m     0.45  45.0   0.31s
Tether     Dollar         Kraken          $ 999.64000m     0.4   40.0   0.69s

    Coin pair             Mediam             Mean    Weighted median  Sources
--  -------------  -------------  ---------------  -----------------  ---------
↓   BTC/USD        29365.1        29369.2              29365.1        5
↓   BTC/USDT       29366.2        29364.7              29366.5        4
↓   RIF/BTC            2.68e-06       3.40706e-06          2.68e-06   5
ƒ   RIF/USD            0.0786986      0.100063             0.0786986  N/A
ƒ   RIF/USD(B)         0.0786986      0.100063             0.0786986  N/A
ƒ   RIF/USD(T)         0.0784902      0.0784844            0.0784902  N/A
ƒ   RIF/USD(TB)        0.078497       0.0785119            0.0784964  N/A
ƒ   RIF/USD(WMTB)      0.0785474      0.0838996            0.0785469  N/A
↓   RIF/USDT           0.0785         0.0785               0.0785     1
↓   USDT/USD           0.999875       0.999802             0.999875   3

Response time 3.29s

user@workstation:~$
```

