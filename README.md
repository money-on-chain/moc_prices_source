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
Decimal('97467.53')
>>> 
```

And that's it!

More [usage examples](docs/examples.md) can be seen [here](docs/examples.md)



## How the included CLI tool looks like

Here you can see how the output of the `moc_prices_source_check` command looks like

```shell
user@host:~$ moc_prices_source_check "BTC/USD"

Coinpair    V.    Short description    Exchnage    Response        Weight    %  Time
----------  ----  -------------------  ----------  ------------  --------  ---  ------
BTC/USD           Bitcoin to Dollar    Bitfinex    $  93.07100K      0.18   18  0.59s
BTC/USD           Bitcoin to Dollar    Bitstamp    $  93.05500K      0.22   22  0.8s
BTC/USD           Bitcoin to Dollar    Coinbase    $  93.04720K      0.25   25  1.2s
BTC/USD           Bitcoin to Dollar    Gemini      $  93.04565K      0.17   17  1.0s
BTC/USD           Bitcoin to Dollar    Kraken      $  93.04330K      0.18   18  0.8s

    Coinpair            Value   Sources count    Ok
--  ----------  -------------  ---------------  ----
↓   BTC/USD     93,047.205000      5 of 5        ✓

Response time 1.21s

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

