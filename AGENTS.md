# Repository Guidance

## Code Review Rules

### Experimental web scraping

- Web scraping engines are experimental and serve as references for monitoring.
  Do not report failures confined to their HTML parsing or scraped prices as
  review findings.
- Review whether a web scraping engine's failure can interrupt price collection
  or corrupt results for other coinpairs obtained through non-scraping methods.
  Report failures that cross that boundary.
- Keep in mind that a configured scraping source can still contribute to its
  own coinpair's aggregate price and to computed pairs that depend on it.

### Intentional proxy behavior

Treat the following as intentional design invariants:

- Proxy routing is transport-only and does not imply automatic endpoint
  failover.
- Proxy resolution follows this precedence:
  - A non-empty per-engine proxy overrides `DEFAULT_PROXY`.
  - `None` falls back to `DEFAULT_PROXY`.
  - An empty per-engine proxy explicitly disables `DEFAULT_PROXY`.
  - If the resolved proxy is empty, requests go directly to the upstream
    endpoint and must not inherit `HTTP_PROXY`, `HTTPS_PROXY`, or `ALL_PROXY`.
- Redis HTTP cache keys intentionally exclude proxy configuration. Cached
  upstream requests share cached responses regardless of their proxy route.
- `Envs` intentionally does not cast default values. Production proxy defaults
  must remain `None`; a non-`None` URL default must be constructed as `URL`.
- Proxy credentials, paths, and query parameters must never appear in errors,
  logs, or rendered configuration, regardless of where the URL originated.
