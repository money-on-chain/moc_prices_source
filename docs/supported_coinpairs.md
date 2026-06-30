# **MoC prices source**

This is the python package used in [**Money on Chain**](https://moneyonchain.com/) projects where it is required to get the coinpair values directly from the sources.
This package includes a CLI tool that allows you to query the coinpair values in the same way that [**Money on Chain**](https://moneyonchain.com/) projects do.


# Supported coinpairs and symbols


## Symbols

| Symbol   | Name        | Char   |
|----------|-------------|--------|
| ARS      | Peso Arg.   | $      |
| BNB      | BinanceCoin | Ƀ      |
| BPRO     | BPro        |        |
| BTC      | Bitcoin     | ₿      |
| COP      | Peso Col.   | $      |
| DOC      | DOC         |        |
| ETH      | Ether       | ⟠      |
| GAS      | Gas         |        |
| MOC      | MOC         |        |
| MXN      | Peso Mex.   | $      |
| RIF      | RIF         |        |
| USD      | Dollar      | $      |
| USDT     | Tether      | ₮      |


## Coinpairs

| Name              | Coinpair     | Variant   | Method   |
|-------------------|--------------|-----------|----------|
| ARS/BPRO          | ARS/BPRO     |           | Inverted |
| ARS/BTC           | ARS/BTC      |           | Inverted |
| ARS/USD(CCB)      | ARS/USD      | CCB       | Inverted |
| BLOCK(RSK)        | BLOCK        | RSK       | Onchain  |
| BNB/USD           | BNB/USD      |           | Computed |
| BNB/USDT          | BNB/USDT     |           | Direct   |
| BPRO/ARS          | BPRO/ARS     |           | Computed |
| BPRO/BTC          | BPRO/BTC     |           | Onchain  |
| BPRO/COP          | BPRO/COP     |           | Computed |
| BPRO/MOC          | BPRO/MOC     |           | Inverted |
| BPRO/USD          | BPRO/USD     |           | Computed |
| BTC/ARS           | BTC/ARS      |           | Weighted |
| BTC/BPRO          | BTC/BPRO     |           | Inverted |
| BTC/COP           | BTC/COP      |           | Weighted |
| BTC/MOC           | BTC/MOC      |           | Inverted |
| BTC/USD           | BTC/USD      |           | Weighted |
| BTC/USD(24h)      | BTC/USD(24h) |           | Computed |
| BTC/USD(och)      | BTC/USD      | och       | Onchain  |
| BTC/USDT          | BTC/USDT     |           | Weighted |
| COP/BPRO          | COP/BPRO     |           | Inverted |
| COP/BTC           | COP/BTC      |           | Inverted |
| COP/USD(CCB)      | COP/USD      | CCB       | Inverted |
| DOC/USD           | DOC/USD      |           | Dummy    |
| DOC/USD(tec)      | DOC/USD      | tec       | Onchain  |
| DOC/USD(tec-test) | DOC/USD      | tec-test  | Onchain  |
| ETH/BTC           | ETH/BTC      |           | Weighted |
| ETH/USD           | ETH/USD      |           | Weighted |
| ETH/USD(B)        | ETH/USD      | B         | Computed |
| GAS/BTC           | GAS/BTC      |           | Onchain  |
| ISLIQ_ROC         | ISLIQ_ROC    |           | Computed |
| ISLIQ_ROC(test)   | ISLIQ_ROC    | test      | Computed |
| MOC/BPRO          | MOC/BPRO     |           | Computed |
| MOC/BTC           | MOC/BTC      |           | Computed |
| MOC/BTC(sov)      | MOC/BTC      | sov       | Onchain  |
| MOC/RIF           | MOC/RIF      |           | Inverted |
| MOC/USD           | MOC/USD      |           | Computed |
| MOC/USD(Oku)      | MOC/USD      | Oku       | Onchain  |
| MOC/USD(WM)       | MOC/USD      | WM        | Computed |
| RIF/BTC           | RIF/BTC      |           | Direct   |
| RIF/BTC(mp1%)     | RIF/BTC      | mp1%      | Direct   |
| RIF/MOC           | RIF/MOC      |           | Computed |
| RIF/USD           | RIF/USD      |           | Computed |
| RIF/USD(B)        | RIF/USD      | B         | Computed |
| RIF/USD(T)        | RIF/USD      | T         | Computed |
| RIF/USD(TB)       | RIF/USD      | TB        | Computed |
| RIF/USD(TBMA)     | RIF/USD      | TBMA      | Computed |
| RIF/USD(TBMA2)    | RIF/USD      | TBMA2     | Computed |
| RIF/USD(TBMA3)    | RIF/USD      | TBMA3     | Computed |
| RIF/USD(TMA)      | RIF/USD      | TMA       | Computed |
| RIF/USD(TMA2)     | RIF/USD      | TMA2      | Computed |
| RIF/USD(TMA3)     | RIF/USD      | TMA3      | Computed |
| RIF/USD(WMTB)     | RIF/USD      | WMTB      | Computed |
| RIF/USDT          | RIF/USDT     |           | Direct   |
| RIF/USDT(MA)      | RIF/USDT     | MA        | Direct   |
| RIF/USDT(MA2)     | RIF/USDT     | MA2       | Direct   |
| RIF/USDT(MA3)     | RIF/USDT     | MA3       | Direct   |
| RIF/USDT(mp1%)    | RIF/USDT     | mp1%      | Direct   |
| USD/ARS           | USD/ARS      |           | Weighted |
| USD/ARS(CCB)      | USD/ARS      | CCB       | Computed |
| USD/ARS(CCL)      | USD/ARS      | CCL       | Weighted |
| USD/BPRO          | USD/BPRO     |           | Inverted |
| USD/BTC           | USD/BTC      |           | Inverted |
| USD/COP           | USD/COP      |           | Weighted |
| USD/COP(CCB)      | USD/COP      | CCB       | Computed |
| USD/MOC           | USD/MOC      |           | Inverted |
| USD/MXN           | USD/MXN      |           | Weighted |
| USDT/BTC          | USDT/BTC     |           | Inverted |
| USDT/USD          | USDT/USD     |           | Weighted |
| USDT/USD(B)       | USDT/USD     | B         | Computed |

| Method   | Description                                              |
|----------|----------------------------------------------------------|
| Computed | Compute made with previously obtained coinpairs          |
| Direct   | Direct value from a single source                        |
| Dummy    | Dummy constant value                                     |
| Inverted | Inverted coinpair (x⁻¹)                                  |
| Onchain  | Obtained directly from the blockchain                    |
| Weighted | Weighted median of values obtained from multiple sources |

| Name              | Comment/Description                                                              |
|-------------------|----------------------------------------------------------------------------------|
| ARS/BPRO          | Inverted pair of pair BPRO/ARS                                                   |
| ARS/BTC           | Inverted pair of pair BTC/ARS                                                    |
| ARS/USD(CCB)      | Inverted pair of pair USD/ARS(CCB)                                               |
| BLOCK(RSK)        | Rootstock block number                                                           |
| BNB/USD           |                                                                                  |
| BNB/USDT          |                                                                                  |
| BPRO/ARS          |                                                                                  |
| BPRO/BTC          | Obtained from MOC onchain                                                        |
| BPRO/COP          |                                                                                  |
| BPRO/MOC          | Inverted pair of pair MOC/BPRO                                                   |
| BPRO/USD          | Offchain                                                                         |
| BTC/ARS           |                                                                                  |
| BTC/BPRO          | Inverted pair of pair BPRO/BTC                                                   |
| BTC/COP           |                                                                                  |
| BTC/MOC           | Inverted pair of pair MOC/BTC                                                    |
| BTC/USD           |                                                                                  |
| BTC/USD(24h)      | BTC/USD percentage difference over 24 hours                                      |
| BTC/USD(och)      | Obtained from the blockchain                                                     |
| BTC/USDT          |                                                                                  |
| COP/BPRO          | Inverted pair of pair BPRO/COP                                                   |
| COP/BTC           | Inverted pair of pair BTC/COP                                                    |
| COP/USD(CCB)      | Inverted pair of pair USD/COP(CCB)                                               |
| DOC/USD           | Pegged 1:1 to USD                                                                |
| DOC/USD(tec)      | On chain DOC/USD technical price                                                 |
| DOC/USD(tec-test) | On chain DOC/USD technical price for testnet                                     |
| ETH/BTC           |                                                                                  |
| ETH/USD           |                                                                                  |
| ETH/USD(B)        | Passing through Bitcoin                                                          |
| GAS/BTC           | Rootstock gas price from nodes                                                   |
| ISLIQ_ROC         | If RoC is in liquidation (mainnet)                                               |
| ISLIQ_ROC(test)   | If RoC is in liquidation (testnet)                                               |
| MOC/BPRO          |                                                                                  |
| MOC/BTC           |                                                                                  |
| MOC/BTC(sov)      | Obtained from Sovryn onchain                                                     |
| MOC/RIF           | Inverted pair of pair RIF/MOC                                                    |
| MOC/USD           | Default option, weighted median                                                  |
| MOC/USD(Oku)      | Obtained from Oku onchain                                                        |
| MOC/USD(WM)       | Weighted median                                                                  |
| RIF/BTC           |                                                                                  |
| RIF/BTC(mp1%)     | To move the price 1 percent                                                      |
| RIF/MOC           | Use RIF/USDT(MA) 100k depth, USDT/USD and MOC/USD(Oku)                           |
| RIF/USD           | Leave this as legacy                                                             |
| RIF/USD(B)        | Passing through Bitcoin                                                          |
| RIF/USD(T)        | Passing through Tether                                                           |
| RIF/USD(TB)       | Passing through Tether & Bitcoin                                                 |
| RIF/USD(TBMA)     | Passing through Tether & Bitcoin, using [DWAP](fundamentals/dwap.md), 100k depth |
| RIF/USD(TBMA2)    | Passing through Tether & Bitcoin, using [DWAP](fundamentals/dwap.md), 200k depth |
| RIF/USD(TBMA3)    | Passing through Tether & Bitcoin, using [DWAP](fundamentals/dwap.md), 600k depth |
| RIF/USD(TMA)      | Passing through Tether, using [DWAP](fundamentals/dwap.md), 100k depth           |
| RIF/USD(TMA2)     | Passing through Tether, using [DWAP](fundamentals/dwap.md), 200k depth           |
| RIF/USD(TMA3)     | Passing through Tether, using [DWAP](fundamentals/dwap.md), 600k depth           |
| RIF/USD(WMTB)     | Passing through Tether & Bitcoin using weighted median                           |
| RIF/USDT          |                                                                                  |
| RIF/USDT(MA)      | Using [DWAP](fundamentals/dwap.md), 100k depth                                   |
| RIF/USDT(MA2)     | Using [DWAP](fundamentals/dwap.md), 200k depth                                   |
| RIF/USDT(MA3)     | Using [DWAP](fundamentals/dwap.md), 600k depth                                   |
| RIF/USDT(mp1%)    | To move the price 1 percent                                                      |
| USD/ARS           | Free, from press portals                                                         |
| USD/ARS(CCB)      | Paid in Bitcoin                                                                  |
| USD/ARS(CCL)      |                                                                                  |
| USD/BPRO          | Inverted pair of pair BPRO/USD                                                   |
| USD/BTC           | Inverted pair of pair BTC/USD                                                    |
| USD/COP           | Free, from press portals                                                         |
| USD/COP(CCB)      | Paid in Bitcoin                                                                  |
| USD/MOC           | Inverted pair of pair MOC/USD                                                    |
| USD/MXN           |                                                                                  |
| USDT/BTC          | Inverted pair of pair BTC/USDT                                                   |
| USDT/USD          |                                                                                  |
| USDT/USD(B)       | Passing through Bitcoin                                                          |


## Formulas used in the computed coinpairs

```
ARS/BPRO         =  (bpro_btc × btc_ars)⁻¹
ARS/BTC          =  (btc_ars)⁻¹
ARS/USD(CCB)     =  (btc_ars / btc_usd)⁻¹
BNB/USD          =  bnb_usdt × btc_usd / btc_usdt
BPRO/ARS         =  bpro_btc × btc_ars
BPRO/COP         =  bpro_btc × btc_cop
BPRO/MOC         =  (Median((moc_btc_sov × btc_usd), moc_usd_oku) / btc_usd × bpro_btc)⁻¹
BPRO/USD         =  bpro_btc × btc_usd
BTC/BPRO         =  (bpro_btc)⁻¹
BTC/MOC          =  (Median((moc_btc_sov × btc_usd), moc_usd_oku) / btc_usd)⁻¹
BTC/USD(24h)     =  (BTC/USD@NOW - BTC/USD@24hAGO) / BTC/USD@24hAGO
COP/BPRO         =  (bpro_btc × btc_cop)⁻¹
COP/BTC          =  (btc_cop)⁻¹
COP/USD(CCB)     =  (btc_cop / btc_usd)⁻¹
ETH/USD(B)       =  eth_btc × btc_usd
ISLIQ_ROC        =  MultiCollateralGuard.readyToLiquidate([
                        [rif_usdt_ma],
                        [doc_usd_tec]
                    ])
ISLIQ_ROC(test)  =  MultiCollateralGuardTestnet.readyToLiquidate([
                        [rif_usdt_ma],
                        [doc_usd_tec_test]
                    ])
MOC/BPRO         =  Median((moc_btc_sov × btc_usd), moc_usd_oku) / btc_usd × bpro_btc
MOC/BTC          =  Median((moc_btc_sov × btc_usd), moc_usd_oku) / btc_usd
MOC/RIF          =  (rif_usdt_ma × usdt_usd / moc_usd_oku)⁻¹
MOC/USD          =  moc_btc_sov × btc_usd
MOC/USD(WM)      =  Median((moc_btc_sov × btc_usd), moc_usd_oku)
RIF/MOC          =  rif_usdt_ma × usdt_usd / moc_usd_oku
RIF/USD          =  rif_btc × btc_usd
RIF/USD(B)       =  rif_btc × btc_usd
RIF/USD(T)       =  rif_usdt × usdt_usd
RIF/USD(TB)      =  rif_usdt × btc_usd / btc_usdt
RIF/USD(TBMA)    =  rif_usdt_ma × btc_usd / btc_usdt
RIF/USD(TBMA2)   =  rif_usdt_ma2 × btc_usd / btc_usdt
RIF/USD(TBMA3)   =  rif_usdt_ma3 × btc_usd / btc_usdt
RIF/USD(TMA)     =  rif_usdt_ma × usdt_usd
RIF/USD(TMA2)    =  rif_usdt_ma2 × usdt_usd
RIF/USD(TMA3)    =  rif_usdt_ma3 × usdt_usd
RIF/USD(WMTB)    =  Weighted(
                      (rif_usdt × btc_usd / btc_usdt) at 75%,
                      (rif_btc × btc_usd) at 25%
                    )
USD/ARS(CCB)     =  btc_ars / btc_usd
USD/BPRO         =  (bpro_btc × btc_usd)⁻¹
USD/BTC          =  (btc_usd)⁻¹
USD/COP(CCB)     =  btc_cop / btc_usd
USD/MOC          =  (Median((moc_btc_sov × btc_usd), moc_usd_oku))⁻¹
USDT/BTC         =  (btc_usdt)⁻¹
USDT/USD(B)      =  btc_usd / btc_usdt
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


### For coinpair BTC/ARS (from Bitcoin to Peso Arg.)

| Source    |   Weight | URI                                                                                 |
|-----------|----------|-------------------------------------------------------------------------------------|
| belo.app  |     0.20 | https://api.belo.app/public/price                                                   |
| Binance   |     0.20 | https://api.binance.com/api/v3/ticker/24hr?symbol=BTCARS                            |
| BuenBit   |     0.20 | http://91f83c67-4611-4562-ae66-421ac3d642eb.buenbit.com/public/market_price/btc/ars |
| Decrypto  |     0.20 | https://api.decrypto.la/1.0/frontend/trading/data/prices                            |
| Lemoncash |     0.20 | https://api.lemoncash.com.ar/api/v1/exchange-rates-quotations-external              |


### For coinpair BTC/USD (from Bitcoin to Dollar)

| Source   |   Weight | URI                                                  |
|----------|----------|------------------------------------------------------|
| Coinbase |     0.25 | https://api.coinbase.com/v2/prices/spot?currency=USD |
| Bitstamp |     0.22 | https://www.bitstamp.net/api/v2/ticker/btcusd/       |
| Bitfinex |     0.18 | https://api-pub.bitfinex.com/v2/ticker/tBTCUSD       |
| Kraken   |     0.18 | https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD |
| Gemini   |     0.17 | https://api.gemini.com/v1/pubticker/BTCUSD           |


### For coinpair ETH/USD (from Ether to Dollar)

| Source   |   Weight | URI                                                  |
|----------|----------|------------------------------------------------------|
| Coinbase |     0.25 | https://api.coinbase.com/v2/prices/ETH-USD/spot      |
| Bitstamp |     0.22 | https://www.bitstamp.net/api/v2/ticker/ethusd/       |
| Bitfinex |     0.18 | https://api-pub.bitfinex.com/v2/ticker/tETHUSD       |
| Kraken   |     0.18 | https://api.kraken.com/0/public/Ticker?pair=XETHZUSD |
| Gemini   |     0.17 | https://api.gemini.com/v1/pubticker/ETHUSD           |


### For coinpair RIF/BTC (from RIF to Bitcoin)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFBTC)


### For coinpair RIF/USDT (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=RIFUSDT)


### For coinpair RIF/USDT(mp1%) (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/BTC(mp1%) (from RIF to Bitcoin)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFBTC)


### For coinpair RIF/USDT(MA) (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA2) (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair RIF/USDT(MA3) (from RIF to Tether)

Only Binance (URI: https://api.binance.com/api/v3/depth?symbol=RIFUSDT)


### For coinpair ETH/BTC (from Ether to Bitcoin)

| Source   |   Weight | URI                                                      |
|----------|----------|----------------------------------------------------------|
| Bitstamp |     0.25 | https://www.bitstamp.net/api/v2/ticker/ethbtc/           |
| Bitfinex |     0.25 | https://api-pub.bitfinex.com/v2/ticker/tETHBTC           |
| Kraken   |     0.25 | https://api.kraken.com/0/public/Ticker?pair=ETHBTC       |
| Binance  |     0.25 | https://api.binance.com/api/v3/ticker/24hr?symbol=ETHBTC |


### For coinpair BTC/USDT (from Bitcoin to Tether)

| Source   |   Weight | URI                                                                   |
|----------|----------|-----------------------------------------------------------------------|
| Binance  |     0.65 | https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT       |
| OKX      |     0.15 | https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT              |
| Bybit    |     0.10 | https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT  |
| Huobi    |     0.05 | https://api.huobi.pro/market/detail/merged?symbol=btcusdt             |
| KuCoin   |     0.05 | https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT |


### For coinpair BNB/USDT (from BinanceCoin to Tether)

Only Binance (URI: https://api.binance.com/api/v3/ticker/24hr?symbol=BNBUSDT)


### For coinpair USD/ARS(CCL) (from Dollar to Peso Arg.)

| Source           |   Weight | URI                                                                         |
|------------------|----------|-----------------------------------------------------------------------------|
| Ambito.com       |     0.14 | https://mercados.ambito.com//dolarrava/cl/variacion                         |
| CriptoYa.com     |     0.14 | https://criptoya.com/api/dolar                                              |
| LaNacion.com.ar  |     0.14 | https://api-contenidos.lanacion.com.ar/json/V3/economia/cotizacionblue/DCCL |
| DolarHoy.com     |     0.14 | https://dolarhoy.com/cotizaciondolarcontadoconliqui                         |
| Infobae          |     0.14 | https://www.infobae.com/economia/divisas/dolar-hoy/                         |
| InfoDolar.com    |     0.14 | https://www.infodolar.com/cotizacion-dolar-contado-con-liquidacion.aspx     |
| CoinMonitor.info |     0.14 | https://coinmonitor.info/chart_DOLARES_24hs.json                            |


### For coinpair USD/ARS (from Dollar to Peso Arg.)

| Source           |   Weight | URI                                                                          |
|------------------|----------|------------------------------------------------------------------------------|
| Ambito.com       |     0.14 | https://mercados.ambito.com/dolar/informal/variacion                         |
| CriptoYa.com     |     0.14 | https://criptoya.com/api/dolar                                               |
| LaNacion.com.ar  |     0.14 | https://api-contenidos.lanacion.com.ar/json/V3/economia/cotizacionblue/DBLUE |
| DolarHoy.com     |     0.14 | https://dolarhoy.com/cotizaciondolarblue                                     |
| Infobae          |     0.14 | https://www.infobae.com/economia/divisas/dolar-hoy/                          |
| InfoDolar.com    |     0.14 | https://www.infodolar.com/cotizacion-dolar-blue.aspx                         |
| CoinMonitor.info |     0.14 | https://coinmonitor.info/chart_DOLARES_24hs.json                             |


### For coinpair USD/MXN (from Dollar to Peso Mex.)

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


### For coinpair MOC/BTC(sov) (from MOC to Bitcoin)

Only Sovryn onchain (URI: https://public-node.rsk.co)


### For coinpair MOC/USD(Oku) (from MOC to Dollar)

Only Oku onchain (URI: https://public-node.rsk.co)


### For coinpair BPRO/BTC (from BPro to Bitcoin)

Only MOC onchain (URI: https://public-node.rsk.co)


### For coinpair DOC/USD(tec) (from DOC to Dollar)

Only DOC/USD onchain (URI: https://public-node.rsk.co)


### For coinpair DOC/USD(tec-test) (from DOC to Dollar)

Only DOC/USD onchain (testnet) (URI: https://public-node.rsk.co)


### For coinpair GAS/BTC (from Gas to Bitcoin)

Only RSK onchain (URI: https://public-node.rsk.co)


### For coinpair USDT/USD (from Tether to Dollar)

| Source   |   Weight | URI                                                        |
|----------|----------|------------------------------------------------------------|
| Bitstamp |     0.15 | https://www.bitstamp.net/api/v2/ticker/usdtusd/            |
| Coinbase |     0.35 | https://api.exchange.coinbase.com/products/USDT-USD/ticker |
| Gemini   |     0.15 | https://api.gemini.com/v1/pubticker/usdtusd                |
| Kraken   |     0.35 | https://api.kraken.com/0/public/Ticker?pair=USDTUSD        |


### For coinpair USD/COP (from Dollar to Peso Col.)

| Source      |   Weight | URI                                                                                                     |
|-------------|----------|---------------------------------------------------------------------------------------------------------|
| BanRep      |     0.50 | https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario |
| DolarHoy.co |     0.50 | https://www.dolarhoy.co                                                                                 |


### For coinpair BTC/COP (from Bitcoin to Peso Col.)

| Source   |   Weight | URI                                                                                 |
|----------|----------|-------------------------------------------------------------------------------------|
| BuenBit  |     0.33 | http://91f83c67-4611-4562-ae66-421ac3d642eb.buenbit.com/public/market_price/btc/cop |
| Coinbase |     0.33 | https://api.coinbase.com/v2/prices/BTC-COP/spot                                     |
| buda.com |     0.33 | https://www.buda.com/api/v2/markets/BTC-COP/ticker                                  |


### For coinpair BLOCK(RSK)

Only RSK onchain (URI: https://public-node.rsk.co)


### For coinpair BTC/USD(och) (from Bitcoin to Dollar)

Only MOC onchain (URI: https://public-node.rsk.co)

