# **MoC prices source**

This is the python package used in [**Money on Chain**](https://moneyonchain.com/) projects where it is required to get the coinpair values directly from the sources.
This package includes a CLI tool that allows you to query the coinpair values in the same way that [**Money on Chain**](https://moneyonchain.com/) projects do.


# Supported coinpairs and symbols


## Symbols

| Symbol   | Name            | Char   |
|----------|-----------------|--------|
| ARS      | Peso Argentino  | $      |
| BNB      | Binance Coin    | Ƀ      |
| BTC      | Bitcoin         | ₿      |
| COP      | Peso Colombiano | $      |
| ETH      | Ether           | ⟠      |
| GAS      | Gas             |        |
| MOC      | MOC Token       |        |
| MXN      | Peso Mexicano   | $      |
| RIF      | RIF Token       |        |
| USD      | Dollar          | $      |
| USDT     | Tether          | ₮      |


## Coinpairs

| Name           | Coinpair   | Variant   | Method   |
|----------------|------------|-----------|----------|
| BNB/USD        | BNB/USD    |           | Computed |
| BNB/USDT       | BNB/USDT   |           | Weighted |
| BTC/ARS        | BTC/ARS    |           | Weighted |
| BTC/COP        | BTC/COP    |           | Weighted |
| BTC/USD        | BTC/USD    |           | Weighted |
| BTC/USDT       | BTC/USDT   |           | Weighted |
| ETH/BTC        | ETH/BTC    |           | Weighted |
| ETH/USD        | ETH/USD    |           | Computed |
| GAS/BTC        | GAS/BTC    |           | Weighted |
| MOC/BTC        | MOC/BTC    |           | Weighted |
| MOC/USD        | MOC/USD    |           | Computed |
| RIF/BTC        | RIF/BTC    |           | Weighted |
| RIF/BTC(mp1%)  | RIF/BTC    | mp1%      | Weighted |
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
| USD/ARS        | USD/ARS    |           | Weighted |
| USD/ARS(CCB)   | USD/ARS    | CCB       | Computed |
| USD/ARS(CCL)   | USD/ARS    | CCL       | Weighted |
| USD/COP        | USD/COP    |           | Weighted |
| USD/COP(CCB)   | USD/COP    | CCB       | Computed |
| USD/MXN        | USD/MXN    |           | Weighted |
| USDT/USD       | USDT/USD   |           | Weighted |
| USDT/USD(B)    | USDT/USD   | B         | Computed |

| Method   | Description                                              |
|----------|----------------------------------------------------------|
| Weighted | Weighted median of values ​​obtained from multiple sources |
| Computed | Compute made with previously obtained coinpairs          |

| Name           | Comment/Description                                     |
|----------------|---------------------------------------------------------|
| BNB/USD        |                                                         |
| BNB/USDT       |                                                         |
| BTC/ARS        |                                                         |
| BTC/COP        |                                                         |
| BTC/USD        |                                                         |
| BTC/USDT       |                                                         |
| ETH/BTC        |                                                         |
| ETH/USD        |                                                         |
| GAS/BTC        |                                                         |
| MOC/BTC        |                                                         |
| MOC/USD        |                                                         |
| RIF/BTC        |                                                         |
| RIF/BTC(mp1%)  | To move the price 1 percent                             |
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
| USD/ARS        |                                                         |
| USD/ARS(CCB)   |                                                         |
| USD/ARS(CCL)   |                                                         |
| USD/COP        |                                                         |
| USD/COP(CCB)   |                                                         |
| USD/MXN        |                                                         |
| USDT/USD       |                                                         |
| USDT/USD(B)    | Passing through Bitcoin                                 |


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
USD/ARS(CCB)   =  btc_ars / btc_usd
USD/COP(CCB)   =  btc_cop / btc_usd
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


### For coinpair BTC/ARS (from Bitcoin to Peso Argentino)

| Source        |   Weight | URI                                                                    |
|---------------|----------|------------------------------------------------------------------------|
| ArgenBTC      |     0.14 | https://argenbtc.com/cotizacion                                        |
| belo.app      |     0.14 | https://api.belo.app/public/price                                      |
| Binance       |     0.14 | https://api.binance.com/api/v3/ticker/24hr?symbol=BTCARS               |
| BuenBit       |     0.14 | https://be.buenbit.com/api/market/tickers                              |
| cryptomkt.com |     0.14 | https://api.exchange.cryptomkt.com/api/3/public/ticker/BTCARS          |
| Decrypto      |     0.14 | https://api.decrypto.la/1.0/frontend/trading/data/prices               |
| Lemoncash     |     0.14 | https://api.lemoncash.com.ar/api/v1/exchange-rates-quotations-external |


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


### For coinpair RIF/BTC(mp1%) (from RIF Token to Bitcoin)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFBTC)


### For coinpair RIF/USDT(MA) (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA2) (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA3) (from RIF Token to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


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


### For coinpair USD/ARS(CCL) (from Dollar to Peso Argentino)

| Source           |   Weight | URI                                                                         |
|------------------|----------|-----------------------------------------------------------------------------|
| Ambito.com       |     0.14 | https://mercados.ambito.com//dolarrava/cl/variacion                         |
| CriptoYa.com     |     0.14 | https://criptoya.com/api/dolar                                              |
| LaNacion.com.ar  |     0.14 | https://api-contenidos.lanacion.com.ar/json/V3/economia/cotizacionblue/DCCL |
| DolarHoy.com     |     0.14 | https://dolarhoy.com/cotizaciondolarcontadoconliqui                         |
| Infobae          |     0.14 | https://www.infobae.com/economia/divisas/dolar-hoy/                         |
| InfoDolar.com    |     0.14 | https://www.infodolar.com/cotizacion-dolar-contado-con-liquidacion.aspx     |
| CoinMonitor.info |     0.14 | https://coinmonitor.info/chart_DOLARES_24hs.json                            |


### For coinpair USD/ARS (from Dollar to Peso Argentino)

| Source           |   Weight | URI                                                                          |
|------------------|----------|------------------------------------------------------------------------------|
| Ambito.com       |     0.14 | https://mercados.ambito.com/dolar/informal/variacion                         |
| CriptoYa.com     |     0.14 | https://criptoya.com/api/dolar                                               |
| LaNacion.com.ar  |     0.14 | https://api-contenidos.lanacion.com.ar/json/V3/economia/cotizacionblue/DBLUE |
| DolarHoy.com     |     0.14 | https://dolarhoy.com/cotizaciondolarblue                                     |
| Infobae          |     0.14 | https://www.infobae.com/economia/divisas/dolar-hoy/                          |
| InfoDolar.com    |     0.14 | https://www.infodolar.com/cotizacion-dolar-blue.aspx                         |
| CoinMonitor.info |     0.14 | https://coinmonitor.info/chart_DOLARES_24hs.json                             |


### For coinpair USD/MXN (from Dollar to Peso Mexicano)

| Source                |   Weight | URI                                                                                           |
|-----------------------|----------|-----------------------------------------------------------------------------------------------|
| ElDolar.info          |     0.10 | https://www.eldolar.info/es-MX/mexico/dia/hoy                                                 |
| Intercam.com.mx       |     0.10 | https://intercamprod.finsol.cloud/services/historico/getLast                                  |
| CitiBanamex           |     0.10 | https://finanzasenlinea.infosel.com/banamex/WSFeedJSON/service.asmx/DivisasLast?callback=     |
| Wise.com              |     0.10 | https://wise.com/rates/history+live?source=USD&target=MXN&length=1&resolution=hourly&unit=day |
| X-rates.com           |     0.10 | https://www.x-rates.com/calculator/?from=USD&to=MXN&amount=1                                  |
| TheMoneyConverter.com |     0.10 | https://themoneyconverter.com/USD/MXN                                                         |
| Currency.me.uk        |     0.10 | https://www.currency.me.uk/convert/usd/mxn                                                    |
| InfoDolar.com.mx      |     0.10 | https://www.infodolar.com.mx                                                                  |
| ElEconomista.es       |     0.10 | https://www.eleconomista.es/cruce/USDMXN                                                      |
| Bitso.com             |     0.10 | https://api.bitso.com/v3/ticker/?book=usd_mxn                                                 |


### For coinpair MOC/BTC (from MOC Token to Bitcoin)

Only Sovryn onchain (URI: https://public-node.rsk.co)


### For coinpair GAS/BTC (from Gas to Bitcoin)

Only RSK onchain (URI: https://public-node.rsk.co)


### For coinpair USDT/USD (from Tether to Dollar)

| Source   |   Weight | URI                                                      |
|----------|----------|----------------------------------------------------------|
| Bitstamp |     0.15 | https://www.bitstamp.net/api/v2/ticker/usdtusd/          |
| Coinbase |     0.45 | https://api.coinbase.com/v2/exchange-rates?currency=USDT |
| Kraken   |     0.40 | https://api.kraken.com/0/public/Ticker?pair=USDTZUSD     |


### For coinpair USD/COP (from Dollar to Peso Colombiano)

| Source      |   Weight | URI                                                                                                     |
|-------------|----------|---------------------------------------------------------------------------------------------------------|
| BanRep      |     0.50 | https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario |
| DolarHoy.co |     0.50 | https://www.dolarhoy.co                                                                                 |


### For coinpair BTC/COP (from Bitcoin to Peso Colombiano)

| Source        |   Weight | URI                                                           |
|---------------|----------|---------------------------------------------------------------|
| bitso.com     |     0.20 | https://api.bitso.com/v3/ticker/?book=btc_cop                 |
| BuenBit       |     0.20 | https://be.buenbit.com/api/market/tickers                     |
| cryptomkt.com |     0.20 | https://api.exchange.cryptomkt.com/api/3/public/ticker/BTCCOP |
| Coinbase      |     0.20 | https://api.coinbase.com/v2/prices/BTC-COP/spot               |
| buda.com      |     0.20 | https://www.buda.com/api/v2/markets/BTC-COP/ticker            |

