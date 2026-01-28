# **MoC prices source**

This is the python package used in [**Money on Chain**](https://moneyonchain.com/) projects where it is required to get the coinpair values directly from the sources.
This package includes a CLI tool that allows you to query the coinpair values in the same way that [**Money on Chain**](https://moneyonchain.com/) projects do.



## How to use it in your project

A simple example, do some imports first

```python
user@host:~$ python3 -q
>>> from moc_prices_source import get_price, BTC_USD
>>>
```

Get de `BTC/USD` coin pair

```python
>>> get_price(BTC_USD)
Decimal('89561.50000')
>>> 
```

And that's it!

More [usage examples](docs/examples.md) can be seen [here](docs/examples.md)



## How the included CLI tool looks like

Here you can see how the output of the `moc_prices_source_check` command looks like

```shell
user@host:~$ moc_prices_source_check "BTC/USD*"

Coinpair    V.    Short description    Exchnage     Response        Weight    %  Time
----------  ----  -------------------  -----------  ------------  --------  ---  ------
BTC/USD     och   Bitcoin to Dollar    MOC onchain  $  89.77020K      1     100  1.67s
BTC/USD           Bitcoin to Dollar    Bitfinex     $  89.86900K      0.18   18  201ms
BTC/USD           Bitcoin to Dollar    Bitstamp     $  89.76100K      0.22   22  301ms
BTC/USD           Bitcoin to Dollar    Coinbase     $  89.75598K      0.25   25  559ms
BTC/USD           Bitcoin to Dollar    Gemini       $  89.74511K      0.17   17  761ms
BTC/USD           Bitcoin to Dollar    Kraken       $  89.75720K      0.18   18  156ms
BTC/USDT          Bitcoin to Tether    Binance      ₮  89.87206K      0.65   65  356ms
BTC/USDT          Bitcoin to Tether    Bybit        ₮  89.87485K      0.1    10  467ms
BTC/USDT          Bitcoin to Tether    Huobi        ₮  89.86499K      0.05    5  635ms
BTC/USDT          Bitcoin to Tether    KuCoin       ₮  89.87055K      0.05    5  757ms
BTC/USDT          Bitcoin to Tether    OKX          ₮  89.87335K      0.15   15  760ms

    Coinpair              Value   Sources count    Ok   Time
--  ------------  -------------  ---------------  ----  ------
⇓   BTC/USD       89,757.200000      5 of 5        ✓    761ms
⛓   BTC/USD(och)  89,770.200000      1 of 1        ✓    1.67s
⇓   BTC/USDT      89,872.055000      5 of 5        ✓    760ms

Response time 1.71s

user@host:~$ 
```

This command has many options. you can run `moc_prices_source_check --help` to get help on how to run them.
More information about this CLI tool can be seen [here](docs/cli.md).



## References

* [Source code in Github](https://github.com/money-on-chain/moc_prices_source)
* [Package from Python package index (PyPI)](https://pypi.org/project/moneyonchain-prices-source)



## Requirements

* Python 3.6+ support



## Installation

### From the Python package index (PyPI) 

Run:

```shell
$ pip3 install moneyonchain-prices-source 
```

And then run:

```shell
$ moc_prices_source_check --version
```

To verify that it has been installed correctly

### From source

Download from [Github](https://github.com/money-on-chain/moc_prices_source)

Standing inside the folder, run:

```shell
$ pip3 install -r requirements.txt 
```

For install the dependencies and then run:

```shell
$ pip3 install .
```

Finally run:

```shell
$ moc_prices_source_check --version
```

To verify that it has been installed correctly



## Supported coinpairs and symbols

[Here](docs/supported_coinpairs.md) you can find an [summary of supported coinpairs and symbols](docs/supported_coinpairs.md)

