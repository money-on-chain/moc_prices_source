# Report – BTC/USDT price sources

Last Reviewed on 2026-03-03  

---

## 1. Suggested Price Source Allocation

| Exchange       | Weight (%) | Est. Annual Volume (BTC/USDT) | Source Reference | Comment / Rationale |
|----------------|------------|--------------------------------|------------------|---------------------|
| **Binance**    | 65%        | ≈ **$1.5–2.0T** (≈ $4–5B daily × 365) | CoinGecko / CMC aggregator, Binance market stats | By far the largest BTC/USDT venue, with deep liquidity and narrow spreads. Needs overweighting, but capped below 70% for decentralization. |
| **OKX**        | 15%        | ≈ **$350–450B** (≈ $1–1.2B daily × 365) | OKX market stats + CoinMarketCap | One of the top global venues for BTC/USDT. Strong Asian market presence. |
| **Bybit**      | 10%        | ≈ **$200–250B** (≈ $550–700M daily × 365) | Bybit spot markets data | Adds diversity, mid-tier liquidity. Popular exchange for retail + institutional users. |
| **Huobi (HTX)**| 5%         | ≈ **$100B** (≈ $250–300M daily × 365) | Huobi Global stats | Still significant in Asia, though declining. Provides geographic diversity. |
| **KuCoin**     | 5%         | ≈ **$80–100B** (≈ $220–270M daily × 365) | KuCoin market data | Mid-level exchange, reliable API. Helps avoid over-dependence on the top 2 venues. |

---

## 2. API Endpoints

| Exchange   | API Endpoint (REST) | Notes |
|------------|----------------------|-------|
| **Binance** | `https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT` | Returns best bid/ask. Alternative: `/ticker/24hr` for volume + last price. |
| **OKX**     | `https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT` | Returns last, best bid/ask, volume. |
| **Bybit**   | `https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT` | JSON with last price, bid/ask, volume. |
| **Huobi**   | `https://api.huobi.pro/market/detail/merged?symbol=btcusdt` | Returns aggregated tick data (bid/ask/last, volume). |
| **KuCoin**  | `https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT` | Level 1 orderbook: best bid/ask + price. |

---

## 3. Methodology (Summary)

- **Exchange selection:** Focused on the largest BTC/USDT spot markets by reported and adjusted volumes.  
- **Weighting scheme:** Weighted according to estimated annualized spot trading volumes. Binance dominates, but allocations capped to keep redundancy.  
- **APIs:** REST endpoints selected for reliability, transparency, and available liquidity data (bid/ask/last/volume).  

---

## 4. Conclusion

The proposed basket — **Binance (65%), OKX (15%), Bybit (10%), Huobi (5%), KuCoin (5%)** — reflects actual liquidity distribution while avoiding over-reliance on Binance.  
This ensures that the BTC/USDT reference price is robust, manipulation-resistant, and geographically diversified across Asia, Europe, and global retail exchanges.  

By consuming the listed API endpoints and applying a robust aggregation methodology (weighted median + outlier filters), you get a reliable and manipulation-resistant reference price for the BTC/USDT pair.
