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
  -v, --verbose                   Verbose mode.
  --version                       Show version and exit.
  -j, --json                      Show data in JSON format and exit.
  -w, --weighing                  Show the default weighing and exit.
  -c, --computed                  Show the computed pairs formula and exit.
  -e, --show-envs                 Show used ENV variables used and exit.
  -s, --summary                   Show the summary and exit.
  -m, --markdown                  Set markdown for the summary format.
  -n, --not-ignore-zero-weighing  Not ignore sources with zero weighing.
  -h, --help                      Show this message and exit.
user@workstation:~$
```

Get data from only coinpairs that start from `BTC`

```shell
user@workstation:~$ moc_prices_source_check BTC/*

Coinpair    V.    Short description     Exchnage        Response        Weight      %  Time
----------  ----  --------------------  --------------  ------------  --------  -----  ------
BPRO/BTC          BPro to Bitcoin       MOC onchain     ₿   1.21310       1     100    1.93s
BTC/ARS           Bitcoin to Peso Arg.  Binance         $ 135.12397M      0.2    20    451ms
BTC/ARS           Bitcoin to Peso Arg.  BuenBit         $ 134.70770M      0.2    20    449ms
BTC/ARS           Bitcoin to Peso Arg.  Decrypto        $ 134.91922M      0.2    20    2.11s
BTC/ARS           Bitcoin to Peso Arg.  Lemoncash       $ 132.29125M      0.2    20    710ms
BTC/ARS           Bitcoin to Peso Arg.  belo.app        $ 135.54673M      0.2    20    282ms
BTC/COP           Bitcoin to Peso Col.  BuenBit         $ 323.84841M      0.33   33.3  454ms
BTC/COP           Bitcoin to Peso Col.  Coinbase        $ 327.95854M      0.33   33.3  663ms
BTC/COP           Bitcoin to Peso Col.  buda.com        $ 326.25767M      0.33   33.3  3.44s
BTC/USD     och   Bitcoin to Dollar     MOC onchain     $  89.19600K      1     100    1.68s
BTC/USD           Bitcoin to Dollar     Bitfinex        $  89.40900K      0.18   18    166ms
BTC/USD           Bitcoin to Dollar     Bitstamp        $  89.19300K      0.22   22    354ms
BTC/USD           Bitcoin to Dollar     Coinbase        $  89.30822K      0.25   25    635ms
BTC/USD           Bitcoin to Dollar     Gemini          $  89.28400K      0.17   17    1.06s
BTC/USD           Bitcoin to Dollar     Kraken          $  89.23240K      0.18   18    294ms
BTC/USDT          Bitcoin to Tether     Binance         ₮  89.31562K      0.65   65    445ms
BTC/USDT          Bitcoin to Tether     Bybit           ₮  89.31345K      0.1    10    493ms
BTC/USDT          Bitcoin to Tether     Huobi           ₮  89.31000K      0.05    5    447ms
BTC/USDT          Bitcoin to Tether     KuCoin          ₮  89.31135K      0.05    5    814ms
BTC/USDT          Bitcoin to Tether     OKX             ₮  89.31255K      0.15   15    811ms
MOC/BTC     sov   MOC to Bitcoin        Sovryn onchain  ₿ 415.62570p      1     100    883ms
MOC/USD     Oku   MOC to Dollar         Oku onchain     $  37.71208m      1     100    1.69s

    Coinpair                   Value   Sources count    Ok   Time
--  ------------  ------------------  ---------------  ----  ------
⛓   BPRO/BTC                1.213105      1 of 1        ✓    1.93s
⇓   BTC/ARS       134,919,219.450000      5 of 5        ✓    2.11s
⇄   BTC/BPRO                0.824331        N/A         ✓    <10ms
⇓   BTC/COP       326,257,671.605000      3 of 3        ✓    3.44s
⇄   BTC/MOC         2,386,608.811140        N/A         ✓    <10ms
⇓   BTC/USD            89,284.000000      5 of 5        ✓    1.06s
⛓   BTC/USD(och)       89,196.000000      1 of 1        ✓    1.68s
⇓   BTC/USDT           89,315.615000      5 of 5        ✓    814ms
⛓   MOC/BTC(sov)        4.156 × 10⁻⁷      1 of 1        ✓    883ms
⛓   MOC/USD(Oku)            0.037712      1 of 1        ✓    1.69s

Response time 3.46s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

Coinpair    V.    Short description       Exchnage               Response        Weight      %  Time
----------  ----  ----------------------  ---------------------  ------------  --------  -----  ------
BLOCK       RSK   Rootstock block number  RSK onchain            8469815           1     100    1.47s
BNB/USDT          BinanceCoin to Tether   Binance                ₮ 902.13000       1     100    411ms
BPRO/BTC          BPro to Bitcoin         MOC onchain            ₿   1.21325       1     100    1.61s
BTC/ARS           Bitcoin to Peso Arg.    Binance                $ 135.12397M      0.2    20    404ms
BTC/ARS           Bitcoin to Peso Arg.    BuenBit                $ 134.70770M      0.2    20    682ms
BTC/ARS           Bitcoin to Peso Arg.    Decrypto               $ 134.85895M      0.2    20    1.95s
BTC/ARS           Bitcoin to Peso Arg.    Lemoncash              $ 132.24382M      0.2    20    613ms
BTC/ARS           Bitcoin to Peso Arg.    belo.app               $ 135.44914M      0.2    20    1.26s
BTC/COP           Bitcoin to Peso Col.    BuenBit                $ 323.84841M      0.33   33.3  439ms
BTC/COP           Bitcoin to Peso Col.    Coinbase               $ 327.95854M      0.33   33.3  629ms
BTC/COP           Bitcoin to Peso Col.    buda.com               $ 326.25767M      0.33   33.3  115ms
BTC/USD     och   Bitcoin to Dollar       MOC onchain            $  89.32150K      1     100    1.84s
BTC/USD           Bitcoin to Dollar       Bitfinex               $  89.40900K      0.18   18    283ms
BTC/USD           Bitcoin to Dollar       Bitstamp               $  89.15800K      0.22   22    788ms
BTC/USD           Bitcoin to Dollar       Coinbase               $  89.30822K      0.25   25    885ms
BTC/USD           Bitcoin to Dollar       Gemini                 $  89.28400K      0.17   17    782ms
BTC/USD           Bitcoin to Dollar       Kraken                 $  89.23240K      0.18   18    207ms
BTC/USDT          Bitcoin to Tether       Binance                ₮  89.28220K      0.65   65    408ms
BTC/USDT          Bitcoin to Tether       Bybit                  ₮  89.27225K      0.1    10    425ms
BTC/USDT          Bitcoin to Tether       Huobi                  ₮  89.27200K      0.05    5    361ms
BTC/USDT          Bitcoin to Tether       KuCoin                 ₮  89.27785K      0.05    5    608ms
BTC/USDT          Bitcoin to Tether       OKX                    ₮  89.28095K      0.15   15    849ms
DOC/USD           Pegged 1:1 to USD       Dummy                  $   1.00000       1     100    <10ms
ETH/BTC           Ether to Bitcoin        Binance                ₿  33.68000m      0.25   25    411ms
ETH/BTC           Ether to Bitcoin        Bitfinex               ₿  33.70500m      0.25   25    400ms
ETH/BTC           Ether to Bitcoin        Bitstamp               ₿  33.70824m      0.25   25    349ms
ETH/BTC           Ether to Bitcoin        Kraken                 ₿  33.70000m      0.25   25    418ms
ETH/USD           Ether to Dollar         Bitfinex               $   3.01070K      0.18   18    256ms
ETH/USD           Ether to Dollar         Bitstamp               $   3.00290K      0.22   22    414ms
ETH/USD           Ether to Dollar         Coinbase               $   3.00936K      0.25   25    909ms
ETH/USD           Ether to Dollar         Gemini                 $   3.00234K      0.17   17    918ms
ETH/USD           Ether to Dollar         Kraken                 $   3.00232K      0.18   18    436ms
GAS/BTC           Rootstock gas price     RSK onchain            ₿  26.06560p      1     100    1.58s
MOC/BTC     sov   MOC to Bitcoin          Sovryn onchain         ₿ 415.62570p      1     100    832ms
MOC/USD     Oku   MOC to Dollar           Oku onchain            $  37.71208m      1     100    1.48s
RIF/BTC           RIF to Bitcoin          Binance                ₿ 380.00000p      1     100    415ms
RIF/USDT    MA    RIF to Tether           Binance                ₮  34.09864m      1     100    434ms
RIF/USDT    MA2   RIF to Tether           Binance                ₮  34.09046m      1     100    389ms
RIF/USDT    MA3   RIF to Tether           Binance                ₮  34.07906m      1     100    378ms
RIF/USDT    mp1%  To move the price 1%    Binance                ₮  43.14267K      1     100    386ms
RIF/USDT          RIF to Tether           Binance                ₮  34.00000m      1     100    397ms
USD/ARS     CCL   Dollar to Peso Arg.     Ambito.com             $   1.50678K      0.14   14.3  116ms
USD/ARS     CCL   Dollar to Peso Arg.     CoinMonitor.info       $   1.50804K      0.14   14.3  784ms
USD/ARS     CCL   Dollar to Peso Arg.     CriptoYa.com           $   1.50586K      0.14   14.3  1.13s
USD/ARS     CCL   Dollar to Peso Arg.     DolarHoy.com           $   1.50885K      0.14   14.3  472ms
USD/ARS     CCL   Dollar to Peso Arg.     InfoDolar.com          $   1.50716K      0.14   14.3  1.34s
USD/ARS     CCL   Dollar to Peso Arg.     Infobae                $   1.50901K      0.14   14.3  524ms
USD/ARS     CCL   Dollar to Peso Arg.     LaNacion.com.ar        $   1.50521K      0.14   14.3  259ms
USD/ARS           Dollar to Peso Arg.     Ambito.com             $   1.47500K      0.14   14.3  123ms
USD/ARS           Dollar to Peso Arg.     CoinMonitor.info       $   1.48500K      0.14   14.3  771ms
USD/ARS           Dollar to Peso Arg.     CriptoYa.com           $   1.47500K      0.14   14.3  1.10s
USD/ARS           Dollar to Peso Arg.     DolarHoy.com           $   1.47500K      0.14   14.3  532ms
USD/ARS           Dollar to Peso Arg.     InfoDolar.com          $   1.47500K      0.14   14.3  542ms
USD/ARS           Dollar to Peso Arg.     Infobae                $   1.48500K      0.14   14.3  522ms
USD/ARS           Dollar to Peso Arg.     LaNacion.com.ar        $   1.47500K      0.14   14.3  230ms
USD/COP           Dollar to Peso Col.     BanRep                 $   3.66598K      0.5    50    803ms
USD/COP           Dollar to Peso Col.     DolarHoy.co            $   3.66500K      0.5    50    773ms
USD/MXN           Dollar to Peso Mex.     Bitso.com              $  17.23000       0.1    10    3.30s
USD/MXN           Dollar to Peso Mex.     CitiBanamex            $  20.04275       0.1    10    471ms
USD/MXN           Dollar to Peso Mex.     Currency.me.uk         $  17.23810       0.1    10    3.60s
USD/MXN           Dollar to Peso Mex.     ElDolar.info           $  17.17950       0.1    10    783ms
USD/MXN           Dollar to Peso Mex.     ElEconomista.es        $  17.93300       0.1    10    1.87s
USD/MXN           Dollar to Peso Mex.     InfoDolar.com.mx       $  17.34000       0.1    10    2.08s
USD/MXN           Dollar to Peso Mex.     Intercam.com.mx        $  17.23125       0.1    10    985ms
USD/MXN           Dollar to Peso Mex.     TheMoneyConverter.com  $  17.23494       0.1    10    3.55s
USD/MXN           Dollar to Peso Mex.     Wise.com               $  17.23450       0.1    10    355ms
USD/MXN           Dollar to Peso Mex.     X-rates.com            $  17.23253       0.1    10    793ms
USDT/USD          Tether to Dollar        Bitstamp               $ 998.61000m      0.15   15    322ms
USDT/USD          Tether to Dollar        Coinbase               $ 998.73500m      0.35   35    644ms
USDT/USD          Tether to Dollar        Gemini                 $ 998.92500m      0.15   15    967ms
USDT/USD          Tether to Dollar        Kraken                 $ 998.66500m      0.35   35    506ms

    Coinpair                     Value   Sources count    Ok   Time
--  --------------  ------------------  ---------------  ----  ------
⇄   ARS/BPRO              6.112 × 10⁻⁹        N/A         ✓    <10ms
⇄   ARS/BTC               7.415 × 10⁻⁹        N/A         ✓    <10ms
⇄   ARS/USD(CCB)              0.000662        N/A         ✓    <10ms
⛓   BLOCK(RSK)                 8469815      1 of 1        ✓    1.47s
ƒ   BNB/USD                 902.148137        N/A         ✓    <10ms
↓   BNB/USDT                902.130000      1 of 1        ✓    411ms
ƒ   BPRO/ARS        163,616,986.595891        N/A         ✓    <10ms
⛓   BPRO/BTC                  1.213245      1 of 1        ✓    1.61s
ƒ   BPRO/COP        395,830,583.612631        N/A         ✓    <10ms
⇄   BPRO/MOC          1,967,128.023934        N/A         ✓    <10ms
ƒ   BPRO/USD            108,323.392530        N/A         ✓    <10ms
⇓   BTC/ARS         134,858,950.500000      5 of 5        ✓    1.95s
⇄   BTC/BPRO                  0.824236        N/A         ✓    <10ms
⇓   BTC/COP         326,257,671.605000      3 of 3        ✓    629ms
⇄   BTC/MOC           2,386,608.811140        N/A         ✓    <10ms
⇓   BTC/USD              89,284.000000      5 of 5        ✓    885ms
⛓   BTC/USD(och)         89,321.500000      1 of 1        ✓    1.84s
⇓   BTC/USDT             89,282.205000      5 of 5        ✓    849ms
⇄   COP/BPRO              2.526 × 10⁻⁹        N/A         ✓    <10ms
⇄   COP/BTC               3.065 × 10⁻⁹        N/A         ✓    <10ms
⇄   COP/USD(CCB)              0.000274        N/A         ✓    <10ms
=   DOC/USD                   1.000000      1 of 1        ✓    <10ms
⇓   ETH/BTC                   0.033704      4 of 4        ✓    418ms
⇓   ETH/USD               3,002.900000      5 of 5        ✓    918ms
ƒ   ETH/USD(B)            3,009.238650        N/A         ✓    <10ms
⛓   GAS/BTC              2.607 × 10⁻¹¹      1 of 1        ✓    1.58s
ƒ   MOC/BPRO                  0.000001        N/A         ✓    <10ms
ƒ   MOC/BTC               4.190 × 10⁻⁷        N/A         ✓    <10ms
⛓   MOC/BTC(sov)          4.156 × 10⁻⁷      1 of 1        ✓    832ms
ƒ   MOC/USD                   0.037109        N/A         ✓    <10ms
⛓   MOC/USD(Oku)              0.037712      1 of 1        ✓    1.48s
ƒ   MOC/USD(WM)               0.037410        N/A         ✓    <10ms
↓   RIF/BTC               3.800 × 10⁻⁷      1 of 1        ✓    415ms
ƒ   RIF/USD                   0.033928        N/A         ✓    <10ms
ƒ   RIF/USD(B)                0.033928        N/A         ✓    <10ms
ƒ   RIF/USD(T)                0.033957        N/A         ✓    <10ms
ƒ   RIF/USD(TB)               0.034001        N/A         ✓    <10ms
ƒ   RIF/USD(TBMA)             0.034099        N/A         ✓    <10ms
ƒ   RIF/USD(TMA)              0.034056        N/A         ✓    <10ms
ƒ   RIF/USD(WMTB)             0.033982        N/A         ✓    <10ms
↓   RIF/USDT                  0.034000      1 of 1        ✓    397ms
↓   RIF/USDT(MA)              0.034099      1 of 1        ✓    434ms
↓   RIF/USDT(MA2)             0.034090      1 of 1        ✓    389ms
↓   RIF/USDT(MA3)             0.034079      1 of 1        ✓    378ms
↓   RIF/USDT(mp1%)       43,142.669500      1 of 1        ✓    386ms
⇓   USD/ARS               1,475.000000      7 of 7        ✓    1.10s
ƒ   USD/ARS(CCB)          1,510.449246        N/A         ✓    <10ms
⇓   USD/ARS(CCL)          1,507.165000      7 of 7        ✓    1.34s
⇄   USD/BPRO                  0.000009        N/A         ✓    <10ms
⇄   USD/BTC                   0.000011        N/A         ✓    <10ms
⇓   USD/COP               3,665.488900      2 of 2        ✓    803ms
ƒ   USD/COP(CCB)          3,654.156082        N/A         ✓    <10ms
⇄   USD/MOC                  26.730532        N/A         ✓    <10ms
⇓   USD/MXN                  17.233514     10 of 10       ✓    3.60s
⇄   USDT/BTC                  0.000011        N/A         ✓    <10ms
⇓   USDT/USD                  0.998743      4 of 4        ✓    967ms
ƒ   USDT/USD(B)               1.000020        N/A         ✓    <10ms

Response time 3.94s

user@workstation:~$
```

