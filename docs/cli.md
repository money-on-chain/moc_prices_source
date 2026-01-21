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
BTC/ARS           Bitcoin to Peso Arg.  Binance     $ 141.33142M      0.2   20    0.52s
BTC/ARS           Bitcoin to Peso Arg.  BuenBit     $ 140.53123M      0.2   20    0.53s
BTC/ARS           Bitcoin to Peso Arg.  Decrypto    $ 141.24921M      0.2   20    2.36s
BTC/ARS           Bitcoin to Peso Arg.  Lemoncash   $ 139.04959M      0.2   20    0.85s
BTC/ARS           Bitcoin to Peso Arg.  belo.app    $ 141.97048M      0.2   20    1.47s
BTC/COP           Bitcoin to Peso Col.  BuenBit     $ 337.09448M      0.33  33.3  0.77s
BTC/COP           Bitcoin to Peso Col.  Coinbase    $ 342.05334M      0.33  33.3  0.94s
BTC/COP           Bitcoin to Peso Col.  buda.com    $ 330.09554M      0.33  33.3  0.44s
BTC/USD           Bitcoin to Dollar     Bitfinex    $  93.21900K      0.18  18    0.33s
BTC/USD           Bitcoin to Dollar     Bitstamp    $  93.19100K      0.22  22    0.93s
BTC/USD           Bitcoin to Dollar     Coinbase    $  93.18800K      0.25  25    0.93s
BTC/USD           Bitcoin to Dollar     Gemini      $  93.18596K      0.17  17    1.23s
BTC/USD           Bitcoin to Dollar     Kraken      $  93.19250K      0.18  18    0.54s
BTC/USDT          Bitcoin to Tether     Binance     ₮  93.24244K      0.65  65    0.5s
BTC/USDT          Bitcoin to Tether     Bybit       ₮  93.24105K      0.1   10    0.6s
BTC/USDT          Bitcoin to Tether     Huobi       ₮  93.25393K      0.05   5    0.81s
BTC/USDT          Bitcoin to Tether     KuCoin      ₮  93.24085K      0.05   5    1.02s
BTC/USDT          Bitcoin to Tether     OKX         ₮  93.23385K      0.15  15    0.91s

    Coinpair                 Value   Sources count    Ok
--  ----------  ------------------  ---------------  ----
↓   BTC/ARS     141,249,207.000000      5 of 5        ✓
↓   BTC/COP     337,094,479.904000      3 of 3        ✓
↓   BTC/USD          93,191.000000      5 of 5        ✓
↓   BTC/USDT         93,242.445000      5 of 5        ✓

Response time 2.37s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

Coinpair    V.    Short description       Exchnage               Response                Weight  %      Time
----------  ----  ----------------------  ---------------------  --------------------  --------  -----  ------
BLOCK       RSK   Rootstock block number  RSK onchain            8438775                   1     100.0  2.41s
BNB/USDT          BinanceCoin to Tether   Binance                ₮ 926.50000               1     100.0  0.68s
BPRO/BTC          BPro to Bitcoin         MOC onchain            ₿   1.21772               1     100.0  2.57s
BTC/ARS           Bitcoin to Peso Arg.    Binance                $ 141.33142M              0.2   20.0   0.68s
BTC/ARS           Bitcoin to Peso Arg.    BuenBit                $ 140.53123M              0.2   20.0   0.87s
BTC/ARS           Bitcoin to Peso Arg.    Decrypto               $ 141.24936M              0.2   20.0   2.34s
BTC/ARS           Bitcoin to Peso Arg.    Lemoncash              $ 139.04959M              0.2   20.0   1.19s
BTC/ARS           Bitcoin to Peso Arg.    belo.app               $ 141.97048M              0.2   20.0   3.68s
BTC/COP           Bitcoin to Peso Col.    BuenBit                $ 337.09448M              0.33  33.3   0.67s
BTC/COP           Bitcoin to Peso Col.    Coinbase               $ 342.05920M              0.33  33.3   1.15s
BTC/COP           Bitcoin to Peso Col.    buda.com               $ 330.09554M              0.33  33.3   0.62s
BTC/USD           Bitcoin to Dollar       Bitfinex               $  93.21900K              0.18  18.0   0.93s
BTC/USD           Bitcoin to Dollar       Bitstamp               $  93.19100K              0.22  22.0   0.66s
BTC/USD           Bitcoin to Dollar       Coinbase               $  93.18800K              0.25  25.0   1.31s
BTC/USD           Bitcoin to Dollar       Gemini                 $  93.18596K              0.17  17.0   1.06s
BTC/USD           Bitcoin to Dollar       Kraken                 $  93.19030K              0.18  18.0   1.13s
BTC/USDT          Bitcoin to Tether       Binance                ₮  93.24244K              0.65  65.0   0.64s
BTC/USDT          Bitcoin to Tether       Bybit                  ₮  93.24105K              0.1   10.0   0.64s
BTC/USDT          Bitcoin to Tether       Huobi                  ₮  93.25393K              0.05  5.0    1.25s
BTC/USDT          Bitcoin to Tether       KuCoin                 ₮  93.24085K              0.05  5.0    1.13s
BTC/USDT          Bitcoin to Tether       OKX                    ₮  93.23385K              0.15  15.0   0.63s
DOC/USD           Pegged 1:1 to USD       Dummy                  $   1.00000               1     100.0  0.0s
ETH/BTC           Ether to Bitcoin        Binance                ₿  34.51000m              0.25  25.0   0.65s
ETH/BTC           Ether to Bitcoin        Bitfinex               ₿  34.51600m              0.25  25.0   0.93s
ETH/BTC           Ether to Bitcoin        Bitstamp               ₿  34.52314m              0.25  25.0   0.62s
ETH/BTC           Ether to Bitcoin        Kraken                 ₿  34.51000m              0.25  25.0   1.47s
ETH/USD           Ether to Dollar         Bitfinex               $   3.21690K              0.18  18.0   0.82s
ETH/USD           Ether to Dollar         Bitstamp               $   3.21602K              0.22  22.0   0.9s
ETH/USD           Ether to Dollar         Coinbase               $   3.21610K              0.25  25.0   1.25s
ETH/USD           Ether to Dollar         Gemini                 $   3.21553K              0.17  17.0   1.22s
ETH/USD           Ether to Dollar         Kraken                 $   3.21599K              0.18  18.0   1.43s
GAS/BTC           Rootstock gas price     RSK onchain            ₿  26.06560p              1     100.0  2.46s
MOC/BTC     sov   MOC to Bitcoin          Sovryn onchain         ₿ 371.18752p              1     100.0  4.47s
MOC/USD     Oku   MOC to Dollar           Oku onchain            $  34.64034m              1     100.0  2.41s
RIF/BTC     mp1%  To move the price 1%    Binance                ₿  50.73925m              1     100.0  2.71s
RIF/BTC           RIF to Bitcoin          Binance                ₿ 380.00000p              1     100.0  1.06s
RIF/USDT    MA    RIF to Tether           Binance                ₮  37.25000m              1     100.0  1.0s
RIF/USDT    MA2   RIF to Tether           Binance                ₮  37.24607m              1     100.0  0.97s
RIF/USDT    MA3   RIF to Tether           Binance                ₮  37.26527m              1     100.0  0.95s
RIF/USDT    mp1%  To move the price 1%    Binance                ₮  40.15552K              1     100.0  0.81s
RIF/USDT          RIF to Tether           Binance                ₮  37.20000m              1     100.0  1.01s
USD/ARS     CCL   Dollar to Peso Arg.     Ambito.com             $   1.51263K              0.14  14.3   0.99s
USD/ARS     CCL   Dollar to Peso Arg.     CoinMonitor.info       $   1.51286K              0.14  14.3   1.36s
USD/ARS     CCL   Dollar to Peso Arg.     CriptoYa.com           $   1.50556K              0.14  14.3   0.57s
USD/ARS     CCL   Dollar to Peso Arg.     DolarHoy.com           $   1.51325K              0.14  14.3   1.65s
USD/ARS     CCL   Dollar to Peso Arg.     InfoDolar.com          $   1.51044K              0.14  14.3   1.45s
USD/ARS     CCL   Dollar to Peso Arg.     Infobae                $   1.51060K              0.14  14.3   1.51s
USD/ARS     CCL   Dollar to Peso Arg.     LaNacion.com.ar        $   1.51902K              0.14  14.3   0.82s
USD/ARS           Dollar to Peso Arg.     Ambito.com             $   1.49500K              0.14  14.3   1.01s
USD/ARS           Dollar to Peso Arg.     CoinMonitor.info       $   1.50500K              0.14  14.3   1.35s
USD/ARS           Dollar to Peso Arg.     CriptoYa.com           $   1.49500K              0.14  14.3   1.0s
USD/ARS           Dollar to Peso Arg.     DolarHoy.com           $   1.49500K              0.14  14.3   1.78s
USD/ARS           Dollar to Peso Arg.     InfoDolar.com          $   1.49500K              0.14  14.3   1.68s
USD/ARS           Dollar to Peso Arg.     Infobae                $   1.50500K              0.14  14.3   1.66s
USD/ARS           Dollar to Peso Arg.     LaNacion.com.ar        $   1.49500K              0.14  14.3   0.95s
USD/COP           Dollar to Peso Col.     BanRep                 $   3.66658K              0.5   50.0   1.35s
USD/COP           Dollar to Peso Col.     DolarHoy.co            $   3.72500K              0.5   50.0   2.31s
USD/MXN           Dollar to Peso Mex.     Bitso.com              $  17.58200               0.1   10.0   0.97s
USD/MXN           Dollar to Peso Mex.     CitiBanamex            $  20.04275               0.1   10.0   1.15s
USD/MXN           Dollar to Peso Mex.     Currency.me.uk         $  17.57650               0.1   10.0   2.3s
USD/MXN           Dollar to Peso Mex.     ElDolar.info           $  17.57850               0.1   10.0   2.28s
USD/MXN           Dollar to Peso Mex.     ElEconomista.es        $  17.93300               0.1   10.0   1.65s
USD/MXN           Dollar to Peso Mex.     InfoDolar.com.mx       $  17.61500               0.1   10.0   2.0s
USD/MXN           Dollar to Peso Mex.     Intercam.com.mx        $  17.57640               0.1   10.0   1.97s
USD/MXN           Dollar to Peso Mex.     TheMoneyConverter.com  $  17.57995               0.1   10.0   1.64s
USD/MXN           Dollar to Peso Mex.     Wise.com               $  17.57690               0.1   10.0   1.31s
USD/MXN           Dollar to Peso Mex.     X-rates.com            $  17.57723               0.1   10.0   1.56s
USDT/USD          Tether to Dollar        Bitstamp               $ 999.39500m              0.15  15.0   1.3s
USDT/USD          Tether to Dollar        Coinbase               $ 999.48000m              0.35  35.0   1.5s
USDT/USD          Tether to Dollar        Gemini                 $ 999.39500m              0.15  15.0   1.09s
USDT/USD          Tether to Dollar        Kraken                 $ 999.42500m              0.35  35.0   1.33s

    Coinpair                     Value   Sources count    Ok
--  --------------  ------------------  ---------------  ----
↓   BLOCK(RSK)                 8438775      1 of 1        ✓
ƒ   BNB/USD                 925.981863        N/A         ✓
↓   BNB/USDT                926.500000      1 of 1        ✓
ƒ   BPRO/ARS        172,002,614.139300        N/A         ✓
↓   BPRO/BTC                  1.217723      1 of 1        ✓
ƒ   BPRO/COP        410,487,752.802188        N/A         ✓
ƒ   BPRO/USD            113,479.985910        N/A         ✓
↓   BTC/ARS         141,249,358.500000      5 of 5        ✓
↓   BTC/COP         337,094,479.904000      3 of 3        ✓
↓   BTC/USD              93,190.300000      5 of 5        ✓
↓   BTC/USDT             93,242.445000      5 of 5        ✓
↓   DOC/USD                   1.000000      1 of 1        ✓
↓   ETH/BTC                   0.034517      4 of 4        ✓
↓   ETH/USD               3,216.020000      5 of 5        ✓
ƒ   ETH/USD(B)            3,216.609513        N/A         ✓
↓   GAS/BTC              2.607 × 10⁻¹¹      1 of 1        ✓
ƒ   MOC/BPRO              4.523 × 10⁻⁷        N/A         ✓
ƒ   MOC/BTC               3.715 × 10⁻⁷        N/A         ✓
↓   MOC/BTC(sov)          3.712 × 10⁻⁷      1 of 1        ✓
ƒ   MOC/USD                   0.034591        N/A         ✓
↓   MOC/USD(Oku)              0.034640      1 of 1        ✓
ƒ   MOC/USD(WM)               0.034616        N/A         ✓
↓   RIF/BTC               3.800 × 10⁻⁷      1 of 1        ✓
↓   RIF/BTC(mp1%)             0.050739      1 of 1        ✓
ƒ   RIF/USD                   0.035412        N/A         ✓
ƒ   RIF/USD(B)                0.035412        N/A         ✓
ƒ   RIF/USD(T)                0.037178        N/A         ✓
ƒ   RIF/USD(TB)               0.037179        N/A         ✓
ƒ   RIF/USD(TBMA)             0.037229        N/A         ✓
ƒ   RIF/USD(TMA)              0.037228        N/A         ✓
ƒ   RIF/USD(WMTB)             0.036737        N/A         ✓
↓   RIF/USDT                  0.037200      1 of 1        ✓
↓   RIF/USDT(MA)              0.037250      1 of 1        ✓
↓   RIF/USDT(MA2)             0.037246      1 of 1        ✓
↓   RIF/USDT(MA3)             0.037265      1 of 1        ✓
↓   RIF/USDT(mp1%)       40,155.515200      1 of 1        ✓
↓   USD/ARS               1,495.000000      7 of 7        ✓
ƒ   USD/ARS(CCB)          1,515.708808        N/A         ✓
↓   USD/ARS(CCL)          1,512.630000      7 of 7        ✓
↓   USD/COP               3,695.787800      2 of 2        ✓
ƒ   USD/COP(CCB)          3,617.270037        N/A         ✓
↓   USD/MXN                  17.755750     10 of 10       ✓
↓   USDT/USD                  0.999416      4 of 4        ✓
ƒ   USDT/USD(B)               0.999441        N/A         ✓

Response time 12.41s

user@workstation:~$
```
