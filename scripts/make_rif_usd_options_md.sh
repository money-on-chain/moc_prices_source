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
