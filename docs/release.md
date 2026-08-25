# Release v0.7.8

This summary is based on the repository history from [v0.7.7](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.7) onward.

* Version `0.7.8-beta-2` to `0.7.8` final.
* Improves the weighted median calculation with input validation, finite-number checks, and better numeric precision.
* Replaces the Binance and Bybit failover hosts with configurable proxy support, including a default proxy for all HTTP requests.
* Adds proxy URL validation and masking to prevent credentials and sensitive URL details from appearing in errors or configuration output.
