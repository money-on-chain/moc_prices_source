#!/usr/bin/env bash

OUTFILE=docs/rif_usd_options.md
RIF_USD_MA_DEPTH=200000

# Working directory: the root of the project
cd "$(dirname "$0")/.."

example () { 
    echo "user@workstation:~$ moc_prices_source_check --help"
    ./moc_prices_source_check --help
    echo ""
    echo "user@workstation:~$ moc_prices_source_check \"RIF/USD*\""
    ./moc_prices_source_check "RIF/USD*"
    echo "user@workstation:~$"
}

options_base () {
    ./moc_prices_source_check --computed | awk 'NR>3 && NF>0 && (substr($0,0,8)=="RIF/USD(") {print($1)}' | grep -v "MA2" | grep -v "MA3" | sort
    echo "RIF/USDT(MA)"
    echo "RIF/USDT"
}


options () {
    options_base | awk '{print("* "$1)}'
}

summary () {
    RIF_USD_MA_DEPTH=$RIF_USD_MA_DEPTH ./moc_prices_source_check "$(options_base | paste -sd, -)" --summary --markdown
}

SUMMARY=$(summary)
OPTIONS=$(options)
COUNT=$(echo "$OPTIONS" | wc -l)
EXAMPLE=$(example)
DATE=$(date '+%F')

report () {
    cat <<EOL
# **Options for the \`RIF/USD\` price source**

Date: **$DATE**




## Options

Currently there are **$COUNT** options:

$OPTIONS

## Chosen Option

**Selected price source for RIF/USD: \`RIF/USD(TMA)\`**

### Why \`RIF/USD(TMA)\` was chosen

We have selected **RIF/USD(TMA)** as the official price source for the \`RIF/USD\` pair.

**Justification:**

1. **Direct computation through the RIF/USDT pair**  
   \`RIF/USD(TMA)\` leverages the **RIF/USDT market depth via the DWAP algorithm** (formerly known as “Magic Average”) and then multiplies it by the **USDT/USD price** to obtain the RIF/USD rate. This means the core pricing is derived from the **active RIF/USDT market**, which in practice is the most liquid and widely traded derivative of RIF versus USD-equivalents available.

2. **Orderbook depth-based averaging (DWAP)**  
   The use of the **DWAP algorithm** (analyzed to a 200k depth) reduces the impact of short-term price spikes, outliers, or illiquid trades, producing a **more robust and less noisy price signal** than simple midpoint or last-trade approaches.

3. **Stability and real market reflection**  
   Compared with alternatives that rely on indirect routing via RIF/BTC, BTC/USDT and BTC/USD (such as \`RIF/USD(TB)\`), \`RIF/USD(TMA)\` **avoids unnecessary dependencies** on multiple intermediary pairs whose correlated price moves can compound slippage or arbitrage deviations. By **focusing on RIF/USDT and the stable USDT/USD rate**, it reflects directly traded and deeper liquidity conditions.

**In summary:**  
\`RIF/USD(TMA)\` combines **true market liquidity (via USDT)** with **depth-aware averaging (DWAP)** and the very stable **USDT/USD conversion**, making it the most **robust, reliable, and less noisy computed source** for the \`RIF/USD\` price among all available options.

![usdt_usd_comparison_2026-03-03.jpg](images/usdt_usd_comparison_2026-03-03.jpg)

_Example data from 2026-03-03_

(¹) _It is the same data for \`USDT/USD\` weighted median_

(²) _Respond to the formula \`BTC/USD\` ÷ \`BTC/USDT\`_


---

## Rationale behind the chosen nomenclature

\`RIF/USD(B)\`: Because it goes through *RIF/**B**itcoin* and ***B**itcoin/Dollar* to reach the desired pair.

\`RIF/USD(T)\`: Because it goes through *RIF/**T**ether* and ***T**ether/Dollar* to reach the desired pair.

\`RIF/USD(TB)\`: Because it goes through *RIF/**T**ether*, ***B**itcoin/Dollar* and *Bitcoin/**T**ether* to get to the desired pair.

\`RIF/USD(TBMA)\`: Because it goes through *RIF/**T**ether*, ***B**itcoin/Dollar* and *Bitcoin/**T**ether* to get to the desired pair, but using the Use the algorithm [DWAP](fundamentals/dwap.md) formerly known as "**M**agic **A**verage" analyzing the orderbook depth for the \`RIF/USDT\` pair.

\`RIF/USD(TMA)\`: Because it goes through *RIF/**T**ether* and ***T**ether/Dollar* to reach the desired pair, but using the algorithm [DWAP](fundamentals/dwap.md) formerly known as "**M**agic **A**verage" algorithm analyzing the orderbook depth for the \`RIF/USDT\` pair.

\`RIF/USD(WMTB)\`: Because uses a **W**eighted **M**edian between \`RIF/USD(B)\` and \`RIF/USD(TB)\` to reach the desired pair.

\`RIF/USDT(MA)\`: Because uses the \`RIF/USDT\` with the algorithm [DWAP](fundamentals/dwap.md) formerly known as "**M**agic **A**verage" algorithm analyzing the orderbook depth.

\`RIF/USDT\`: Because uses directly the \`RIF/USDT\` pair.

$SUMMARY

## The \`moc_prices_source_check\` tool

There is a tool that comes with the [\`moc_prices_source\` package](https://github.com/money-on-chain/moc_prices_source) that allows us to run a simulation that queries and calculates all the coinpairs.
This tool is called \`moc_prices_source_check\` and here you can see an example of its use.

### Example

\`\`\`shell
$EXAMPLE
\`\`\`

EOL
} 

mkdir -p "$(dirname "$OUTFILE")"

report > "$OUTFILE"
