#!/usr/bin/env bash



# Functions

log() {
    local context="$1"
    shift
    
    local level="$1"  # INFO, WARNING, ERROR
    shift
    
    local timestamp
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    echo -e "$timestamp\t$context\t$level: $*"
}

delay() {
    local context="$1"
    shift

    local seconds=$1

    for ((i=seconds; i>0; i--)); do
        log "$context" "INFO" "Waiting $[i]s to start ..."
        sleep 1
    done
}

main() {
    local cmd_list=("moc_prices_source_api" "moc_prices_source_to_db")
    
    if [ -z "$COMMAND" ]; then
        COMMAND="moc_prices_source_api"  # Default
        log "moc_prices_source" "INFO" "COMMAND env variable is empty, using default: $COMMAND"
    fi
    
    if [[ " ${cmd_list[@]} " =~ " $COMMAND " ]]; then
        delay "$COMMAND" 10
        log "$COMMAND" "INFO" "Arguments: \"$MOC_PRICES_SOURCE_ARGS\""
        "/usr/local/bin/$COMMAND" $MOC_PRICES_SOURCE_ARGS
    else
        log "moc_prices_source" "CRITICAL" "COMMAND env variable ($COMMAND) is not in the allowed list (${cmd_list[@]})"
        exit 1
    fi
}



# Script
main
