# VWAP Concepts and Fair Value

## Buy VWAP

The **Buy VWAP** is the *Volume Weighted Average Price* you would pay if you wanted to **buy** a certain maximum quantity `Q` (e.g. 5 BTC) from the **ask side** of the order book.

**Formula:**

$$
\mathrm{VWAP}_{buy} = \frac{\sum_{i=1}^{n} p_i \cdot q_i}{\sum_{i=1}^{n} q_i}
\quad\text{with}\quad
\sum_{i=1}^{n} q_i = Q
$$

- 𝑝𝑖 = ask price at level 𝑖  
- 𝒒𝑖 = quantity taken at level 𝑖  
- Keep summing levels until you fill exactly 𝐐.

This is your **average execution cost per unit** when buying `Q`.

---

## Sell VWAP

The **Sell VWAP** is the same concept, but on the **bid side** of the book: *“If I sell quantity `Q`, what average price will I get?”*

**Formula:**

$$
\mathrm{VWAP}_{sell} = \frac{\sum_{i=1}^{m} p_i \cdot q_i}{\sum_{i=1}^{m} q_i}
\quad\text{with}\quad
\sum_{i=1}^{m} q_i = Q
$$

- 𝑝𝑖 = bid price at level 𝑖
- 𝒒𝑖 = quantity sold into level 𝑖

This is your **average revenue per unit** for selling `Q`.

---

## Mid VWAP (“fair value”)

The **Mid VWAP** is a symmetric “fair value” combining both sides:

**Formula:**

$$
\mathrm{VWAP}_{mid} = \frac{\mathrm{VWAP}_{buy} + \mathrm{VWAP}_{sell}}{2}
$$

### Why use Mid VWAP?

- Symmetric between buy-cost and sell-proceeds for the **same quantity 𝐐**.  
- Less sensitive to short-term order-book imbalances or spoofing.  
- A **single robust reference price**, harder to manipulate than the last trade or top-of-book alone.

In practice, **Mid VWAP** is closer to a *consensus price* reflecting both sides of real liquidity.

---

## Who uses this method?

- **Derivatives exchanges**: Many perpetual swap platforms (e.g., Binance Futures, Bybit, OKX) use variants of VWAP-based or depth-based prices to compute **Mark Price** (used for margining and liquidation safety).  
- **Institutional trading**: VWAP is one of the most common benchmarks for **execution quality** in algorithmic trading.  
- **On-chain oracles**: Some decentralized oracles (inspired by Chainlink, Pyth, UMA) incorporate depth-weighted or medianized VWAPs from multiple venues to avoid manipulation.  

---

##  References

- [Investopedia – Volume Weighted Average Price (VWAP)](https://www.investopedia.com/terms/v/vwap.asp)  
- [Binance Futures – Mark Price and Funding Rate](https://www.binance.com/en/support/faq/binance-futures-how-is-mark-price-calculated-360033525031)  
- [Pyth Network Docs – Price Feeds](https://docs.pyth.network/documentation/pythnet-price-feeds/about)  
- [CFA Institute – VWAP definition](https://www.cfainstitute.org/en/research/foundation/2019/vwap)  