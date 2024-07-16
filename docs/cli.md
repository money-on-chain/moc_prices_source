# **MoC prices source**

This is the python package used in [**Money on Chain**](https://moneyonchain.com/) projects where it is required to get the coinpair values directly from the sources.
This package includes a CLI tool that allows you to query the coinpair values in the same way that [**Money on Chain**](https://moneyonchain.com/) projects do.



## How the included CLI tool looks like

Get command help

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
user@workstation:~$
```

Get data from only coinpairs that start from `BTC`

```shell
user@workstation:~$ moc_prices_source_check BTC/*

From     To               V.    Exchnage       Response        Weight     %  Time
-------  ---------------  ----  -------------  ------------  --------  ----  ------
Bitcoin  Dollar                 Bitfinex       $  67.13000K      0.18  18    0.88s
Bitcoin  Dollar                 Bitstamp       $  67.01400K      0.22  22    1.9s
Bitcoin  Dollar                 Coinbase       $  66.99459K      0.25  25    0.85s
Bitcoin  Dollar                 Gemini         $  67.01966K      0.17  17    1.47s
Bitcoin  Dollar                 Kraken         $  67.01880K      0.18  18    1.88s
Bitcoin  Peso Argentino         ArgenBTC       $  82.39259M      0.14  14.3  1.06s
Bitcoin  Peso Argentino         Binance        $  83.00342M      0.14  14.3  1.31s
Bitcoin  Peso Argentino         BuenBit        $  83.63290M      0.14  14.3  1.91s
Bitcoin  Peso Argentino         Decrypto       $  84.44535M      0.14  14.3  3.58s
Bitcoin  Peso Argentino         Lemoncash      $  81.65245M      0.14  14.3  1.27s
Bitcoin  Peso Argentino         belo.app       $  83.86705M      0.14  14.3  1.47s
Bitcoin  Peso Argentino         cryptomkt.com  $  79.36550M      0.14  14.3  1.07s
Bitcoin  Peso Colombiano        BuenBit        $ 249.25296M      0.2   20    1.9s
Bitcoin  Peso Colombiano        Coinbase       $ 258.59249M      0.2   20    1.05s
Bitcoin  Peso Colombiano        bitso.com      $ 252.78000M      0.2   20    1.05s
Bitcoin  Peso Colombiano        buda.com       $ 251.35210M      0.2   20    1.05s
Bitcoin  Peso Colombiano        cryptomkt.com  $ 252.46572M      0.2   20    1.05s
Bitcoin  Tether                 Binance        ₮  67.09000K      0.8   80    1.3s
Bitcoin  Tether                 Bitfinex       ₮  67.08200K      0.05   5    1.3s
Bitcoin  Tether                 Coinbase       ₮  67.10688K      0.1   10    0.88s
Bitcoin  Tether                 Kraken         ₮  67.07100K      0.05   5    1.3s

    Coin pair             Mediam             Mean    Weighted median  Sources    Ok
--  -----------  ---------------  ---------------  -----------------  ---------  ----
↓   BTC/ARS          8.30034e+07      8.26228e+07        8.30034e+07  7 of 7     ✓
↓   BTC/COP          2.52466e+08      2.52889e+08        2.52466e+08  5 of 5     ✓
↓   BTC/USD      67018.8          67035.4            67018.8          5 of 5     ✓
↓   BTC/USDT     67086            67087.5            67088.9          4 of 4     ✓

Response time 3.62s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

From          To               V.    Exchnage               Response        Weight      %  Time
------------  ---------------  ----  ---------------------  ------------  --------  -----  ------
Binance Coin  Tether                 Binance                ₮ 590.30000       1     100    1.34s
Bitcoin       Dollar                 Bitfinex               $  67.13000K      0.18   18    0.81s
Bitcoin       Dollar                 Bitstamp               $  67.03500K      0.22   22    1.42s
Bitcoin       Dollar                 Coinbase               $  67.01231K      0.25   25    0.96s
Bitcoin       Dollar                 Gemini                 $  67.01966K      0.17   17    1.58s
Bitcoin       Dollar                 Kraken                 $  67.01880K      0.18   18    0.78s
Bitcoin       Peso Argentino         ArgenBTC               $  82.39259M      0.14   14.3  0.82s
Bitcoin       Peso Argentino         Binance                $  83.00342M      0.14   14.3  0.98s
Bitcoin       Peso Argentino         BuenBit                $  83.63290M      0.14   14.3  1.64s
Bitcoin       Peso Argentino         Decrypto               $  84.45152M      0.14   14.3  3.81s
Bitcoin       Peso Argentino         Lemoncash              $  81.67107M      0.14   14.3  1.41s
Bitcoin       Peso Argentino         belo.app               $  83.86705M      0.14   14.3  1.62s
Bitcoin       Peso Argentino         cryptomkt.com          $  79.36550M      0.14   14.3  0.85s
Bitcoin       Peso Colombiano        BuenBit                $ 249.25296M      0.2    20    1.64s
Bitcoin       Peso Colombiano        Coinbase               $ 258.63841M      0.2    20    0.69s
Bitcoin       Peso Colombiano        bitso.com              $ 252.78000M      0.2    20    0.91s
Bitcoin       Peso Colombiano        buda.com               $ 251.35210M      0.2    20    0.88s
Bitcoin       Peso Colombiano        cryptomkt.com          $ 252.52040M      0.2    20    0.74s
Bitcoin       Tether                 Binance                ₮  67.09889K      0.8    80    2.01s
Bitcoin       Tether                 Bitfinex               ₮  67.08200K      0.05    5    0.8s
Bitcoin       Tether                 Coinbase               ₮  67.05418K      0.1    10    0.81s
Bitcoin       Tether                 Kraken                 ₮  67.07100K      0.05    5    0.94s
Dollar        Peso Argentino   CCL   Ambito.com             $   1.24902K      0.14   14.3  0.96s
Dollar        Peso Argentino   CCL   CoinMonitor.info       $   1.25717K      0.14   14.3  1.58s
Dollar        Peso Argentino   CCL   CriptoYa.com           $   1.24338K      0.14   14.3  0.81s
Dollar        Peso Argentino   CCL   DolarHoy.com           $   1.25075K      0.14   14.3  1.22s
Dollar        Peso Argentino   CCL   InfoDolar.com          $   1.22848K      0.14   14.3  1.31s
Dollar        Peso Argentino   CCL   Infobae                $   1.25327K      0.14   14.3  1.7s
Dollar        Peso Argentino   CCL   LaNacion.com.ar        $   1.24831K      0.14   14.3  1.35s
Dollar        Peso Argentino         Ambito.com             $   1.27000K      0.14   14.3  1.03s
Dollar        Peso Argentino         CoinMonitor.info       $   1.28500K      0.14   14.3  2.02s
Dollar        Peso Argentino         CriptoYa.com           $   1.27000K      0.14   14.3  0.87s
Dollar        Peso Argentino         DolarHoy.com           $   1.29000K      0.14   14.3  1.51s
Dollar        Peso Argentino         InfoDolar.com          $   1.29000K      0.14   14.3  1.52s
Dollar        Peso Argentino         Infobae                $   1.28500K      0.14   14.3  1.73s
Dollar        Peso Argentino         LaNacion.com.ar        $   1.27000K      0.14   14.3  1.32s
Dollar        Peso Colombiano        BanRep                 $   3.83764K      0.5    50    3.08s
Dollar        Peso Colombiano        DolarHoy.co            $   3.75000K      0.5    50    1.67s
Dollar        Peso Mexicano          Bitso.com              $  16.73400       0.1    10    0.86s
Dollar        Peso Mexicano          CitiBanamex            $  20.04275       0.1    10    0.88s
Dollar        Peso Mexicano          Currency.me.uk         $  16.75620       0.1    10    1.12s
Dollar        Peso Mexicano          ElDolar.info           $  16.66980       0.1    10    2.39s
Dollar        Peso Mexicano          ElEconomista.es        $  16.73600       0.1    10    1.38s
Dollar        Peso Mexicano          InfoDolar.com.mx       $  16.65500       0.1    10    1.4s
Dollar        Peso Mexicano          Intercam.com.mx        $  16.75615       0.1    10    1.34s
Dollar        Peso Mexicano          TheMoneyConverter.com  $  16.75251       0.1    10    1.33s
Dollar        Peso Mexicano          Wise.com               $  16.74800       0.1    10    0.92s
Dollar        Peso Mexicano          X-rates.com            $  16.74988       0.1    10    1.43s
Ether         Bitcoin                Binance                ₿  55.82000m      0.25   25    0.98s
Ether         Bitcoin                Bitfinex               ₿  55.74000m      0.25   25    0.74s
Ether         Bitcoin                Bitstamp               ₿  55.69874m      0.25   25    1.38s
Ether         Bitcoin                Kraken                 ₿  55.71000m      0.25   25    0.97s
Gas           Bitcoin                RSK onchain            ₿  65.16400p      1     100    1.86s
MOC Token     Bitcoin                Sovryn onchain         ₿   1.38891µ      1     100    1.94s
RIF Token     Bitcoin          mp1%  Binance                ₿  50.73925m      1     100    2.71s
RIF Token     Bitcoin                Binance                ₿   2.28000µ      1     100    0.97s
RIF Token     Tether           MA    Binance                ₮ 152.36218m      1     100    1.34s
RIF Token     Tether           MA2   Binance                ₮ 152.37002m      1     100    0.98s
RIF Token     Tether           MA3   Binance                ₮ 152.28874m      1     100    1.0s
RIF Token     Tether           mp1%  Binance                ₮  47.69312K      1     100    1.06s
RIF Token     Tether                 Binance                ₮ 152.40000m      1     100    1.32s
Tether        Dollar                 Bitstamp               $ 999.18000m      0.15   15    1.39s
Tether        Dollar                 Coinbase               $ 999.17500m      0.45   45    1.0s
Tether        Dollar                 Kraken                 $ 999.12000m      0.4    40    0.96s

    Coin pair                Mediam             Mean    Weighted median  Sources    Ok
--  --------------  ---------------  ---------------  -----------------  ---------  ----
ƒ   BNB/USD           589.8            590.006            589.617        N/A        ✓
↓   BNB/USDT          590.3            590.3              590.3          1 of 1     ✓
↓   BTC/ARS             8.30034e+07      8.26263e+07        8.30034e+07  7 of 7     ✓
↓   BTC/COP             2.5252e+08       2.52909e+08        2.5252e+08   5 of 5     ✓
↓   BTC/USD         67019.7          67043.2            67019.7          5 of 5     ✓
↓   BTC/USDT        67076.5          67076.5            67097.2          4 of 4     ✓
↓   ETH/BTC             0.055725         0.0557422          0.055725     4 of 4     ✓
ƒ   ETH/USD          3734.67          3737.13            3734.67         N/A        ✓
↓   GAS/BTC             6.5164e-11       6.5164e-11         6.5164e-11   1 of 1     ✓
↓   MOC/BTC             1.38891e-06      1.38891e-06        1.38891e-06  1 of 1     ✓
ƒ   MOC/USD             0.0930844        0.093117           0.0930844    N/A        ✓
↓   RIF/BTC             2.28e-06         2.28e-06           2.28e-06     1 of 1     ✓
↓   RIF/BTC(mp1%)       0.0507392        0.0507392          0.0507392    1 of 1     ✓
ƒ   RIF/USD             0.152805         0.152858           0.152805     N/A        ✓
ƒ   RIF/USD(B)          0.152805         0.152858           0.152805     N/A        ✓
ƒ   RIF/USD(T)          0.152274         0.152272           0.152274     N/A        ✓
ƒ   RIF/USD(TB)         0.152271         0.152324           0.152224     N/A        ✓
ƒ   RIF/USD(WMTB)       0.152404         0.152458           0.152369     N/A        ✓
↓   RIF/USDT            0.1524           0.1524             0.1524       1 of 1     ✓
↓   RIF/USDT(MA)        0.152362         0.152362           0.152362     1 of 1     ✓
↓   RIF/USDT(MA2)       0.15237          0.15237            0.15237      1 of 1     ✓
↓   RIF/USDT(MA3)       0.152289         0.152289           0.152289     1 of 1     ✓
↓   RIF/USDT(mp1%)  47693.1          47693.1            47693.1          1 of 1     ✓
↓   USD/ARS          1285             1280               1285            7 of 7     ✓
ƒ   USD/ARS(CCB)     1238.49          1232.43            1238.49         N/A        ✓
↓   USD/ARS(CCL)     1249.02          1247.2             1249.02         7 of 7     ✓
↓   USD/COP          3793.82          3793.82            3793.82         2 of 2     ✓
ƒ   USD/COP(CCB)     3767.86          3772.33            3767.86         N/A        ✓
↓   USD/MXN            16.7489          17.06              18.3954       10 of 10   ✓
↓   USDT/USD            0.999175         0.999158           0.999175     3 of 3     ✓
ƒ   USDT/USD(B)         0.999153         0.999503           0.998844     N/A        ✓

Response time 4.16s

user@workstation:~$
```

