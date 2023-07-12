#!/usr/bin/env bash

OUTFILE=docs/rif_usd_options.md

# Working directory: the root of the project
cd "$(dirname "$0")/.."

example () { 
    echo "user@workstation:~$ moc_prices_source_check \"RIF/USD*\""
    ./moc_prices_source_check "RIF/USD*"
    echo "user@workstation:~$"
}

FORMULAS=$(./moc_prices_source_check --computed | grep "RIF/USD(")
COUNT=$(echo "$FORMULAS" | wc -l)
EXAMPLE=$(example)

report () {
    cat <<EOL
# Options for the \`RIF/USD\` price source

Currently there are **$COUNT** options and they respond to the following formulas:

\`\`\`
$FORMULAS
\`\`\`

An example of these options can be seen by running the \`moc_prices_source_check "RIF/USD*"\` command.

## Example:

\`\`\`
$EXAMPLE
\`\`\`

EOL
} 

mkdir -p "$(dirname "$OUTFILE")"
report > "$OUTFILE"
