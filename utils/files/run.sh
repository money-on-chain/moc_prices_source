#!/usr/bin/env bash
redis-server --save "" --appendonly no > /dev/null 2>&1 &
sleep 10
while /usr/local/bin/moc_prices_source_to_db $MOC_PRICES_SOURCE_ARGS
do
  sleep 10
done
