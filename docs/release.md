# Beta v0.7.11b1

This summary is based on the repository history from [v0.7.10](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.10) onward.

* Fixes the API serving the same cached price for every coinpair on `get_value` and `get_value_simple`.
* Fixes `get_values` returning an error for plain-text responses.
* Serves the API with gunicorn instead of the Flask development server.
* Normalizes the `get_values` and `summary` cache keys.
* Updates `requests` and `flask-cors` for known security issues.
* Runs tests in CI before publishing.
* Docker image: multi-stage build, redis and API run as non-root, redis bound to localhost.
* Access log shows the real client IP (from Cloudflare) and skips successful load balancer health checks.

# Release v0.7.10

This summary is based on the repository history from [v0.7.9](https://github.com/money-on-chain/moc_prices_source/releases/tag/v0.7.9) onward.

* Version `0.7.10b1` to `0.7.10` final.
* Updates the CA certificate bundle used by the application and Docker image.
* Refreshes Docker builds by pulling the base image and disabling the build cache.
