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
BPRO/BTC          BPro to Bitcoin       MOC onchain     ₿   1.21298       1     100    1.73s
BTC/ARS           Bitcoin to Peso Arg.  Binance         $ 134.78322M      0.2    20    410ms
BTC/ARS           Bitcoin to Peso Arg.  BuenBit         $ 134.25266M      0.2    20    447ms
BTC/ARS           Bitcoin to Peso Arg.  Decrypto        $ 134.68464M      0.2    20    2.07s
BTC/ARS           Bitcoin to Peso Arg.  Lemoncash       $ 132.03921M      0.2    20    695ms
BTC/ARS           Bitcoin to Peso Arg.  belo.app        $ 135.13044M      0.2    20    7.44s
BTC/COP           Bitcoin to Peso Col.  BuenBit         $ 322.76335M      0.33   33.3  465ms
BTC/COP           Bitcoin to Peso Col.  Coinbase        $ 326.54534M      0.33   33.3  862ms
BTC/COP           Bitcoin to Peso Col.  buda.com        $ 324.24950M      0.33   33.3  319ms
BTC/USD     och   Bitcoin to Dollar     MOC onchain     $  89.08900K      1     100    1.71s
BTC/USD           Bitcoin to Dollar     Bitfinex        $  89.14600K      0.18   18    240ms
BTC/USD           Bitcoin to Dollar     Bitstamp        $  89.02100K      0.22   22    830ms
BTC/USD           Bitcoin to Dollar     Coinbase        $  89.00637K      0.25   25    323ms
BTC/USD           Bitcoin to Dollar     Gemini          $  89.02257K      0.17   17    977ms
BTC/USD           Bitcoin to Dollar     Kraken          $  89.01450K      0.18   18    221ms
BTC/USDT          Bitcoin to Tether     Binance         ₮  89.16000K      0.65   65    425ms
BTC/USDT          Bitcoin to Tether     Bybit           ₮  89.15895K      0.1    10    520ms
BTC/USDT          Bitcoin to Tether     Huobi           ₮  89.17128K      0.05    5    459ms
BTC/USDT          Bitcoin to Tether     KuCoin          ₮  89.15995K      0.05    5    820ms
BTC/USDT          Bitcoin to Tether     OKX             ₮  89.16745K      0.15   15    1.24s
MOC/BTC     sov   MOC to Bitcoin        Sovryn onchain  ₿ 415.62570p      1     100    881ms
MOC/USD     Oku   MOC to Dollar         Oku onchain     $  37.66684m      1     100    1.73s

    Coinpair                   Value   Sources count    Ok   Time
--  ------------  ------------------  ---------------  ----  ------
⛓   BPRO/BTC                1.212985      1 of 1        ✓    1.73s
⇓   BTC/ARS       134,684,638.800000      5 of 5        ✓    7.44s
⇄   BTC/BPRO                0.824413        N/A         ✓    <10ms
⇓   BTC/COP       324,249,499.605000      3 of 3        ✓    862ms
⇄   BTC/MOC         2,384,504.091050        N/A         ✓    <10ms
⇓   BTC/USD            89,021.000000      5 of 5        ✓    977ms
ƒ   BTC/USD(24h)             ▼ 0.18%        N/A         ✓    2.76s
⛓   BTC/USD(och)       89,089.000000      1 of 1        ✓    1.71s
⇓   BTC/USDT           89,159.995000      5 of 5        ✓    1.24s
⛓   MOC/BTC(sov)        4.156 × 10⁻⁷      1 of 1        ✓    881ms
⛓   MOC/USD(Oku)            0.037667      1 of 1        ✓    1.73s

Response time 10.21s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

Coinpair    V.    Short description       Exchnage               Response        Weight      %  Time
----------  ----  ----------------------  ---------------------  ------------  --------  -----  ------
BLOCK       RSK   Rootstock block number  RSK onchain            8470325           1     100    1.50s
BNB/USDT          BinanceCoin to Tether   Binance                ₮ 903.06000       1     100    415ms
BPRO/BTC          BPro to Bitcoin         MOC onchain            ₿   1.21298       1     100    1.52s
BTC/ARS           Bitcoin to Peso Arg.    Binance                $ 134.78322M      0.2    20    417ms
BTC/ARS           Bitcoin to Peso Arg.    BuenBit                $ 134.28933M      0.2    20    682ms
BTC/ARS           Bitcoin to Peso Arg.    Decrypto               $ 134.67437M      0.2    20    1.88s
BTC/ARS           Bitcoin to Peso Arg.    Lemoncash              $ 132.03897M      0.2    20    600ms
BTC/ARS           Bitcoin to Peso Arg.    belo.app               $ 135.13044M      0.2    20    7.46s
BTC/COP           Bitcoin to Peso Col.    BuenBit                $ 322.76335M      0.33   33.3  428ms
BTC/COP           Bitcoin to Peso Col.    Coinbase               $ 326.58210M      0.33   33.3  863ms
BTC/COP           Bitcoin to Peso Col.    buda.com               $ 324.24950M      0.33   33.3  302ms
BTC/USD     och   Bitcoin to Dollar       MOC onchain            $  89.08900K      1     100    1.50s
BTC/USD           Bitcoin to Dollar       Bitfinex               $  89.15800K      0.18   18    249ms
BTC/USD           Bitcoin to Dollar       Bitstamp               $  89.02100K      0.22   22    365ms
BTC/USD           Bitcoin to Dollar       Coinbase               $  89.01576K      0.25   25    839ms
BTC/USD           Bitcoin to Dollar       Gemini                 $  89.01634K      0.17   17    755ms
BTC/USD           Bitcoin to Dollar       Kraken                 $  89.01450K      0.18   18    291ms
BTC/USDT          Bitcoin to Tether       Binance                ₮  89.15930K      0.65   65    395ms
BTC/USDT          Bitcoin to Tether       Bybit                  ₮  89.15195K      0.1    10    428ms
BTC/USDT          Bitcoin to Tether       Huobi                  ₮  89.16003K      0.05    5    351ms
BTC/USDT          Bitcoin to Tether       KuCoin                 ₮  89.15995K      0.05    5    695ms
BTC/USDT          Bitcoin to Tether       OKX                    ₮  89.15805K      0.15   15    1.18s
DOC/USD           Pegged 1:1 to USD       Dummy                  $   1.00000       1     100    <10ms
ETH/BTC           Ether to Bitcoin        Binance                ₿  33.77000m      0.25   25    422ms
ETH/BTC           Ether to Bitcoin        Bitfinex               ₿  33.77900m      0.25   25    446ms
ETH/BTC           Ether to Bitcoin        Bitstamp               ₿  33.81860m      0.25   25    367ms
ETH/BTC           Ether to Bitcoin        Kraken                 ₿  33.78000m      0.25   25    422ms
ETH/USD           Ether to Dollar         Bitfinex               $   3.01130K      0.18   18    256ms
ETH/USD           Ether to Dollar         Bitstamp               $   3.00697K      0.22   22    350ms
ETH/USD           Ether to Dollar         Coinbase               $   3.00696K      0.25   25    867ms
ETH/USD           Ether to Dollar         Gemini                 $   3.00721K      0.17   17    730ms
ETH/USD           Ether to Dollar         Kraken                 $   3.00705K      0.18   18    451ms
GAS/BTC           Rootstock gas price     RSK onchain            ₿  26.06560p      1     100    1.51s
MOC/BTC     sov   MOC to Bitcoin          Sovryn onchain         ₿ 415.62570p      1     100    794ms
MOC/USD     Oku   MOC to Dollar           Oku onchain            $  37.66684m      1     100    1.54s
RIF/BTC           RIF to Bitcoin          Binance                ₿ 380.00000p      1     100    424ms
RIF/USDT    MA    RIF to Tether           Binance                ₮  33.70209m      1     100    396ms
RIF/USDT    MA2   RIF to Tether           Binance                ₮  33.70104m      1     100    402ms
RIF/USDT    MA3   RIF to Tether           Binance                ₮  33.70107m      1     100    413ms
RIF/USDT    mp1%  To move the price 1%    Binance                ₮  56.19620K      1     100    364ms
RIF/USDT          RIF to Tether           Binance                ₮  33.80000m      1     100    390ms
USD/ARS     CCL   Dollar to Peso Arg.     Ambito.com             $   1.49740K      0.14   14.3  287ms
USD/ARS     CCL   Dollar to Peso Arg.     CoinMonitor.info       $   1.49762K      0.14   14.3  766ms
USD/ARS     CCL   Dollar to Peso Arg.     CriptoYa.com           $   1.51218K      0.14   14.3  255ms
USD/ARS     CCL   Dollar to Peso Arg.     DolarHoy.com           $   1.50850K      0.14   14.3  278ms
USD/ARS     CCL   Dollar to Peso Arg.     InfoDolar.com          $   1.50764K      0.14   14.3  477ms
USD/ARS     CCL   Dollar to Peso Arg.     Infobae                $   1.51039K      0.14   14.3  499ms
USD/ARS     CCL   Dollar to Peso Arg.     LaNacion.com.ar        $   1.52363K      0.14   14.3  166ms
USD/ARS           Dollar to Peso Arg.     Ambito.com             $   1.47500K      0.14   14.3  189ms
USD/ARS           Dollar to Peso Arg.     CoinMonitor.info       $   1.48500K      0.14   14.3  755ms
USD/ARS           Dollar to Peso Arg.     CriptoYa.com           $   1.47500K      0.14   14.3  256ms
USD/ARS           Dollar to Peso Arg.     DolarHoy.com           $   1.47500K      0.14   14.3  1.16s
USD/ARS           Dollar to Peso Arg.     InfoDolar.com          $   1.47500K      0.14   14.3  1.33s
USD/ARS           Dollar to Peso Arg.     Infobae                $   1.48500K      0.14   14.3  480ms
USD/ARS           Dollar to Peso Arg.     LaNacion.com.ar        $   1.47500K      0.14   14.3  175ms
USD/COP           Dollar to Peso Col.     BanRep                 $   3.66598K      0.5    50    911ms
USD/COP           Dollar to Peso Col.     DolarHoy.co            $   3.66500K      0.5    50    1.82s
USD/MXN           Dollar to Peso Mex.     Bitso.com              $  17.18600       0.1    10    337ms
USD/MXN           Dollar to Peso Mex.     CitiBanamex            $  20.04275       0.1    10    961ms
USD/MXN           Dollar to Peso Mex.     Currency.me.uk         $  17.20320       0.1    10    3.82s
USD/MXN           Dollar to Peso Mex.     ElDolar.info           $  17.16670       0.1    10    484ms
USD/MXN           Dollar to Peso Mex.     ElEconomista.es        $  17.93300       0.1    10    411ms
USD/MXN           Dollar to Peso Mex.     InfoDolar.com.mx       $  17.33500       0.1    10    2.23s
USD/MXN           Dollar to Peso Mex.     Intercam.com.mx        $  17.20550       0.1    10    1.06s
USD/MXN           Dollar to Peso Mex.     TheMoneyConverter.com  $  17.20440       0.1    10    1.45s
USD/MXN           Dollar to Peso Mex.     Wise.com               $  17.20720       0.1    10    415ms
USD/MXN           Dollar to Peso Mex.     X-rates.com            $  17.20650       0.1    10    838ms
USDT/USD          Tether to Dollar        Bitstamp               $ 998.48000m      0.15   15    783ms
USDT/USD          Tether to Dollar        Coinbase               $ 998.37500m      0.35   35    663ms
USDT/USD          Tether to Dollar        Gemini                 $ 999.12000m      0.15   15    751ms
USDT/USD          Tether to Dollar        Kraken                 $ 998.41500m      0.35   35    457ms

    Coinpair                     Value   Sources count    Ok   Time
--  --------------  ------------------  ---------------  ----  ------
⇄   ARS/BPRO              6.122 × 10⁻⁹        N/A         ✓    <10ms
⇄   ARS/BTC               7.425 × 10⁻⁹        N/A         ✓    <10ms
⇄   ARS/USD(CCB)              0.000661        N/A         ✓    <10ms
⛓   BLOCK(RSK)                 8470325      1 of 1        ✓    1.50s
ƒ   BNB/USD                 901.612064        N/A         ✓    <10ms
↓   BNB/USDT                903.060000      1 of 1        ✓    415ms
ƒ   BPRO/ARS        163,357,933.216543        N/A         ✓    <10ms
⛓   BPRO/BTC                  1.212985      1 of 1        ✓    1.52s
ƒ   BPRO/COP        393,309,646.604409        N/A         ✓    <10ms
⇄   BPRO/MOC          1,965,763.726194        N/A         ✓    <10ms
ƒ   BPRO/USD            107,975.449268        N/A         ✓    <10ms
⇓   BTC/ARS         134,674,367.400000      5 of 5        ✓    7.46s
⇄   BTC/BPRO                  0.824413        N/A         ✓    <10ms
⇓   BTC/COP         324,249,498.055000      3 of 3        ✓    863ms
⇄   BTC/MOC           2,384,441.120480        N/A         ✓    <10ms
⇓   BTC/USD              89,016.340000      5 of 5        ✓    839ms
ƒ   BTC/USD(24h)               ▼ 0.18%        N/A         ✓    2.79s
⛓   BTC/USD(och)         89,089.000000      1 of 1        ✓    1.50s
⇓   BTC/USDT             89,159.295000      5 of 5        ✓    1.18s
⇄   COP/BPRO              2.543 × 10⁻⁹        N/A         ✓    <10ms
⇄   COP/BTC               3.084 × 10⁻⁹        N/A         ✓    <10ms
⇄   COP/USD(CCB)              0.000275        N/A         ✓    <10ms
=   DOC/USD                   1.000000      1 of 1        ✓    <10ms
⇓   ETH/BTC                   0.033799      4 of 4        ✓    446ms
⇓   ETH/USD               3,007.050000      5 of 5        ✓    867ms
ƒ   ETH/USD(B)            3,008.645472        N/A         ✓    <10ms
⛓   GAS/BTC              2.607 × 10⁻¹¹      1 of 1        ✓    1.51s
ƒ   MOC/BPRO                  0.000001        N/A         ✓    <10ms
ƒ   MOC/BTC               4.194 × 10⁻⁷        N/A         ✓    <10ms
⛓   MOC/BTC(sov)          4.156 × 10⁻⁷      1 of 1        ✓    794ms
ƒ   MOC/USD                   0.036997        N/A         ✓    <10ms
⛓   MOC/USD(Oku)              0.037667      1 of 1        ✓    1.54s
ƒ   MOC/USD(WM)               0.037332        N/A         ✓    <10ms
↓   RIF/BTC               3.800 × 10⁻⁷      1 of 1        ✓    424ms
ƒ   RIF/USD                   0.033826        N/A         ✓    <10ms
ƒ   RIF/USD(B)                0.033826        N/A         ✓    <10ms
ƒ   RIF/USD(T)                0.033754        N/A         ✓    <10ms
ƒ   RIF/USD(TB)               0.033746        N/A         ✓    <10ms
ƒ   RIF/USD(TBMA)             0.033648        N/A         ✓    <10ms
ƒ   RIF/USD(TMA)              0.033656        N/A         ✓    <10ms
ƒ   RIF/USD(WMTB)             0.033766        N/A         ✓    1.87s
↓   RIF/USDT                  0.033800      1 of 1        ✓    390ms
↓   RIF/USDT(MA)              0.033702      1 of 1        ✓    396ms
↓   RIF/USDT(MA2)             0.033701      1 of 1        ✓    402ms
↓   RIF/USDT(MA3)             0.033701      1 of 1        ✓    413ms
↓   RIF/USDT(mp1%)       56,196.200600      1 of 1        ✓    364ms
⇓   USD/ARS               1,475.000000      7 of 7        ✓    1.33s
ƒ   USD/ARS(CCB)          1,512.917374        N/A         ✓    <10ms
⇓   USD/ARS(CCL)          1,508.500000      7 of 7        ✓    766ms
⇄   USD/BPRO                  0.000009        N/A         ✓    <10ms
⇄   USD/BTC                   0.000011        N/A         ✓    <10ms
⇓   USD/COP               3,665.488900      2 of 2        ✓    1.82s
ƒ   USD/COP(CCB)          3,642.584025        N/A         ✓    <10ms
⇄   USD/MOC                  26.786555        N/A         ✓    <10ms
⇓   USD/MXN                  17.204350     10 of 10       ✓    3.82s
⇄   USDT/BTC                  0.000011        N/A         ✓    <10ms
⇓   USDT/USD                  0.998626      4 of 4        ✓    783ms
ƒ   USDT/USD(B)               0.998397        N/A         ✓    <10ms

Response time 10.28s

user@workstation:~$
```

