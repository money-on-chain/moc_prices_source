# **MoC prices source**

This is the python package used in [**Money on Chain**](https://moneyonchain.com/) projects where it is required to get the coinpair values directly from the sources.
This package includes a CLI tool that allows you to query the coinpair values in the same way that [**Money on Chain**](https://moneyonchain.com/) projects do.


# Supported coinpairs and symbols


## Symbols

| Symbol   | Name         | Char   |
|----------|--------------|--------|
| BNB      | Binance Coin | Ƀ      |
| BTC      | Bitcoin      | ₿      |
| ETH      | Ether        | ⟠      |
| MOC      | MOC Token    |        |
| RIF      | RIF Token    |        |
| USD      | Dollar       | $      |
| USDT     | Tether       | ₮      |


## Coinpairs

| Name          | Coinpair   | Variant   | Method   |
|---------------|------------|-----------|----------|
| BNB/USD       | BNB/USD    |           | Computed |
| BNB/USDT      | BNB/USDT   |           | Weighted |
| BTC/USD       | BTC/USD    |           | Weighted |
| BTC/USDT      | BTC/USDT   |           | Weighted |
| ETH/BTC       | ETH/BTC    |           | Weighted |
| ETH/USD       | ETH/USD    |           | Computed |
| MOC/BTC       | MOC/BTC    |           | Weighted |
| MOC/USD       | MOC/USD    |           | Computed |
| RIF/BTC       | RIF/BTC    |           | Weighted |
| RIF/USD       | RIF/USD    |           | Computed |
| RIF/USD(B)    | RIF/USD    | B         | Computed |
| RIF/USD(T)    | RIF/USD    | T         | Computed |
| RIF/USD(TB)   | RIF/USD    | TB        | Computed |
| RIF/USD(WMTB) | RIF/USD    | WMTB      | Computed |
| RIF/USDT      | RIF/USDT   |           | Weighted |
| USDT/USD      | USDT/USD   |           | Weighted |
| USDT/USD(B)   | USDT/USD   | B         | Computed |

| Method   | Description                                              |
|----------|----------------------------------------------------------|
| Weighted | Weighted median of values ​​obtained from multiple sources |
| Computed | Compute made with previously obtained coinpairs          |


## Formulas used in the computed coinpairs

```
BNB/USD        =  bnb_usdt * btc_usd / btc_usdt
ETH/USD        =  eth_btc * btc_usd
MOC/USD        =  moc_btc * btc_usd
RIF/USD        =  rif_btc * btc_usd
RIF/USD(B)     =  rif_btc * btc_usd
RIF/USD(T)     =  rif_usdt * usdt_usd
RIF/USD(TB)    =  rif_usdt * btc_usd / btc_usdt
RIF/USD(WMTB)  =  weighted_median(
                  [(rif_usdt * btc_usd / btc_usdt), (rif_btc * btc_usd)],
                  [0.75, 0.25])
USDT/USD(B)    =  btc_usd / btc_usdt
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


### For coinpair ETH/BTC (from Ether to Bitcoin)

| Source   |   Weight | URI                                                      |
|----------|----------|----------------------------------------------------------|
| Bitstamp |     0.25 | https://www.bitstamp.net/api/v2/ticker/ethbtc/           |
| Bitfinex |     0.25 | https://api-pub.bitfinex.com/v2/ticker/tETHBTC           |
| Kraken   |     0.25 | https://api.kraken.com/0/public/Ticker?pair=ETHBTC       |
| Binance  |     0.25 | https://api.binance.com/api/v3/ticker/24hr?symbol=ETHBTC |


### For coinpair BTC/USDT (from Bitcoin to Tether)

| Source   |   Weight | URI                                                       |
|----------|----------|-----------------------------------------------------------|
| Binance  |     0.80 | https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT |
| Bitfinex |     0.05 | https://api-pub.bitfinex.com/v2/ticker/tBTCUST            |
| Kraken   |     0.05 | https://api.kraken.com/0/public/Ticker?pair=XBTUSDT       |
| Coinbase |     0.10 | https://api.coinbase.com/v2/exchange-rates?currency=BTC   |


### For coinpair BNB/USDT (from Binance Coin to Tether)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=BNBUSDT)


### For coinpair MOC/BTC (from MOC Token to Bitcoin)

Only Sovryn onchain (URI: https://public-node.rsk.co)


### For coinpair USDT/USD (from Tether to Dollar)

| Source   |   Weight | URI                                                      |
|----------|----------|----------------------------------------------------------|
| Bitstamp |     0.15 | https://www.bitstamp.net/api/v2/ticker/usdtusd/          |
| Coinbase |     0.45 | https://api.coinbase.com/v2/exchange-rates?currency=USDT |
| Kraken   |     0.40 | https://api.kraken.com/0/public/Ticker?pair=USDTZUSD     |

