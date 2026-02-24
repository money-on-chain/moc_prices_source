# Report – USDT/USD price sources

Last Reviewed on 2025-09-23

---

## 1. Suggested Price Source Allocation

| Exchange | Weight (%) | Est. Annual Volume (USDT/USD) | Source Reference | Comment / Rationale |
|----------|------------|-------------------------------|------------------|---------------------|
| **Kraken** | 35% | ≈ **$25–30B** (≈ $70–80M daily × 365) | Kraken Pro market page (USDT/USD) + aggregator data | Strong fiat rails, consistent depth and compliance. Fits as a primary venue with robust liquidity. |
| **Coinbase Advanced** | 35% | ≈ **$20–25B** (≈ $55–70M daily × 365) | Coinbase Advanced USDT-USD order book + aggregator data | High liquidity in USDT-USD, strong compliance, and infrastructure. A top-tier fiat venue. |
| **Bitstamp** | 15% | ≈ **$1–1.5B** (≈ $3–4M daily × 365) | Bitstamp market page (USDT/USD) + CoinMarketCap | Lower volumes but reliable European venue. Adds regulatory diversity and historical continuity. |
| **Gemini** | 15% | ≈ **$1.5–2B** (≈ $4–5M daily × 365) | Gemini market data (USDT/USD) + aggregator data | Mid-level liquidity but consistent. Strengthens decentralization and adds US-regulated diversity. |

---

## 2. API Endpoints

| Exchange | API Endpoint (REST) | Notes |
|----------|----------------------|-------|
| **Kraken**   | `https://api.kraken.com/0/public/Ticker?pair=USDTUSD` | Returns bid/ask/last for USDT/USD. Can also fetch order book via `/Depth`. |
| **Coinbase** | `https://api.exchange.coinbase.com/products/USDT-USD/ticker` | Provides last trade, best bid/ask, volume. (Advanced Trade API, formerly Pro). |
| **Bitstamp** | `https://www.bitstamp.net/api/v2/ticker/usdtusd/` | Simple JSON with last, bid, ask, volume. Stable and widely used. |
| **Gemini**   | `https://api.gemini.com/v1/pubticker/usdtusd` | Returns last, bid, ask, volume. Gemini also offers `/v2/candles` for OHLC data. |

---

## 3. Methodology (Summary)

- **Exchange selection:** Focused on regulated venues with direct fiat (USD) order books for USDT.  
- **Weighting scheme:** Based on estimated annualized trading volumes; capped to prevent over-concentration.  
- **APIs:** REST endpoints chosen for reliability and ease of integration.  

---

## 4. Conclusion

The proposed basket — **Kraken (35%), Coinbase Advanced (35%), Bitstamp (15%), Gemini (15%)** — balances liquidity, regulatory diversity, and decentralization.  
These four venues ensure coverage of the largest USDT/USD fiat markets while maintaining redundancy.  

By consuming the listed API endpoints and applying a robust aggregation methodology (weighted median + outlier filters), you get a reliable and manipulation-resistant reference price for the USDT/USD pair.
