#!/usr/bin/env bash
BIN_DIR=/app/venv/bin
redis-server --save "" --appendonly no > /dev/null 2>&1 &
sleep 10
$BIN_DIR/moc_prices_source_check --version
