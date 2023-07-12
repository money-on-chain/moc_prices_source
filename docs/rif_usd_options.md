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
Bitcoin    Dollar         Bitfinex        $  30.30000K     0.18  18.0   3.89s
Bitcoin    Dollar         Bitstamp        $  30.25300K     0.22  22.0   3.91s
Bitcoin    Dollar         Coinbase        $  30.24931K     0.25  25.0   2.52s
Bitcoin    Dollar         Gemini          $  30.25123K     0.17  17.0   3.9s
Bitcoin    Dollar         Kraken          $  30.25440K     0.18  18.0   2.89s
Bitcoin    Tether         Binance         ₮  30.25060K     0.8   80.0   3.9s
Bitcoin    Tether         Bitfinex        ₮  30.26100K     0.05  5.0    2.89s
Bitcoin    Tether         Coinbase        ₮  30.26417K     0.1   10.0   2.52s
Bitcoin    Tether         Kraken          ₮  30.28150K     0.05  5.0    2.69s
RIF Token  Bitcoin        Binance         ₿   2.92000µ     1     100.0  3.92s
RIF Token  Bitcoin        BitHumb         ₿   6.30000µ     0     N/A    4.71s
RIF Token  Bitcoin        Coingecko       ₿   2.93000µ     0     N/A    2.51s
RIF Token  Bitcoin        MEXC            ₿   2.92200µ     0     N/A    3.89s
RIF Token  Bitcoin        Sovryn onchain  ₿   2.94221µ     0     N/A    5.75s
RIF Token  Tether         Binance         ₮  88.50000m     1     100.0  3.88s
Tether     Dollar         Bitstamp        $ 999.97000m     0.15  15.0   3.91s
Tether     Dollar         Coinbase        $ 999.89500m     0.45  45.0   2.71s
Tether     Dollar         Kraken          $ 999.93000m     0.4   40.0   2.9s

    Coin pair           Mediam             Mean    Weighted median  Sources
--  -----------  -------------  ---------------  -----------------  ---------
↓   BTC/USD      30253          30261.6              30253          5
↓   BTC/USDT     30262.6        30264.3              30250.6        4
↓   RIF/BTC          2.93e-06       3.60284e-06          2.92e-06   5
ƒ   RIF/USD          0.0886413      0.109028             0.0883388  N/A
ƒ   RIF/USD(B)       0.0886413      0.109028             0.0883388  N/A
ƒ   RIF/USD(T)       0.0884938      0.088494             0.0884938  N/A
ƒ   RIF/USD(TB)      0.088472       0.088492             0.088507   N/A
↓   RIF/USDT         0.0885         0.0885               0.0885     1
↓   USDT/USD         0.99993        0.999932             0.99993    3

Response time 5.78s

user@workstation:~$
```

## Rationale behind the chosen nomenclature

`RIF/USD(B)`: Because it goes through *RIF/**B**itcoin* and ***B**itcoin/Dollar* to reach the desired pair.

`RIF/USD(TB)`: Because it goes through *RIF/**T**ether*, ***B**itcoin/Dollar* and *Bitcoin/**T**ether* to get to the desired pair.

`RIF/USD(T)`: Because it goes through *RIF/**T**ether* and ***T**ether/Dollar* to reach the desired pair.

