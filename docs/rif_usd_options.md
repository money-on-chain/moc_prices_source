# Options for the `RIF/USD` price source

Currently there are **4** options and they respond to the following formulas:

```
RIF/USD(B) = rif_btc * btc_usd
RIF/USD(TB) = rif_usdt * btc_usd / btc_usdt
RIF/USD(WMTB) = weighted_median(
                [(rif_usdt * btc_usd / btc_usdt), (rif_btc * btc_usd)],
                [0.75, 0.25])
RIF/USD(T) = rif_usdt * usdt_usd
```

An example of these options can be seen by running the `moc_prices_source_check "RIF/USD*"` command.

## Example:

```
user@workstation:~$ moc_prices_source_check "RIF/USD*"

From       To       V.    Exchnage        Response        Weigh  %      Time
---------  -------  ----  --------------  ------------  -------  -----  ------
Bitcoin    Dollar         Bitfinex        $  29.85900K     0.18  18.0   0.49s
Bitcoin    Dollar         Bitstamp        $  29.83400K     0.22  22.0   0.49s
Bitcoin    Dollar         Coinbase        $  29.83312K     0.25  25.0   0.34s
Bitcoin    Dollar         Gemini          $  29.83525K     0.17  17.0   1.1s
Bitcoin    Dollar         Kraken          $  29.82890K     0.18  18.0   0.48s
Bitcoin    Tether         Binance         ₮  29.82528K     0.8   80.0   0.57s
Bitcoin    Tether         Bitfinex        ₮  29.82600K     0.05  5.0    0.49s
Bitcoin    Tether         Coinbase        ₮  29.82255K     0.1   10.0   0.34s
Bitcoin    Tether         Kraken          ₮  29.80490K     0.05  5.0    0.49s
RIF Token  Bitcoin        Binance         ₿   2.87000µ     1     100.0  0.57s
RIF Token  Bitcoin        BitHumb         ₿   6.30000µ     0     N/A    2.2s
RIF Token  Bitcoin        Coingecko       ₿   2.86000µ     0     N/A    0.9s
RIF Token  Bitcoin        MEXC            ₿   2.86500µ     0     N/A    0.53s
RIF Token  Bitcoin        Sovryn onchain  ₿   2.90639µ     0     N/A    1.33s
RIF Token  Tether         Binance         ₮  85.60000m     1     100.0  0.54s
Tether     Dollar         Bitstamp        $ 999.94000m     0.15  15.0   0.45s
Tether     Dollar         Coinbase        $   1.00022      0.45  45.0   0.36s
Tether     Dollar         Kraken          $   1.00002      0.4   40.0   0.5s

    Coin pair             Mediam             Mean    Weighted median  Sources
--  -------------  -------------  ---------------  -----------------  ---------
↓   BTC/USD        29834          29838.1              29834          5
↓   BTC/USDT       29823.9        29819.7              29824.1        4
↓   RIF/BTC            2.87e-06       3.56028e-06          2.87e-06   5
ƒ   RIF/USD            0.0856236      0.106232             0.0856236  N/A
ƒ   RIF/USD(B)         0.0856236      0.106232             0.0856236  N/A
ƒ   RIF/USD(T)         0.0856017      0.085605             0.0856017  N/A
ƒ   RIF/USD(TB)        0.0856289      0.0856527            0.0856285  N/A
ƒ   RIF/USD(WMTB)      0.0856263      0.0959422            0.085626   N/A
↓   RIF/USDT           0.0856         0.0856               0.0856     1
↓   USDT/USD           1.00002        1.00006              1.00002    3

Response time 2.23s

user@workstation:~$
```

## Rationale behind the chosen nomenclature

`RIF/USD(B)`: Because it goes through *RIF/**B**itcoin* and ***B**itcoin/Dollar* to reach the desired pair.

`RIF/USD(TB)`: Because it goes through *RIF/**T**ether*, ***B**itcoin/Dollar* and *Bitcoin/**T**ether* to get to the desired pair.

`RIF/USD(T)`: Because it goes through *RIF/**T**ether* and ***T**ether/Dollar* to reach the desired pair.

`RIF/USD(WMTB)`: Because uses a **W**eighted **M**edian between `RIF/USD(B)` and `RIF/USD(TB)` to reach the desired pair.

