#!/usr/bin/env bash
redis-server --save "" --appendonly no > /dev/null 2>&1 &
sleep 10
/usr/local/bin/moc_prices_source_check
