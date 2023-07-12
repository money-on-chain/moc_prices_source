# Options for the `RIF/USD` price source

Currently there are **3** options and they respond to the following formulas:

```
RIF/USD(B) = rif_btc * btc_usd
RIF/USD(TB) = rif_usdt * btc_usd / btc_usdt
RIF/USD(T) = rif_usdt * usdt_usd
```

An example of these options can be seen by running the `moc_prices_source_check "RIF/USD*"` command.

## Example:

```
user@workstation:~$ moc_prices_source_check "RIF/USD*"

From       To       V.    Exchnage        Response        Weigh  %      Time
---------  -------  ----  --------------  ------------  -------  -----  ------
Bitcoin    Dollar         Bitfinex        $  30.28600K     0.18  18.0   1.01s
Bitcoin    Dollar         Bitstamp        $  30.23400K     0.22  22.0   0.8s
Bitcoin    Dollar         Coinbase        $  30.23921K     0.25  25.0   1.0s
Bitcoin    Dollar         Gemini          $  30.24422K     0.17  17.0   1.61s
Bitcoin    Dollar         Kraken          $  30.23790K     0.18  18.0   1.0s
Bitcoin    Tether         Binance         ₮  30.22201K     0.8   80.0   1.64s
Bitcoin    Tether         Bitfinex        ₮  30.22900K     0.05  5.0    1.01s
Bitcoin    Tether         Coinbase        ₮  30.24002K     0.1   10.0   0.79s
Bitcoin    Tether         Kraken          ₮  30.24100K     0.05  5.0    1.0s
RIF Token  Bitcoin        Binance         ₿   2.93000µ     1     100.0  1.62s
RIF Token  Bitcoin        BitHumb         ₿   6.30000µ     0     N/A    2.21s
RIF Token  Bitcoin        Coingecko       ₿   2.92000µ     0     N/A    0.79s
RIF Token  Bitcoin        MEXC            ₿   2.92900µ     0     N/A    1.21s
RIF Token  Bitcoin        Sovryn onchain  ₿   2.94221µ     0     N/A    1.84s
RIF Token  Tether         Binance         ₮  88.50000m     1     100.0  1.2s
Tether     Dollar         Bitstamp        $   1.00002      0.15  15.0   1.22s
Tether     Dollar         Coinbase        $ 999.93500m     0.45  45.0   0.82s
Tether     Dollar         Kraken          $ 999.98000m     0.4   40.0   1.41s

    Coin pair           Mediam             Mean    Weighted median  Sources
--  -----------  -------------  ---------------  -----------------  ---------
↓   BTC/USD      30239.2        30248.3              30239.2        5
↓   BTC/USDT     30234.5        30233                30222          4
↓   RIF/BTC          2.93e-06       3.60424e-06          2.93e-06   5
ƒ   RIF/USD          0.0886009      0.109022             0.0886009  N/A
ƒ   RIF/USD(B)       0.0886009      0.109022             0.0886009  N/A
ƒ   RIF/USD(T)       0.0884982      0.0884981            0.0884982  N/A
ƒ   RIF/USD(TB)      0.0885138      0.0885447            0.0885504  N/A
↓   RIF/USDT         0.0885         0.0885               0.0885     1
↓   USDT/USD         0.99998        0.999978             0.99998    3

Response time 2.25s

user@workstation:~$
```

