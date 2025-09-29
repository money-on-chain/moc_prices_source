# Weighted Depth Average Price (WDAP) concepts and Fair Value

(a.k.a. _"The magic average"_)


## WDAP vs. VWAP

The **Weighted Depth Average Price (WDAP)** is conceptually very similar to the **Volume Weighted Average Price (VWAP)**, but the key difference lies in **what volume you use to weight prices**.

### VWAP (Volume Weighted Average Price)
- Uses *historical executed trades* (closed transactions).  
- **Formula:**

$$
VWAP = \frac{\sum_{i=1}^n (P_i \times V_i)}{\sum_{i=1}^n V_i}
$$

Where:
- _P_ 𝑖 = trade price  
- _V_ 𝑖 = traded volume  

VWAP answers: *“At what average price has the market traded, given real executed volume?”*

### WDAP (Weighted Depth Average Price)
- Uses *order book depth* — the **quantities available at each price level** in the open order book.  
- **Formula:**

$$
WDAP = \frac{\sum_{i=1}^m (P_i \times Q_i)}{\sum_{i=1}^m Q_i}
$$

Where:
- _P_ 𝑖 = order book price at level 𝑖
- _Q_ 𝑖 = resting order size (quantity) at that level  

WDAP answers: *“If I were to consume liquidity from the book up to a certain depth, what would be my average execution price?”*

### Key Difference
- **VWAP** reflects *actual market activity* (executed trades, historical reality).  
- **WDAP** reflects *potential execution cost* based on the *current state of the order book*.  

This is why WDAP is designed to be used in **fair pricing, index construction or oracle design**, where relying only on the last trade can be too noisy or manipulable, while considering the whole book provides a more robust picture of supply and demand.

### Why use WDAP?

The **Weighted Depth Average Price (WDAP)** carries over **all the advantages of VWAP**, which is widely used in traditional finance, trading algorithms, and execution benchmarking.

**Advantages of WDAP (inherited from VWAP)**

1. **Robust to manipulation**  
   Like VWAP, WDAP reduces the influence of any single outlier price.  
   Instead of being skewed by one small trade (last price) or one thin order,  
   it averages across meaningful liquidity.  

2. **Volume-sensitive**  
   Both VWAP and WDAP give more weight to levels with larger quantities,  
   reflecting the true economic significance of price levels.  

3. **Representative “fair value”**  
   VWAP has long been considered a fair benchmark for executed trades;  
   WDAP provides the same kind of fair representation,  
   but applied to the *current order book*.  

4. **Stability**  
   By using aggregated liquidity across multiple levels,  
   WDAP smooths out noise compared to last trade or top-of-book,  
   just like VWAP smooths out intraday trading volatility.  

5. **Market impact awareness**  
   VWAP tells you the average price traders actually paid;  
   WDAP tells you the average price you would pay (or receive)  
   if you consumed liquidity.  
   In both cases, you capture the impact of *volume* rather than just nominal quotes.  



## Buy WDAP

The **Buy WDAP** is the *Weighted Depth Average Price* you would pay if you wanted to **buy** a certain maximum quantity `Q` (e.g. 5 BTC) from the **ask side** of the order book.

**Formula:**

$$
\mathrm{WDAP}_{buy} = \frac{\sum_{i=1}^{n} p_i \cdot q_i}{\sum_{i=1}^{n} q_i}
\quad\text{with}\quad
\sum_{i=1}^{n} q_i = Q
$$

- _p_ 𝑖 = ask price at level 𝑖
- _q_ 𝑖 = quantity taken at level 𝑖  
- Keep summing levels until you fill exactly _Q_.

This is your **average execution cost per unit** when buying `Q`.

---

## Sell WDAP

The **Sell WDAP** is the same concept, but on the **bid side** of the book: *“If I sell quantity `Q`, what average price will I get?”*

**Formula:**

$$
\mathrm{WDAP}_{sell} = \frac{\sum_{i=1}^{m} p_i \cdot q_i}{\sum_{i=1}^{m} q_i}
\quad\text{with}\quad
\sum_{i=1}^{m} q_i = Q
$$

- _p_ 𝑖 = bid price at level 𝑖
- _q_ 𝑖 = quantity sold into level 𝑖

This is your **average revenue per unit** for selling `Q`.

---

## WDAP (“fair value” what we will finally use)

The **WDAP** is a symmetric “fair value” combining _buy_ and _sell_ sides:

**Formula:**

$$
\mathrm{WDAP} = \frac{\mathrm{WDAP}_{buy} + \mathrm{WDAP}_{sell}}{2}
$$

### Why use WDAP?

- Symmetric between buy-cost and sell-proceeds for the **same quantity _Q_**.  
- Less sensitive to short-term order-book imbalances or spoofing.  
- A **single robust reference price**, harder to manipulate than the last trade or top-of-book alone.

In practice, **WDAP** is closer to a *consensus price* reflecting both sides of real liquidity.
