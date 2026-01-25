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

Coinpair    V.    Short description     Exchnage    Response        Weight     %  Time
----------  ----  --------------------  ----------  ------------  --------  ----  ------
BTC/ARS           Bitcoin to Peso Arg.  Binance     $ 135.35722M      0.2   20    358ms
BTC/ARS           Bitcoin to Peso Arg.  BuenBit     $ 134.17240M      0.2   20    405ms
BTC/ARS           Bitcoin to Peso Arg.  Decrypto    $ 134.77304M      0.2   20    1.97s
BTC/ARS           Bitcoin to Peso Arg.  Lemoncash   $ 131.73549M      0.2   20    628ms
BTC/ARS           Bitcoin to Peso Arg.  belo.app    $ 135.49156M      0.2   20    254ms
BTC/COP           Bitcoin to Peso Col.  BuenBit     $ 318.24092M      0.33  33.3  667ms
BTC/COP           Bitcoin to Peso Col.  Coinbase    $ 321.34918M      0.33  33.3  626ms
BTC/COP           Bitcoin to Peso Col.  buda.com    $ 322.04446M      0.33  33.3  1.35s
BTC/USD           Bitcoin to Dollar     Bitfinex    $  88.92300K      0.18  18    259ms
BTC/USD           Bitcoin to Dollar     Bitstamp    $  88.82200K      0.22  22    329ms
BTC/USD           Bitcoin to Dollar     Coinbase    $  88.81998K      0.25  25    575ms
BTC/USD           Bitcoin to Dollar     Gemini      $  88.82401K      0.17  17    806ms
BTC/USD           Bitcoin to Dollar     Kraken      $  88.82460K      0.18  18    232ms
BTC/USDT          Bitcoin to Tether     Binance     ₮  88.95776K      0.65  65    344ms
BTC/USDT          Bitcoin to Tether     Bybit       ₮  88.96945K      0.1   10    459ms
BTC/USDT          Bitcoin to Tether     Huobi       ₮  88.97126K      0.05   5    613ms
BTC/USDT          Bitcoin to Tether     KuCoin      ₮  88.96655K      0.05   5    846ms
BTC/USDT          Bitcoin to Tether     OKX         ₮  88.95905K      0.15  15    785ms

    Coinpair                 Value   Sources count    Ok   Time
--  ----------  ------------------  ---------------  ----  ------
↓   BTC/ARS     134,773,036.500000      5 of 5        ✓    1.97s
↓   BTC/COP     321,349,176.833012      3 of 3        ✓    1.35s
↓   BTC/USD          88,824.010000      5 of 5        ✓    806ms
↓   BTC/USDT         88,957.755000      5 of 5        ✓    846ms

Response time 1.98s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

Coinpair    V.    Short description       Exchnage               Response        Weight      %  Time
----------  ----  ----------------------  ---------------------  ------------  --------  -----  ------
BLOCK       RSK   Rootstock block number  RSK onchain            8457171           1     100    1.50s
BNB/USDT          BinanceCoin to Tether   Binance                ₮ 882.04000       1     100    410ms
BPRO/BTC          BPro to Bitcoin         MOC onchain            ₿   1.21288       1     100    1.54s
BTC/ARS           Bitcoin to Peso Arg.    Binance                $ 135.35722M      0.2    20    371ms
BTC/ARS           Bitcoin to Peso Arg.    BuenBit                $ 134.17237M      0.2    20    411ms
BTC/ARS           Bitcoin to Peso Arg.    Decrypto               $ 134.77288M      0.2    20    1.91s
BTC/ARS           Bitcoin to Peso Arg.    Lemoncash              $ 131.73546M      0.2    20    600ms
BTC/ARS           Bitcoin to Peso Arg.    belo.app               $ 135.49156M      0.2    20    281ms
BTC/COP           Bitcoin to Peso Col.    BuenBit                $ 318.24092M      0.33   33.3  413ms
BTC/COP           Bitcoin to Peso Col.    Coinbase               $ 321.34918M      0.33   33.3  648ms
BTC/COP           Bitcoin to Peso Col.    buda.com               $ 322.04446M      0.33   33.3  125ms
BTC/USD           Bitcoin to Dollar       Bitfinex               $  88.92300K      0.18   18    195ms
BTC/USD           Bitcoin to Dollar       Bitstamp               $  88.82200K      0.22   22    317ms
BTC/USD           Bitcoin to Dollar       Coinbase               $  88.81998K      0.25   25    584ms
BTC/USD           Bitcoin to Dollar       Gemini                 $  88.82401K      0.17   17    776ms
BTC/USD           Bitcoin to Dollar       Kraken                 $  88.82460K      0.18   18    253ms
BTC/USDT          Bitcoin to Tether       Binance                ₮  88.95774K      0.65   65    385ms
BTC/USDT          Bitcoin to Tether       Bybit                  ₮  88.96945K      0.1    10    428ms
BTC/USDT          Bitcoin to Tether       Huobi                  ₮  88.97126K      0.05    5    364ms
BTC/USDT          Bitcoin to Tether       KuCoin                 ₮  88.96655K      0.05    5    397ms
BTC/USDT          Bitcoin to Tether       OKX                    ₮  88.95905K      0.15   15    818ms
DOC/USD           Pegged 1:1 to USD       Dummy                  $   1.00000       1     100    <10ms
ETH/BTC           Ether to Bitcoin        Binance                ₿  33.07000m      0.25   25    381ms
ETH/BTC           Ether to Bitcoin        Bitfinex               ₿  33.06400m      0.25   25    375ms
ETH/BTC           Ether to Bitcoin        Bitstamp               ₿  33.07515m      0.25   25    759ms
ETH/BTC           Ether to Bitcoin        Kraken                 ₿  33.07000m      0.25   25    826ms
ETH/USD           Ether to Dollar         Bitfinex               $   2.94090K      0.18   18    392ms
ETH/USD           Ether to Dollar         Bitstamp               $   2.93735K      0.22   22    310ms
ETH/USD           Ether to Dollar         Coinbase               $   2.93762K      0.25   25    629ms
ETH/USD           Ether to Dollar         Gemini                 $   2.93793K      0.17   17    789ms
ETH/USD           Ether to Dollar         Kraken                 $   2.93749K      0.18   18    477ms
GAS/BTC           Rootstock gas price     RSK onchain            ₿  26.06560p      1     100    1.47s
MOC/BTC     sov   MOC to Bitcoin          Sovryn onchain         ₿ 420.21618p      1     100    890ms
MOC/USD     Oku   MOC to Dollar           Oku onchain            $  37.40610m      1     100    1.49s
RIF/BTC           RIF to Bitcoin          Binance                ₿ 380.00000p      1     100    382ms
RIF/USDT    MA    RIF to Tether           Binance                ₮  38.75000m      1     100    383ms
RIF/USDT    MA2   RIF to Tether           Binance                ₮  38.74638m      1     100    407ms
RIF/USDT    MA3   RIF to Tether           Binance                ₮  38.74445m      1     100    411ms
RIF/USDT    mp1%  To move the price 1%    Binance                ₮  55.65613K      1     100    332ms
RIF/USDT          RIF to Tether           Binance                ₮  38.70000m      1     100    370ms
USD/ARS     CCL   Dollar to Peso Arg.     Ambito.com             $   1.50736K      0.14   14.3  181ms
USD/ARS     CCL   Dollar to Peso Arg.     CoinMonitor.info       $   1.50759K      0.14   14.3  802ms
USD/ARS     CCL   Dollar to Peso Arg.     CriptoYa.com           $   1.49746K      0.14   14.3  3.17s
USD/ARS     CCL   Dollar to Peso Arg.     DolarHoy.com           $   1.51095K      0.14   14.3  3.23s
USD/ARS     CCL   Dollar to Peso Arg.     InfoDolar.com          $   1.51552K      0.14   14.3  481ms
USD/ARS     CCL   Dollar to Peso Arg.     Infobae                $   1.51085K      0.14   14.3  932ms
USD/ARS     CCL   Dollar to Peso Arg.     LaNacion.com.ar        $   1.48833K      0.14   14.3  192ms
USD/ARS           Dollar to Peso Arg.     Ambito.com             $   1.47500K      0.14   14.3  221ms
USD/ARS           Dollar to Peso Arg.     CoinMonitor.info       $   1.48500K      0.14   14.3  743ms
USD/ARS           Dollar to Peso Arg.     CriptoYa.com           $   1.47500K      0.14   14.3  122ms
USD/ARS           Dollar to Peso Arg.     DolarHoy.com           $   1.47500K      0.14   14.3  227ms
USD/ARS           Dollar to Peso Arg.     InfoDolar.com          $   1.47500K      0.14   14.3  557ms
USD/ARS           Dollar to Peso Arg.     Infobae                $   1.48500K      0.14   14.3  878ms
USD/ARS           Dollar to Peso Arg.     LaNacion.com.ar        $   1.47500K      0.14   14.3  145ms
USD/COP           Dollar to Peso Col.     BanRep                 $   3.63816K      0.5    50    947ms
USD/COP           Dollar to Peso Col.     DolarHoy.co            $   3.66000K      0.5    50    766ms
USD/MXN           Dollar to Peso Mex.     Bitso.com              $  17.40500       0.1    10    272ms
USD/MXN           Dollar to Peso Mex.     CitiBanamex            $  20.04275       0.1    10    910ms
USD/MXN           Dollar to Peso Mex.     Currency.me.uk         $  17.36310       0.1    10    602ms
USD/MXN           Dollar to Peso Mex.     ElDolar.info           $  17.35210       0.1    10    1.54s
USD/MXN           Dollar to Peso Mex.     ElEconomista.es        $  17.93300       0.1    10    178ms
USD/MXN           Dollar to Peso Mex.     InfoDolar.com.mx       $  17.45500       0.1    10    1.13s
USD/MXN           Dollar to Peso Mex.     Intercam.com.mx        $  17.36115       0.1    10    614ms
USD/MXN           Dollar to Peso Mex.     TheMoneyConverter.com  $  17.37432       0.1    10    467ms
USD/MXN           Dollar to Peso Mex.     Wise.com               $  17.36570       0.1    10    354ms
USD/MXN           Dollar to Peso Mex.     X-rates.com            $  17.36328       0.1    10    773ms
USDT/USD          Tether to Dollar        Bitstamp               $ 998.36500m      0.15   15    321ms
USDT/USD          Tether to Dollar        Coinbase               $ 998.47000m      0.35   35    488ms
USDT/USD          Tether to Dollar        Gemini                 $ 998.34500m      0.15   15    751ms
USDT/USD          Tether to Dollar        Kraken                 $ 998.42500m      0.35   35    356ms

    Coinpair                     Value   Sources count    Ok   Time
--  --------------  ------------------  ---------------  ----  ------
↓   BLOCK(RSK)                 8457171      1 of 1        ✓    1.50s
ƒ   BNB/USD                 880.714080        N/A         ✓    <10ms
↓   BNB/USDT                882.040000      1 of 1        ✓    410ms
ƒ   BPRO/ARS        163,463,862.088727        N/A         ✓    <10ms
↓   BPRO/BTC                  1.212884      1 of 1        ✓    1.54s
ƒ   BPRO/COP        389,759,242.181077        N/A         ✓    <10ms
ƒ   BPRO/USD            107,733.211475        N/A         ✓    <10ms
↓   BTC/ARS         134,772,885.000000      5 of 5        ✓    1.91s
↓   BTC/COP         321,349,176.833012      3 of 3        ✓    648ms
↓   BTC/USD              88,824.010000      5 of 5        ✓    776ms
↓   BTC/USDT             88,957.735000      5 of 5        ✓    818ms
↓   DOC/USD                   1.000000      1 of 1        ✓    <10ms
↓   ETH/BTC                   0.033067      4 of 4        ✓    826ms
↓   ETH/USD               2,937.615000      5 of 5        ✓    789ms
ƒ   ETH/USD(B)            2,937.143539        N/A         ✓    <10ms
↓   GAS/BTC              2.607 × 10⁻¹¹      1 of 1        ✓    1.47s
ƒ   MOC/BPRO                  0.000001        N/A         ✓    <10ms
ƒ   MOC/BTC               4.207 × 10⁻⁷        N/A         ✓    <10ms
↓   MOC/BTC(sov)          4.202 × 10⁻⁷      1 of 1        ✓    890ms
ƒ   MOC/USD                   0.037325        N/A         ✓    <10ms
↓   MOC/USD(Oku)              0.037406      1 of 1        ✓    1.49s
ƒ   MOC/USD(WM)               0.037366        N/A         ✓    <10ms
↓   RIF/BTC               3.800 × 10⁻⁷      1 of 1        ✓    382ms
ƒ   RIF/USD                   0.033753        N/A         ✓    <10ms
ƒ   RIF/USD(B)                0.033753        N/A         ✓    <10ms
ƒ   RIF/USD(T)                0.038638        N/A         ✓    <10ms
ƒ   RIF/USD(TB)               0.038642        N/A         ✓    <10ms
ƒ   RIF/USD(TBMA)             0.038692        N/A         ✓    <10ms
ƒ   RIF/USD(TMA)              0.038688        N/A         ✓    <10ms
ƒ   RIF/USD(WMTB)             0.037420        N/A         ✓    <10ms
↓   RIF/USDT                  0.038700      1 of 1        ✓    370ms
↓   RIF/USDT(MA)              0.038750      1 of 1        ✓    383ms
↓   RIF/USDT(MA2)             0.038746      1 of 1        ✓    407ms
↓   RIF/USDT(MA3)             0.038744      1 of 1        ✓    411ms
↓   RIF/USDT(mp1%)       55,656.132800      1 of 1        ✓    332ms
↓   USD/ARS               1,475.000000      7 of 7        ✓    878ms
ƒ   USD/ARS(CCB)          1,517.302416        N/A         ✓    <10ms
↓   USD/ARS(CCL)          1,507.586104      7 of 7        ✓    3.23s
↓   USD/COP               3,649.080750      2 of 2        ✓    947ms
ƒ   USD/COP(CCB)          3,617.818840        N/A         ✓    <10ms
↓   USD/MXN                  17.364488     10 of 10       ✓    1.54s
↓   USDT/USD                  0.998401      4 of 4        ✓    751ms
ƒ   USDT/USD(B)               0.998497        N/A         ✓    <10ms

Response time 3.47s

user@workstation:~$
```

