# Release v0.7.4

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

- Major work around **RIF/USD [Weighted Depth Average Price (WDAP)](https://github.com/money-on-chain/moc_prices_source/tree/master/docs/fundamentals/wdap.md) variants** (`TMA`, `TBMA`) and related monitoring/documentation updates.
- Expanded reporting and source updates for `BTC/USDT` and `USDT/USD` price feeds.
- Hardening against exchange/API issues (e.g., Bybit API restrictions, URI and engine handling updates).
- Improvements in on-chain reliability and HTTP provider behavior.

### February–June 2025

- Stabilization work around integrations and infrastructure (InfluxDB handling, Docker builder updates, formatting and scraping fixes).
- New and adjusted coin pairs, including `BPRO/*` and `MOC/*` related pairs.
- Incremental beta and release version bumps.

## Overall trend

From [v0.7.3](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.3) onward, the project evolved from integration and reliability fixes into a broader architecture effort focused on computed and synthetic pricing pairs, better environment/config management, and stronger observability/error handling.
