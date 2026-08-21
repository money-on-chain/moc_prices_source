# Repository Guidance

## Code Review Rules

### Intentional proxy behavior

The following are deliberate design decisions. Do not report them as defects
unless the implementation deviates from the behavior described here:

- Binance and Bybit intentionally inherit from `Base`, not
  `BaseWithFailover`.
- Legacy failover hosts and the environment variables
  `BINANCE_API_HOST_FAILOVER` and `BYBIT_API_HOST_FAILOVER` are intentionally
  unsupported.
- When no proxy is configured, requests intentionally use only the direct
  endpoint. No automatic failover is expected.
- Redis HTTP cache keys intentionally exclude proxy configuration. Cached
  responses for the same request are considered interchangeable regardless
  of which proxy produced them.
- `Envs` intentionally does not cast default values. URL masking applies only
  to values converted to `URL`. Current production proxy defaults must remain
  `None`; callers that need a non-`None` URL default must construct a `URL`
  explicitly.
- An empty per-engine proxy intentionally disables `DEFAULT_PROXY`.

Only report a proxy-related finding when it contradicts one of these
invariants, exposes credentials from an environment-provided URL, or causes
behavior outside this documented scope.

