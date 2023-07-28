#!/usr/bin/env bash

OUTFILE=docs/supported_coinpairs.md

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


# Supported coinpairs and symbols

$(./moc_prices_source_check --summary --markdown)

EOL
} 

mkdir -p "$(dirname "$OUTFILE")"

report > "$OUTFILE"
