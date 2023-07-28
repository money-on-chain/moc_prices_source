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
Bitcoin  Dollar        Bitfinex    $  29.53300K      0.18   18  0.84s
Bitcoin  Dollar        Bitstamp    $  29.50100K      0.22   22  0.84s
Bitcoin  Dollar        Coinbase    $  29.50268K      0.25   25  0.82s
Bitcoin  Dollar        Gemini      $  29.50690K      0.17   17  1.04s
Bitcoin  Dollar        Kraken      $  29.50080K      0.18   18  1.03s
Bitcoin  Tether        Binance     ₮  29.50917K      0.8    80  0.83s
Bitcoin  Tether        Bitfinex    ₮  29.49400K      0.05    5  1.24s
Bitcoin  Tether        Coinbase    ₮  29.47703K      0.1    10  0.62s
Bitcoin  Tether        Kraken      ₮  29.51200K      0.05    5  1.04s

    Coin pair      Mediam     Mean    Weighted median    Sources
--  -----------  --------  -------  -----------------  ---------
↓   BTC/USD       29502.7  29508.9            29502.7          5
↓   BTC/USDT      29501.6  29498.1            29509.3          4

Response time 1.25s

user@workstation:~$
```

Get data from all supported coinpairs

```shell
user@workstation:~$ moc_prices_source_check 

From          To       V.    Exchnage        Response        Weight  %      Time
------------  -------  ----  --------------  ------------  --------  -----  ------
Binance Coin  Tether         Binance         ₮ 242.30000       1     100.0  0.5s
Bitcoin       Dollar         Bitfinex        $  29.53300K      0.18  18.0   0.39s
Bitcoin       Dollar         Bitstamp        $  29.50100K      0.22  22.0   0.51s
Bitcoin       Dollar         Coinbase        $  29.50404K      0.25  25.0   0.5s
Bitcoin       Dollar         Gemini          $  29.50690K      0.17  17.0   0.88s
Bitcoin       Dollar         Kraken          $  29.50080K      0.18  18.0   0.78s
Bitcoin       Tether         Binance         ₮  29.50918K      0.8   80.0   0.51s
Bitcoin       Tether         Bitfinex        ₮  29.49400K      0.05  5.0    0.3s
Bitcoin       Tether         Coinbase        ₮  29.47703K      0.1   10.0   0.21s
Bitcoin       Tether         Kraken          ₮  29.51200K      0.05  5.0    0.73s
Ether         Bitcoin        Binance         ₿  63.73000m      0.25  25.0   0.6s
Ether         Bitcoin        Bitfinex        ₿  63.71300m      0.25  25.0   0.51s
Ether         Bitcoin        Bitstamp        ₿  63.70931m      0.25  25.0   0.52s
Ether         Bitcoin        Gemini          ₿  63.78000m      0     N/A    0.87s
Ether         Bitcoin        Kraken          ₿  63.70000m      0.25  25.0   0.41s
MOC Token     Bitcoin        Sovryn onchain  ₿   2.98958µ      1     100.0  1.17s
RIF Token     Bitcoin        Binance         ₿   2.67000µ      1     100.0  0.53s
RIF Token     Bitcoin        BitHumb         ₿   6.30000µ      0     N/A    1.84s
RIF Token     Bitcoin        Coingecko       ₿   2.66000µ      0     N/A    0.48s
RIF Token     Bitcoin        MEXC            ₿   2.66700µ      0     N/A    0.54s
RIF Token     Bitcoin        Sovryn onchain  ₿   2.69475µ      0     N/A    1.38s
RIF Token     Tether         Binance         ₮  78.70000m      1     100.0  0.56s
Tether        Dollar         Bitstamp        $ 999.68000m      0.15  15.0   1.23s
Tether        Dollar         Coinbase        $ 999.65500m      0.45  45.0   0.43s
Tether        Dollar         Kraken          $ 999.66000m      0.4   40.0   0.79s

    Coin pair               Mediam             Mean    Weighted median  Sources
--  -------------  ---------------  ---------------  -----------------  ---------
ƒ   BNB/USD          242.32           242.391            242.256        N/A
↓   BNB/USDT         242.3            242.3              242.3          1
↓   BTC/USD        29504            29509.1            29504            5
↓   BTC/USDT       29501.6          29498.1            29509.3          4
↓   ETH/BTC            0.063713         0.0637265          0.0637093    5
ƒ   ETH/USD         1879.79          1880.51            1879.68         N/A
↓   MOC/BTC            2.98958e-06      2.98958e-06        2.98958e-06  1
ƒ   MOC/USD            0.0882048        0.08822            0.0882048    N/A
↓   RIF/BTC            2.67e-06         3.39835e-06        2.67e-06     5
ƒ   RIF/USD            0.0787758        0.100282           0.0787758    N/A
ƒ   RIF/USD(B)         0.0787758        0.100282           0.0787758    N/A
ƒ   RIF/USD(T)         0.0786732        0.0786736          0.0786732    N/A
ƒ   RIF/USD(TB)        0.0787065        0.0787296          0.0786859    N/A
ƒ   RIF/USD(WMTB)      0.0787239        0.0841178          0.0787083    N/A
↓   RIF/USDT           0.0787           0.0787             0.0787       1
↓   USDT/USD           0.99966          0.999665           0.99966      3
ƒ   USDT/USD(B)        1.00008          1.00038            0.99982      N/A

Response time 1.9s

user@workstation:~$
```

