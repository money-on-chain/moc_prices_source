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

From     To               V.    Exchnage    Response        Weight     %  Time
-------  ---------------  ----  ----------  ------------  --------  ----  ------
Bitcoin  Dollar                 Bitfinex    $  97.60900K      0.18  18    0.14s
Bitcoin  Dollar                 Bitstamp    $  97.62100K      0.22  22    0.13s
Bitcoin  Dollar                 Coinbase    $  97.75202K      0.25  25    0.15s
Bitcoin  Dollar                 Gemini      $  97.62253K      0.17  17    0.73s
Bitcoin  Dollar                 Kraken      $  97.61320K      0.18  18    0.3s
Bitcoin  Peso Argentino         Binance     $ 149.30197M      0.2   20    0.38s
Bitcoin  Peso Argentino         BuenBit     $ 148.62379M      0.2   20    3.25s
Bitcoin  Peso Argentino         Decrypto    $ 148.62021M      0.2   20    1.97s
Bitcoin  Peso Argentino         Lemoncash   $ 146.03527M      0.2   20    0.66s
Bitcoin  Peso Argentino         belo.app    $ 149.92490M      0.2   20    0.28s
Bitcoin  Peso Colombiano        BuenBit     $ 355.27837M      0.33  33.3  1.24s
Bitcoin  Peso Colombiano        Coinbase    $ 359.18179M      0.33  33.3  0.32s
Bitcoin  Peso Colombiano        buda.com    $ 346.95004M      0.33  33.3  3.19s
Bitcoin  Tether                 Binance     ₮  97.61932K      0.65  65    0.35s
Bitcoin  Tether                 Bybit       ₮  97.61685K      0.1   10    0.42s
Bitcoin  Tether                 Huobi       ₮  97.59964K      0.05   5    0.96s
Bitcoin  Tether                 KuCoin      ₮  97.62255K      0.05   5    0.49s
Bitcoin  Tether                 OKX         ₮  97.61125K      0.15  15    0.4s

    Coin pair                 Value   Sources count    Ok
--  -----------  ------------------  ---------------  ----
↓   BTC/ARS      148,623,790.420000      5 of 5        ✓
↓   BTC/COP      355,278,370.898000      3 of 3        ✓
↓   BTC/USD           97,621.000000      5 of 5        ✓
↓   BTC/USDT          97,619.325000      5 of 5        ✓

Response time 3.26s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

From          To               V.      Exchnage               Response                Weight  %      Time
------------  ---------------  ------  ---------------------  --------------------  --------  -----  ------
Binance Coin  Tether                   Binance                ₮ 945.96000               1     100.0  0.38s
Bitcoin       Dollar                   Bitfinex               $  97.60900K              0.18  18.0   0.11s
Bitcoin       Dollar                   Bitstamp               $  97.62700K              0.22  22.0   0.3s
Bitcoin       Dollar                   Coinbase               $  97.75202K              0.25  25.0   0.25s
Bitcoin       Dollar                   Gemini                 $  97.62253K              0.17  17.0   0.93s
Bitcoin       Dollar                   Kraken                 $  97.61650K              0.18  18.0   0.38s
Bitcoin       Peso Argentino           Binance                $ 149.30197M              0.2   20.0   0.36s
Bitcoin       Peso Argentino           BuenBit                $ 148.24363M              0.2   20.0   10.2s
Bitcoin       Peso Argentino           Decrypto               $ 148.57088M              0.2   20.0   2.04s
Bitcoin       Peso Argentino           Lemoncash              $ 146.04463M              0.2   20.0   0.68s
Bitcoin       Peso Argentino           belo.app               $ 149.86164M              0.2   20.0   3.35s
Bitcoin       Peso Colombiano          BuenBit                $ 355.27837M              0.33  33.3   1.21s
Bitcoin       Peso Colombiano          Coinbase               $ 359.18179M              0.33  33.3   0.58s
Bitcoin       Peso Colombiano          buda.com               $ 346.95004M              0.33  33.3   7.46s
Bitcoin       Tether                   Binance                ₮  97.59000K              0.65  65.0   0.4s
Bitcoin       Tether                   Bybit                  ₮  97.58565K              0.1   10.0   0.45s
Bitcoin       Tether                   Huobi                  ₮  97.59597K              0.05  5.0    0.39s
Bitcoin       Tether                   KuCoin                 ₮  97.59950K              0.05  5.0    0.42s
Bitcoin       Tether                   OKX                    ₮  97.60995K              0.15  15.0   0.44s
Bpro          Bitcoin                  MOC onchain            ₿   1.22221               1     100.0  1.85s
DOC Token     Dollar                   Dummy                  $   1.00000               1     100.0  0.0s
Dollar        Peso Argentino   CCL     Ambito.com             $   1.52253K              0.14  14.3   0.16s
Dollar        Peso Argentino   CCL     CoinMonitor.info       $   1.52488K              0.14  14.3   0.74s
Dollar        Peso Argentino   CCL     CriptoYa.com           $   1.50896K              0.14  14.3   0.19s
Dollar        Peso Argentino   CCL     DolarHoy.com           $   1.52080K              0.14  14.3   0.61s
Dollar        Peso Argentino   CCL     InfoDolar.com          $   1.52444K              0.14  14.3   0.84s
Dollar        Peso Argentino   CCL     Infobae                $   1.52744K              0.14  14.3   0.54s
Dollar        Peso Argentino   CCL     LaNacion.com.ar        $   1.52954K              0.14  14.3   0.18s
Dollar        Peso Argentino           Ambito.com             $   1.50500K              0.14  14.3   1.34s
Dollar        Peso Argentino           CoinMonitor.info       $   1.51500K              0.14  14.3   0.83s
Dollar        Peso Argentino           CriptoYa.com           $   1.50500K              0.14  14.3   7.29s
Dollar        Peso Argentino           DolarHoy.com           $   1.50500K              0.14  14.3   10.12s
Dollar        Peso Argentino           InfoDolar.com          $   1.50500K              0.14  14.3   3.64s
Dollar        Peso Argentino           Infobae                $   1.51500K              0.14  14.3   0.57s
Dollar        Peso Argentino           LaNacion.com.ar        $   1.50500K              0.14  14.3   0.14s
Dollar        Peso Colombiano          BanRep                 $   3.65501K              0.5   50.0   0.75s
Dollar        Peso Colombiano          DolarHoy.co            $   3.70000K              0.5   50.0   1.0s
Dollar        Peso Mexicano            Bitso.com              $  17.81400               0.1   10.0   3.38s
Dollar        Peso Mexicano            CitiBanamex            $  20.04275               0.1   10.0   0.37s
Dollar        Peso Mexicano            Currency.me.uk         $  17.81280               0.1   10.0   1.82s
Dollar        Peso Mexicano            ElDolar.info           $  17.77450               0.1   10.0   0.98s
Dollar        Peso Mexicano            ElEconomista.es        $  17.93300               0.1   10.0   0.92s
Dollar        Peso Mexicano            InfoDolar.com.mx       $  17.73500               0.1   10.0   8.24s
Dollar        Peso Mexicano            Intercam.com.mx        $  17.81305               0.1   10.0   1.11s
Dollar        Peso Mexicano            TheMoneyConverter.com  $  17.81254               0.1   10.0   3.53s
Dollar        Peso Mexicano            Wise.com               $  17.81310               0.1   10.0   0.44s
Dollar        Peso Mexicano            X-rates.com            $  17.81279               0.1   10.0   0.85s
Ether         Bitcoin                  Binance                ₿  34.63000m              0.25  25.0   0.4s
Ether         Bitcoin                  Bitfinex               ₿  34.63100m              0.25  25.0   0.32s
Ether         Bitcoin                  Bitstamp               ₿  34.60250m              0.25  25.0   0.35s
Ether         Bitcoin                  Kraken                 ₿  34.64000m              0.25  25.0   0.54s
Ether         Dollar                   Bitfinex               $   3.37850K              0.18  18.0   0.31s
Ether         Dollar                   Bitstamp               $   3.37980K              0.22  22.0   0.34s
Ether         Dollar                   Coinbase               $   3.38575K              0.25  25.0   0.62s
Ether         Dollar                   Gemini                 $   3.37863K              0.17  17.0   0.84s
Ether         Dollar                   Kraken                 $   3.37971K              0.18  18.0   0.45s
Gas           Bitcoin                  RSK onchain            ₿  26.06560p              1     100.0  1.72s
MOC Token     Bitcoin          Sovryn  Sovryn onchain         ₿ 371.22669p              1     100.0  3.31s
MOC Token     Dollar           Oku     Oku onchain            $  36.58623m              1     100.0  1.7s
RIF Token     Bitcoin          mp1%    Binance                ₿  50.73925m              1     100.0  2.71s
RIF Token     Bitcoin                  Binance                ₿ 380.00000p              1     100.0  0.39s
RIF Token     Tether           MA      Binance                ₮  37.45222m              1     100.0  0.39s
RIF Token     Tether           MA2     Binance                ₮  37.47018m              1     100.0  0.37s
RIF Token     Tether           MA3     Binance                ₮  37.47988m              1     100.0  0.39s
RIF Token     Tether           mp1%    Binance                ₮  24.18568K              1     100.0  0.36s
RIF Token     Tether                   Binance                ₮  37.60000m              1     100.0  0.39s
Tether        Dollar                   Bitstamp               $ 999.87500m              0.15  15.0   0.83s
Tether        Dollar                   Coinbase               $ 999.93500m              0.35  35.0   0.4s
Tether        Dollar                   Gemini                 $ 999.89000m              0.15  15.0   0.92s
Tether        Dollar                   Kraken                 $ 999.88500m              0.35  35.0   0.41s

    Coin pair                     Value   Sources count    Ok
--  ---------------  ------------------  ---------------  ----
ƒ   BNB/USD                  946.275272        N/A         ✓
↓   BNB/USDT                 945.960000      1 of 1        ✓
ƒ   BPRO/ARS         181,584,944.254282        N/A         ✓
↓   BPRO/BTC                   1.222211      1 of 1        ✓
ƒ   BPRO/COP         434,225,089.849684        N/A         ✓
ƒ   BPRO/USD             119,315.318164        N/A         ✓
↓   BTC/ARS          148,570,878.750000      5 of 5        ✓
↓   BTC/COP          355,278,370.898000      3 of 3        ✓
↓   BTC/USD               97,622.530000      5 of 5        ✓
↓   BTC/USDT              97,590.005000      5 of 5        ✓
↓   DOC/USD                    1.000000      1 of 1        ✓
↓   ETH/BTC                    0.034630      4 of 4        ✓
↓   ETH/USD                3,379.710000      5 of 5        ✓
ƒ   ETH/USD(B)             3,380.717025        N/A         ✓
↓   GAS/BTC               2.607 × 10⁻¹¹      1 of 1        ✓
ƒ   MOC/BPRO               4.559 × 10⁻⁷        N/A         ✓
ƒ   MOC/BTC                3.730 × 10⁻⁷        N/A         ✓
↓   MOC/BTC(Sovryn)        3.712 × 10⁻⁷      1 of 1        ✓
ƒ   MOC/USD                    0.036240        N/A         ✓
↓   MOC/USD(Oku)               0.036586      1 of 1        ✓
ƒ   MOC/USD(WM)                0.036413        N/A         ✓
↓   RIF/BTC                3.800 × 10⁻⁷      1 of 1        ✓
↓   RIF/BTC(mp1%)              0.050739      1 of 1        ✓
ƒ   RIF/USD                    0.037097        N/A         ✓
ƒ   RIF/USD(B)                 0.037097        N/A         ✓
ƒ   RIF/USD(T)                 0.037596        N/A         ✓
ƒ   RIF/USD(TB)                0.037613        N/A         ✓
ƒ   RIF/USD(TBMA)              0.037465        N/A         ✓
ƒ   RIF/USD(TMA)               0.037448        N/A         ✓
ƒ   RIF/USD(WMTB)              0.037484        N/A         ✓
↓   RIF/USDT                   0.037600      1 of 1        ✓
↓   RIF/USDT(MA)               0.037452      1 of 1        ✓
↓   RIF/USDT(MA2)              0.037470      1 of 1        ✓
↓   RIF/USDT(MA3)              0.037480      1 of 1        ✓
↓   RIF/USDT(mp1%)        24,185.678300      1 of 1        ✓
↓   USD/ARS                1,505.000000      7 of 7        ✓
ƒ   USD/ARS(CCB)           1,521.891297        N/A         ✓
↓   USD/ARS(CCL)           1,524.445000      7 of 7        ✓
↓   USD/COP                3,677.506400      2 of 2        ✓
ƒ   USD/COP(CCB)           3,639.307145        N/A         ✓
↓   USD/MXN                   17.793650     10 of 10       ✓
↓   USDT/USD                   0.999886      4 of 4        ✓
ƒ   USDT/USD(B)                1.000333        N/A         ✓

Response time 10.97s

user@workstation:~$
```
