# Notes related to the branch `new-coinpair-rif_usd_tma` purpose

## Add `RIF/USD(TMA)` coinpair to be used by *RIF on chain*


### Description

Define a new computed coinpair `RIF/USD(TMA)` that reuses the Binance *“magic average”* orderbook-depth source for `RIF/USDT(MA)` as the base quote. Then multiply that value by the live `USDT/USD` conversion so the resulting price in `USD` reflects any deviation of `USDT` from its peg. The suffix **TMA** indicates that the price is obtained through (T)ether and ultimately relies on the (M)agic (A)verage mechanism.


### Examples using the `CLI-Tool`

```shell
user@workstation:~/code/moc_prices_source$ ./moc_prices_source_check --help
Usage: moc_prices_source_check [OPTIONS] [COINPAIRS_FILTER]

  Description:
      CLI-type tool that shows the data obtained by
      the `moc_price_source` library.   
      Useful for troubleshooting.

  COINPAIRS_FILTER:
      Is a display pairs filter that accepts wildcards.
      Example: "btc*"
      Default value: "*" (all available pairs)

Options:
  -v, --version                   Show version and exit.
  -j, --json                      Show data in JSON format and exit.
  -w, --weighing                  Show the default weighing and exit.
  -c, --computed                  Show the computed pairs formula and exit.
  -s, --summary                   Show the summary and exit.
  -m, --markdown                  Set markdown for the summary format.
  -n, --not-ignore-zero-weighing  Not ignore sources with zero weighing.
  -h, --help                      Show this message and exit.
user@workstation:~/code/moc_prices_source$
```

```shell
user@workstation:~/code/moc_prices_source$ ./moc_prices_source_check --computed | grep "RIF/USD(TMA)"
RIF/USD(TMA)     =  rif_usdt_ma * usdt_usd
user@workstation:~/code/moc_prices_source$
```

```shell
user@workstation:~/code/moc_prices_source$ ./moc_prices_source_check "RIF/USD(TMA)"

From       To      V.    Exchnage    Response        Weight    %  Time
---------  ------  ----  ----------  ------------  --------  ---  ------
RIF Token  Tether  MA    Binance     ₮  60.45920m      1     100  0.37s
Tether     Dollar        Bitstamp    $   1.00035       0.15   15  0.77s
Tether     Dollar        Coinbase    $   1.00042       0.45   45  0.58s
Tether     Dollar        Kraken      $   1.00028       0.4    40  0.47s

    Coin pair       Mediam      Mean    Weighted median   Sources    Ok
--  ------------  --------  --------  -----------------  ---------  ----
ƒ   RIF/USD(TMA)   0.06048   0.06048            0.06048     N/A      ✓
↓   RIF/USDT(MA)  0.060459  0.060459           0.060459   1 of 1     ✓
↓   USDT/USD       1.00035   1.00035            1.00035   3 of 3     ✓

Response time 0.78s

user@workstation:~/code/moc_prices_source$ 
```


### ToDo list

- [x] Add `RIF/USD(TMA)` coinpair
- [ ] Bump Beta version to 0.7.4b10
- [ ] Put pair `RIF/USD(TMA)` under monitoring as soon as possible
- [ ] Verify and validate price sources and their weights for pair `USDT/USD`
- [ ] Verify and validate the depth used in the order book for pair `RIF/USDT(MA)`

