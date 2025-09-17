# Notes related to the branch `new-coinpair-rif_usd_tma` purpose

## Add `RIF/USD(TMA)` coinpair to be used by *RIF on chain*

### Description

Define a new computed coinpair `RIF/USD(TMA)` that reuses the Binance *“magic average”* orderbook-depth source for `RIF/USDT(MA)` as the base quote. Then multiply that value by the live `USDT/USD` conversion so the resulting price in `USD` reflects any deviation of `USDT` from its peg. The suffix **TMA** indicates that the price is obtained through (T)ether and ultimately relies on the (M)agic (A)verage mechanism.
