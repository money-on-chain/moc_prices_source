# Beta v0.7.11b1

This summary is based on the repository history from [v0.7.10](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.10) onward.

* Fixes the API serving the same cached price for every coinpair on `get_value` and `get_value_simple`.
* Fixes `get_values` returning an error for plain-text responses.
* Serves the API with gunicorn instead of the Flask development server.
* Normalizes the `get_values` and `summary` cache keys.
* Updates `requests` and `flask-cors` for known security issues.
* Runs tests in CI before publishing.
* Docker image: multi-stage build, redis and API run as non-root, redis bound to localhost.
* Access log shows the real client IP (from Cloudflare). Successful load balancer health checks are summarized every 100 requests per API worker by default; `HEALTH_CHECK_LOG_INTERVAL` configures the interval.
* Uses a consistent timestamp, level, source, and process ID format for application and Gunicorn logs.
* Includes the client IP in API calculation logs, using the same Cloudflare address validation and remote-address fallback as the access log.
* Logs calculated values and their successful/total source counts in the same entry.

# Release v0.7.10 (2026-10-22)

This summary is based on the repository history from [v0.7.9](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.9) onward.

* Version `0.7.10b1` to `0.7.10` final.
* Updates the CA certificate bundle used by the application and Docker image.
* Refreshes Docker builds by pulling the base image and disabling the build cache.

# Release v0.7.9 (2026-10-07)

This summary is based on the repository history from [v0.7.8](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.8) onward.

* Version `0.7.9b1` to `0.7.9` final.
* Improves price collection when a source encounters an error.
* Updates several price sources and disables those that are no longer available.

# Release v0.7.8 (2026-08-26)

This summary is based on the repository history from [v0.7.7](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.7) onward.

* Version `0.7.8-beta-2` to `0.7.8` final.
* Improves the weighted median calculation with input validation, finite-number checks, and better numeric precision.
* Replaces the Binance and Bybit failover hosts with configurable proxy support, including a default proxy for all HTTP requests.
* Adds proxy URL validation and masking to prevent credentials and sensitive URL details from appearing in errors or configuration output.

# Release v0.7.4 (2026-02-24)

This summary is based on the repository history from [v0.7.3](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.3) onward.

## Main changes by period

### January–February 2026

- Largest development wave in the period:
  - Introduction and expansion of **computed/on-chain** and **inverted** pair logic.
  - Environment handling refactors (`Envs` and boolean/env parsing improvements).
  - Output/CLI and summary handling improvements, including JSON behavior fixes.
  - Logging and error-handling enhancements.
  - New `RIF/USD` variants (`RIF_USD_TMA2`, `RIF_USD_TMA3`) and additional depth-related work.
- Continued version progression up to `0.7.4b35`.

### September–November 2025

- Major work around **RIF/USD [Depth Weighted Average Price (DWAP)](https://github.com/money-on-chain/moc_prices_source/tree/master/docs/fundamentals/dwap.md) variants** (`TMA`, `TBMA`) and related monitoring/documentation updates.
- Expanded reporting and source updates for `BTC/USDT` and `USDT/USD` price feeds.
- Hardening against exchange/API issues (e.g., Bybit API restrictions, URI and engine handling updates).
- Improvements in on-chain reliability and HTTP provider behavior.

### February–June 2025

- Stabilization work around integrations and infrastructure (InfluxDB handling, Docker builder updates, formatting and scraping fixes).
- New and adjusted coin pairs, including `BPRO/*` and `MOC/*` related pairs.
- Incremental beta and release version bumps.

## Overall trend

From [v0.7.3](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.3) onward, the project evolved from integration and reliability fixes into a broader architecture effort focused on computed and synthetic pricing pairs, better environment/config management, and stronger observability/error handling.
