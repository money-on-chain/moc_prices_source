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
  -v, --version   Show version and exit.
  -j, --json      Show data in JSON format and exit.
  -w, --weighing  Show the default weighing and exit.
  -c, --computed  Show the computed pairs formula and exit.
  -s, --summary   Show the summary and exit.
  -m, --markdown  Set markdown for the summary format.
  -h, --help      Show this message and exit.
user@workstation:~$
```

Get data from only coinpairs that start from `BTC`

```shell
user@workstation:~$ moc_prices_source_check BTC/*

From     To      V.    Exchnage    Response        Weight    %  Time
-------  ------  ----  ----------  ------------  --------  ---  ------
Bitcoin  Dollar        Bitfinex    $  26.63200K      0.18   18  0.98s
Bitcoin  Dollar        Bitstamp    $  26.59600K      0.22   22  0.98s
Bitcoin  Dollar        Coinbase    $  26.59208K      0.25   25  0.97s
Bitcoin  Dollar        Gemini      $  26.59521K      0.17   17  1.15s
Bitcoin  Dollar        Kraken      $  26.59240K      0.18   18  0.76s
Bitcoin  Tether        Binance     ₮  26.60007K      0.8    80  0.98s
Bitcoin  Tether        Bitfinex    ₮  26.60600K      0.05    5  1.08s
Bitcoin  Tether        Coinbase    ₮  26.59744K      0.1    10  0.96s
Bitcoin  Tether        Kraken      ₮  26.61380K      0.05    5  0.98s

    Coin pair      Mediam     Mean    Weighted median    Sources
--  -----------  --------  -------  -----------------  ---------
↓   BTC/USD       26595.2  26601.5            26595.2          5
↓   BTC/USDT      26603    26604.3            26600.9          4

Response time 1.17s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

From          To       V.    Exchnage        Response                Weight  %      Time
------------  -------  ----  --------------  --------------------  --------  -----  ------
Binance Coin  Tether         Binance         ₮ 210.40000               1     100.0  0.55s
Bitcoin       Dollar         Bitfinex        $  26.63200K              0.18  18.0   0.32s
Bitcoin       Dollar         Bitstamp        $  26.59600K              0.22  22.0   0.56s
Bitcoin       Dollar         Coinbase        $  26.59208K              0.25  25.0   0.56s
Bitcoin       Dollar         Gemini          $  26.59521K              0.17  17.0   1.17s
Bitcoin       Dollar         Kraken          $  26.59240K              0.18  18.0   0.75s
Bitcoin       Tether         Binance         ₮  26.60006K              0.8   80.0   0.71s
Bitcoin       Tether         Bitfinex        ₮  26.60600K              0.05  5.0    0.51s
Bitcoin       Tether         Coinbase        ₮  26.59744K              0.1   10.0   0.54s
Bitcoin       Tether         Kraken          ₮  26.61380K              0.05  5.0    0.54s
Ether         Bitcoin        Binance         ₿  59.99000m              0.25  25.0   0.72s
Ether         Bitcoin        Bitfinex        ₿  60.01700m              0.25  25.0   0.72s
Ether         Bitcoin        Bitstamp        ₿  60.03022m              0.25  25.0   0.57s
Ether         Bitcoin        Gemini          ₿  59.98000m              0     N/A    1.13s
Ether         Bitcoin        Kraken          ₿  60.01000m              0.25  25.0   0.56s
MOC Token     Bitcoin        Sovryn onchain  ₿   1.58450µ              1     100.0  1.72s
RIF Token     Bitcoin        Binance         ₿   2.57000µ              1     100.0  0.72s
RIF Token     Bitcoin        BitHumb         HTTPSConnectio [...]      0     N/A    N/A
RIF Token     Bitcoin        Coingecko       Response age e [...]      0     N/A    N/A
RIF Token     Bitcoin        MEXC            ₿   2.57400µ              0     N/A    0.68s
RIF Token     Bitcoin        Sovryn onchain  ₿   2.57035µ              0     N/A    1.77s
RIF Token     Tether   MA    Binance         ₮  68.27699m              1     100.0  0.55s
RIF Token     Tether         Binance         ₮  68.10000m              1     100.0  0.65s
Tether        Dollar         Bitstamp        $ 999.89000m              0.15  15.0   0.56s
Tether        Dollar         Coinbase        $ 999.94500m              0.45  45.0   0.58s
Tether        Dollar         Kraken          $ 999.80000m              0.4   40.0   1.19s

    Coin pair               Mediam             Mean    Weighted median  Sources
--  -------------  ---------------  ---------------  -----------------  ---------
ƒ   BNB/USD          210.338          210.378             210.355       N/A
↓   BNB/USDT         210.4            210.4               210.4         1
↓   BTC/USD        26595.2          26601.5             26595.2         5
↓   BTC/USDT       26603            26604.3             26600.9         4
↓   ETH/BTC            0.06001          0.0600054           0.06001     5
ƒ   ETH/USD         1595.98          1596.24             1595.98        N/A
↓   MOC/BTC            1.5845e-06       1.5845e-06          1.5845e-06  1
ƒ   MOC/USD            0.04214          0.04215             0.04214     N/A
↓   RIF/BTC            2.57035e-06      2.57145e-06         2.57e-06    3
ƒ   RIF/USD            0.068359         0.0684045           0.0683497   N/A
ƒ   RIF/USD(B)         0.068359         0.0684045           0.0683497   N/A
ƒ   RIF/USD(T)         0.0680925        0.0680917           0.0680925   N/A
ƒ   RIF/USD(TB)        0.06808          0.0680929           0.0680855   N/A
ƒ   RIF/USD(WMTB)      0.0681497        0.0681708           0.0681516   N/A
↓   RIF/USDT           0.0681           0.0681              0.0681      1
↓   RIF/USDT(MA)       0.068277         0.068277            0.068277    1
↓   USDT/USD           0.99989          0.999878            0.99989     3
ƒ   USDT/USD(B)        0.999706         0.999895            0.999787    N/A

Response time 1.82s

user@workstation:~$
```

