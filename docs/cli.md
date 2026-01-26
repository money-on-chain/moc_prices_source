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

Coinpair    V.    Short description     Exchnage     Response        Weight      %  Time
----------  ----  --------------------  -----------  ------------  --------  -----  ------
BTC/ARS           Bitcoin to Peso Arg.  Binance      $ 133.66059M      0.2    20    434ms
BTC/ARS           Bitcoin to Peso Arg.  BuenBit      $ 133.35912M      0.2    20    453ms
BTC/ARS           Bitcoin to Peso Arg.  Decrypto     $ 133.31318M      0.2    20    2.26s
BTC/ARS           Bitcoin to Peso Arg.  Lemoncash    $ 130.90154M      0.2    20    710ms
BTC/ARS           Bitcoin to Peso Arg.  belo.app     $ 134.02114M      0.2    20    371ms
BTC/COP           Bitcoin to Peso Col.  BuenBit      $ 319.46235M      0.33   33.3  694ms
BTC/COP           Bitcoin to Peso Col.  Coinbase     $ 322.62065M      0.33   33.3  845ms
BTC/COP           Bitcoin to Peso Col.  buda.com     $ 320.30450M      0.33   33.3  507ms
BTC/USD     och   Bitcoin to Dollar     MOC onchain  $  87.96490K      1     100    1.67s
BTC/USD           Bitcoin to Dollar     Bitfinex     $  88.04600K      0.18   18    281ms
BTC/USD           Bitcoin to Dollar     Bitstamp     $  87.89800K      0.22   22    380ms
BTC/USD           Bitcoin to Dollar     Coinbase     $  87.88300K      0.25   25    823ms
BTC/USD           Bitcoin to Dollar     Gemini       $  87.85822K      0.17   17    929ms
BTC/USD           Bitcoin to Dollar     Kraken       $  87.88000K      0.18   18    516ms
BTC/USDT          Bitcoin to Tether     Binance      ₮  87.99234K      0.65   65    449ms
BTC/USDT          Bitcoin to Tether     Bybit        ₮  87.99265K      0.1    10    505ms
BTC/USDT          Bitcoin to Tether     Huobi        ₮  87.98864K      0.05    5    692ms
BTC/USDT          Bitcoin to Tether     KuCoin       ₮  87.99235K      0.05    5    781ms
BTC/USDT          Bitcoin to Tether     OKX          ₮  87.99555K      0.15   15    757ms

    Coinpair                   Value   Sources count    Ok   Time
--  ------------  ------------------  ---------------  ----  ------
⇓   BTC/ARS       133,359,116.580000      5 of 5        ✓    2.26s
⇓   BTC/COP       320,304,500.500000      3 of 3        ✓    845ms
⇓   BTC/USD            87,882.995000      5 of 5        ✓    929ms
⛓   BTC/USD(och)       87,964.900000      1 of 1        ✓    1.67s
⇓   BTC/USDT           87,992.345000      5 of 5        ✓    781ms

Response time 2.29s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

Coinpair    V.    Short description       Exchnage               Response        Weight      %  Time
----------  ----  ----------------------  ---------------------  ------------  --------  -----  ------
BLOCK       RSK   Rootstock block number  RSK onchain            8462966           1     100    1.44s
BNB/USDT          BinanceCoin to Tether   Binance                ₮ 874.26000       1     100    382ms
BPRO/BTC          BPro to Bitcoin         MOC onchain            ₿   1.21198       1     100    1.50s
BTC/ARS           Bitcoin to Peso Arg.    Binance                $ 133.66059M      0.2    20    382ms
BTC/ARS           Bitcoin to Peso Arg.    BuenBit                $ 133.35912M      0.2    20    402ms
BTC/ARS           Bitcoin to Peso Arg.    Decrypto               $ 133.31318M      0.2    20    1.90s
BTC/ARS           Bitcoin to Peso Arg.    Lemoncash              $ 130.90154M      0.2    20    623ms
BTC/ARS           Bitcoin to Peso Arg.    belo.app               $ 134.02114M      0.2    20    271ms
BTC/COP           Bitcoin to Peso Col.    BuenBit                $ 319.46235M      0.33   33.3  431ms
BTC/COP           Bitcoin to Peso Col.    Coinbase               $ 322.62065M      0.33   33.3  820ms
BTC/COP           Bitcoin to Peso Col.    buda.com               $ 320.30450M      0.33   33.3  1.14s
BTC/USD     och   Bitcoin to Dollar       MOC onchain            $  87.96490K      1     100    1.46s
BTC/USD           Bitcoin to Dollar       Bitfinex               $  88.05600K      0.18   18    205ms
BTC/USD           Bitcoin to Dollar       Bitstamp               $  87.89700K      0.22   22    537ms
BTC/USD           Bitcoin to Dollar       Coinbase               $  87.87338K      0.25   25    798ms
BTC/USD           Bitcoin to Dollar       Gemini                 $  87.85822K      0.17   17    742ms
BTC/USD           Bitcoin to Dollar       Kraken                 $  87.88000K      0.18   18    426ms
BTC/USDT          Bitcoin to Tether       Binance                ₮  87.99234K      0.65   65    388ms
BTC/USDT          Bitcoin to Tether       Bybit                  ₮  87.99265K      0.1    10    434ms
BTC/USDT          Bitcoin to Tether       Huobi                  ₮  87.98864K      0.05    5    354ms
BTC/USDT          Bitcoin to Tether       KuCoin                 ₮  87.99235K      0.05    5    672ms
BTC/USDT          Bitcoin to Tether       OKX                    ₮  87.99555K      0.15   15    742ms
DOC/USD           Pegged 1:1 to USD       Dummy                  $   1.00000       1     100    <10ms
ETH/BTC           Ether to Bitcoin        Binance                ₿  33.23000m      0.25   25    382ms
ETH/BTC           Ether to Bitcoin        Bitfinex               ₿  33.23300m      0.25   25    429ms
ETH/BTC           Ether to Bitcoin        Bitstamp               ₿  33.24453m      0.25   25    330ms
ETH/BTC           Ether to Bitcoin        Kraken                 ₿  33.23000m      0.25   25    855ms
ETH/USD           Ether to Dollar         Bitfinex               $   2.92550K      0.18   18    890ms
ETH/USD           Ether to Dollar         Bitstamp               $   2.92072K      0.22   22    3.04s
ETH/USD           Ether to Dollar         Coinbase               $   2.92094K      0.25   25    486ms
ETH/USD           Ether to Dollar         Gemini                 $   2.92078K      0.17   17    747ms
ETH/USD           Ether to Dollar         Kraken                 $   2.92067K      0.18   18    430ms
GAS/BTC           Rootstock gas price     RSK onchain            ₿  26.06560p      1     100    1.46s
MOC/BTC     sov   MOC to Bitcoin          Sovryn onchain         ₿ 420.21618p      1     100    866ms
MOC/USD     Oku   MOC to Dollar           Oku onchain            $  37.04682m      1     100    1.55s
RIF/BTC           RIF to Bitcoin          Binance                ₿ 380.00000p      1     100    391ms
RIF/USDT    MA    RIF to Tether           Binance                ₮  37.33321m      1     100    397ms
RIF/USDT    MA2   RIF to Tether           Binance                ₮  37.31660m      1     100    386ms
RIF/USDT    MA3   RIF to Tether           Binance                ₮  37.31848m      1     100    371ms
RIF/USDT    mp1%  To move the price 1%    Binance                ₮  21.92392K      1     100    379ms
RIF/USDT          RIF to Tether           Binance                ₮  37.20000m      1     100    390ms
USD/ARS     CCL   Dollar to Peso Arg.     Ambito.com             $   1.51596K      0.14   14.3  312ms
USD/ARS     CCL   Dollar to Peso Arg.     CoinMonitor.info       $   1.51109K      0.14   14.3  771ms
USD/ARS     CCL   Dollar to Peso Arg.     CriptoYa.com           $   1.50786K      0.14   14.3  1.14s
USD/ARS     CCL   Dollar to Peso Arg.     DolarHoy.com           $   1.51575K      0.14   14.3  487ms
USD/ARS     CCL   Dollar to Peso Arg.     InfoDolar.com          $   1.51625K      0.14   14.3  740ms
USD/ARS     CCL   Dollar to Peso Arg.     Infobae                $   1.51924K      0.14   14.3  524ms
USD/ARS     CCL   Dollar to Peso Arg.     LaNacion.com.ar        $   1.51519K      0.14   14.3  482ms
USD/ARS           Dollar to Peso Arg.     Ambito.com             $   1.48000K      0.14   14.3  329ms
USD/ARS           Dollar to Peso Arg.     CoinMonitor.info       $   1.49000K      0.14   14.3  790ms
USD/ARS           Dollar to Peso Arg.     CriptoYa.com           $   1.48000K      0.14   14.3  134ms
USD/ARS           Dollar to Peso Arg.     DolarHoy.com           $   1.48000K      0.14   14.3  1.20s
USD/ARS           Dollar to Peso Arg.     InfoDolar.com          $   1.48000K      0.14   14.3  867ms
USD/ARS           Dollar to Peso Arg.     Infobae                $   1.49000K      0.14   14.3  504ms
USD/ARS           Dollar to Peso Arg.     LaNacion.com.ar        $   1.48000K      0.14   14.3  452ms
USD/COP           Dollar to Peso Col.     BanRep                 $   3.67615K      0.5    50    1.11s
USD/COP           Dollar to Peso Col.     DolarHoy.co            $   3.66000K      0.5    50    918ms
USD/MXN           Dollar to Peso Mex.     Bitso.com              $  17.36800       0.1    10    3.45s
USD/MXN           Dollar to Peso Mex.     CitiBanamex            $  20.04275       0.1    10    1.03s
USD/MXN           Dollar to Peso Mex.     Currency.me.uk         $  17.37360       0.1    10    1.71s
USD/MXN           Dollar to Peso Mex.     ElDolar.info           $  17.35470       0.1    10    750ms
USD/MXN           Dollar to Peso Mex.     ElEconomista.es        $  17.93300       0.1    10    736ms
USD/MXN           Dollar to Peso Mex.     InfoDolar.com.mx       $  17.42500       0.1    10    2.41s
USD/MXN           Dollar to Peso Mex.     Intercam.com.mx        $  17.37360       0.1    10    1.24s
USD/MXN           Dollar to Peso Mex.     TheMoneyConverter.com  $  17.37984       0.1    10    805ms
USD/MXN           Dollar to Peso Mex.     Wise.com               $  17.36650       0.1    10    564ms
USD/MXN           Dollar to Peso Mex.     X-rates.com            $  17.36595       0.1    10    873ms
USDT/USD          Tether to Dollar        Bitstamp               $ 998.92500m      0.15   15    815ms
USDT/USD          Tether to Dollar        Coinbase               $ 999.08000m      0.35   35    691ms
USDT/USD          Tether to Dollar        Gemini                 $ 998.83500m      0.15   15    732ms
USDT/USD          Tether to Dollar        Kraken                 $ 998.95500m      0.35   35    248ms

    Coinpair                     Value   Sources count    Ok   Time
--  --------------  ------------------  ---------------  ----  ------
⛓   BLOCK(RSK)                 8462966      1 of 1        ✓    1.44s
ƒ   BNB/USD                 873.143781        N/A         ✓    <10ms
↓   BNB/USDT                874.260000      1 of 1        ✓    382ms
ƒ   BPRO/ARS        161,628,127.810570        N/A         ✓    <10ms
⛓   BPRO/BTC                  1.211977      1 of 1        ✓    1.50s
ƒ   BPRO/COP        388,201,557.364536        N/A         ✓    <10ms
ƒ   BPRO/USD            106,508.503027        N/A         ✓    <10ms
⇓   BTC/ARS         133,359,116.580000      5 of 5        ✓    1.90s
⇓   BTC/COP         320,304,500.500000      3 of 3        ✓    1.14s
⇓   BTC/USD              87,880.000000      5 of 5        ✓    798ms
⛓   BTC/USD(och)         87,964.900000      1 of 1        ✓    1.46s
⇓   BTC/USDT             87,992.345000      5 of 5        ✓    742ms
=   DOC/USD                   1.000000      1 of 1        ✓    <10ms
⇓   ETH/BTC                   0.033237      4 of 4        ✓    855ms
⇓   ETH/USD               2,920.780000      5 of 5        ✓    3.04s
ƒ   ETH/USD(B)            2,920.890848        N/A         ✓    <10ms
⛓   GAS/BTC              2.607 × 10⁻¹¹      1 of 1        ✓    1.46s
ƒ   MOC/BPRO                  0.000001        N/A         ✓    <10ms
ƒ   MOC/BTC               4.209 × 10⁻⁷        N/A         ✓    <10ms
⛓   MOC/BTC(sov)          4.202 × 10⁻⁷      1 of 1        ✓    866ms
ƒ   MOC/USD                   0.036929        N/A         ✓    <10ms
⛓   MOC/USD(Oku)              0.037047      1 of 1        ✓    1.55s
ƒ   MOC/USD(WM)               0.036988        N/A         ✓    <10ms
↓   RIF/BTC               3.800 × 10⁻⁷      1 of 1        ✓    391ms
ƒ   RIF/USD                   0.033394        N/A         ✓    <10ms
ƒ   RIF/USD(B)                0.033394        N/A         ✓    <10ms
ƒ   RIF/USD(T)                0.037160        N/A         ✓    <10ms
ƒ   RIF/USD(TB)               0.037153        N/A         ✓    <10ms
ƒ   RIF/USD(TBMA)             0.037286        N/A         ✓    <10ms
ƒ   RIF/USD(TMA)              0.037293        N/A         ✓    <10ms
ƒ   RIF/USD(WMTB)             0.036213        N/A         ✓    <10ms
↓   RIF/USDT                  0.037200      1 of 1        ✓    390ms
↓   RIF/USDT(MA)              0.037333      1 of 1        ✓    397ms
↓   RIF/USDT(MA2)             0.037317      1 of 1        ✓    386ms
↓   RIF/USDT(MA3)             0.037318      1 of 1        ✓    371ms
↓   RIF/USDT(mp1%)       21,923.923400      1 of 1        ✓    379ms
⇓   USD/ARS               1,480.000000      7 of 7        ✓    1.20s
ƒ   USD/ARS(CCB)          1,517.513844        N/A         ✓    <10ms
⇓   USD/ARS(CCL)          1,515.750000      7 of 7        ✓    1.14s
⇓   USD/COP               3,668.076850      2 of 2        ✓    1.11s
ƒ   USD/COP(CCB)          3,644.794043        N/A         ✓    <10ms
⇓   USD/MXN                  17.373600     10 of 10       ✓    3.45s
⇓   USDT/USD                  0.998919      4 of 4        ✓    815ms
ƒ   USDT/USD(B)               0.998723        N/A         ✓    <10ms

Response time 3.55s

user@workstation:~$
```

