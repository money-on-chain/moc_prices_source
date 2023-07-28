#!/usr/bin/env bash

OUTFILE=docs/cli.md

# Working directory: the root of the project
cd "$(dirname "$0")/.."

run () {
    echo "\`\`\`shell" 
    echo "user@workstation:~$ moc_prices_source_check $@"
    ./moc_prices_source_check $@
    echo "user@workstation:~$"
    echo "\`\`\`" 
}

report () {
    cat <<EOL
# **MoC prices source**

This is the python package used in [**Money on Chain**](https://moneyonchain.com/) projects where it is required to get the coinpair values directly from the sources.
This package includes a CLI tool that allows you to query the coinpair values in the same way that [**Money on Chain**](https://moneyonchain.com/) projects do.



## How the included CLI tool looks like

Get command help

$(run --help)

Get data from only coinpairs that start from \`BTC\`

$(run BTC/*)

Get data from all supported coinpairs

$(run)

EOL
} 

mkdir -p "$(dirname "$OUTFILE")"

report > "$OUTFILE"
