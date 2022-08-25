# Proof of concept for auto-update `moc_price_source`

This is a proof of concept to update the package programmatically from the same process that makes use of the package.



## References

* [Using pip from your program](https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program)



## Example

File: `poc_autoupdate_package.py`

```python
#!/usr/bin/env python3
import sys
from importlib import reload
from subprocess import CalledProcessError, check_call



def get_installed_version(module_name: str) -> str or None:
    """Returns the version of a module.
    
    if the module is not installed returns None"""

    try:
        module_obj = __import__(module_name, {}, {})

        # Necessary in case the package changed while this process is running.
        reload(module_obj)

        return module_obj.__version__

    except ModuleNotFoundError:
        return None



def check_package(package_name: str, module_name: str, required_version: str
                  ) -> bool:
    """Checks if a package is installed.

    Installs the package if it is not installed or (Up/Down)grade the package
    if the version is not the required one.

    Finally returns True or False if the package meets the requirements."""

    if get_installed_version(module_name) != required_version:

        # Use sys.executable to ensure that you will call the same pip
        # associated with the current runtime, Ref:
        # https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
        
        try:
            check_call(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    f"{package_name}=={required_version}"
                ]
            )
        except CalledProcessError:
            pass

    ok = get_installed_version(module_name) == required_version

    return ok



if __name__ == '__main__':

    # These parameters are hardcoded but can be taken from anywhere,
    # a configuration file or a process that takes data from the onchain
    # registry, for this proof of concept it is enough.

    package_name = 'moneyonchain-prices-source'
    module_name = 'moc_prices_source'
    required_version = '0.6.0b'

    # Check the package
    package_ok = check_package(package_name, module_name, required_version)

    if not package_ok:
        message = f"Invalid {package_name} version, must be {required_version}."
        print(message, file=sys.stderr)
        exit(1)

    # As an example I use the library to obtain the BTC price.
    from moc_prices_source import get_price, BTC_USD

    pair = BTC_USD
    price = get_price(pair)

    print(f"{pair}")
    print(f"1{pair.from_.small_symbol} = {price:.2f}{pair.to_.small_symbol}")

```

This file can be downloaded from [here](files/poc_autoupdate_package.py)

The result of running this if things go well:
```shell
jbokser@beta:~/moc_prices_source/docs/files$ ./poc_autoupdate_package.py 
BTC/USD
1₿ = 21690.19$
jbokser@beta:~/moc_prices_source/docs/files$
```

If things go wrong:
```shell
jbokser@beta:~/moc_prices_source/docs/files$ ./poc_autoupdate_package.py 
Invalid moneyonchain-prices-source version, must be 0.6.0b.
jbokser@beta:~/moc_prices_source/docs/files$ 
```