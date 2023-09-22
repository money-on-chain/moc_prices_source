#!/usr/bin/env bash

OUTFILE=docs/rif_usd_options.md

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

options () {
    ./moc_prices_source_check --computed | awk 'NR>3 && NF>0 && (substr($0,0,8)=="RIF/USD(") {print("* "$1)}'
    echo "* RIF/USDT(MA)"
    echo "* RIF/USDT"
}

summary () {
    ./moc_prices_source_check "RIF/USD*" --summary --markdown
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

\`RIF/USD(TB)\`: Because it goes through *RIF/**T**ether*, ***B**itcoin/Dollar* and *Bitcoin/**T**ether* to get to the desired pair.

\`RIF/USD(T)\`: Because it goes through *RIF/**T**ether* and ***T**ether/Dollar* to reach the desired pair.

\`RIF/USD(WMTB)\`: Because uses a **W**eighted **M**edian between \`RIF/USD(B)\` and \`RIF/USD(TB)\` to reach the desired pair.

\`RIF/USDT(MA)\`: Because uses the \`RIF/USDT\` with the "**M**agic **A**verage" algorithm analyzing the orderbook depth.

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
