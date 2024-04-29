#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
make --directory=../ clean
make --directory=../ build
TARFILE=$(ls -d ../dist/*.tar.gz)
cp $TARFILE files/moneyonchain_prices_source.tar.gz
make --directory=../ clean
sudo docker build -t moc_prices_source -f Dockerfile .
