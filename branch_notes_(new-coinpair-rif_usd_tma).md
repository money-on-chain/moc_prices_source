# Notes related to the branch `new-coinpair-rif_usd_tma` purpose

## Add `RIF/USD(TMA)` and `RIF/USD(TBMA)` coinpairs to be used by *RIF on chain*


### Description

Define a new computed coinpair `RIF/USD(TMA)` that reuses the Binance *“magic average”* orderbook-depth source for `RIF/USDT(MA)` as the base quote. Then multiply that value by the live `USDT/USD` conversion so the resulting price in `USD` reflects any deviation of `USDT` from its peg. The suffix **TMA** indicates that the price is obtained through (T)ether and ultimately relies on the (M)agic (A)verage mechanism.

Define an other new computed coinpair `RIF/USD(TBMA)` that reuses the Binance *“magic average”* orderbook-depth source for `RIF/USDT(MA)` as the base quote. Then multiply that value by the live `USDT/USD(B)` conversion so the resulting price in `USD` reflects any deviation of `USDT` from its peg. The suffix **TBMA** indicates that the price is obtained through (T)ether, (B)itcoin and ultimately relies on the (M)agic (A)verage mechanism.

`USDT/USD(B)` = `BTC/USD` ÷ `BTC/USDT`


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
user@workstation:~/code/moc_prices_source$ ./moc_prices_source_check --computed | grep "RIF/USD(T"
RIF/USD(TB)      =  rif_usdt * btc_usd / btc_usdt
RIF/USD(T)       =  rif_usdt * usdt_usd
RIF/USD(TBMA)    =  rif_usdt_ma * btc_usd / btc_usdt
RIF/USD(TMA)     =  rif_usdt_ma * usdt_usd
user@workstation:~/code/moc_prices_source$
```

```shell
user@workstation:~/code/moc_prices_source$ ./moc_prices_source_check "RIF/USD(T*MA)"

From       To      V.    Exchnage    Response        Weight    %  Time
---------  ------  ----  ----------  ------------  --------  ---  ------
Bitcoin    Dollar        Bitfinex    $ 117.62000K      0.18   18  0.3s
Bitcoin    Dollar        Bitstamp    $ 117.67900K      0.22   22  0.92s
Bitcoin    Dollar        Coinbase    $ 117.67200K      0.25   25  0.6s
Bitcoin    Dollar        Gemini      $ 117.68816K      0.17   17  0.9s
Bitcoin    Dollar        Kraken      $ 117.68760K      0.18   18  0.45s
Bitcoin    Tether        Binance     ₮ 117.63868K      0.8    80  0.41s
Bitcoin    Tether        Bitfinex    ₮ 117.62000K      0.05    5  0.3s
Bitcoin    Tether        Coinbase    ₮ 117.62834K      0.1    10  0.58s
Bitcoin    Tether        Kraken      ₮ 117.59030K      0.05    5  0.45s
RIF Token  Tether  MA    Binance     ₮  63.52933m      1     100  0.42s
Tether     Dollar        Bitstamp    $   1.00027       0.15   15  0.91s
Tether     Dollar        Coinbase    $   1.00040       0.45   45  0.93s
Tether     Dollar        Kraken      $   1.00031       0.4    40  0.47s

    Coin pair              Mediam            Mean    Weighted median   Sources    Ok
--  -------------  --------------  --------------  -----------------  ---------  ----
↓   BTC/USD        117,679.000000  117,669.351000     117,679.000000   5 of 5     ✓
↓   BTC/USDT       117,624.170000  117,619.330000     117,635.834118   4 of 4     ✓
ƒ   RIF/USD(TBMA)        0.063559        0.063556           0.063553     N/A      ✓
ƒ   RIF/USD(TMA)         0.063549        0.063550           0.063549     N/A      ✓
↓   RIF/USDT(MA)         0.063529        0.063529           0.063529   1 of 1     ✓
↓   USDT/USD             1.000310        1.000325           1.000310   3 of 3     ✓

Response time 0.93s

user@workstation:~/code/moc_prices_source$ 
```


### ToDo list

- [x] Add `RIF/USD(TMA)` coinpair
- [x] Bump Beta version to 0.7.4b10
- [x] Put pair `RIF/USD(TMA)` under monitoring as soon as possible
- [x] Add `RIF/USD(TBMA)` coinpair
- [x] Bump Beta version to 0.7.4b11
- [x] Put pair `RIF/USD(TBMA)` under monitoring as soon as possible
- [x] Verify and validate price sources and their weights for pair `USDT/USD` 
- [x] Bump Beta version to 0.7.4b12
- [x] Update monitoring as soon as possible to see the impact of changing weights
- [x] Verify and validate price sources and their weights for pair `BTC/USDT` 
- [x] Bump Beta version to 0.7.4b13
- [x] Update monitoring as soon as possible to see the impact of changing weights
- [ ] Verify and validate the depth used in the order book for pair `RIF/USDT(MA)` 
- [ ] Fix Bybit API ban from U.S.A.  
- [ ] Decide whether to use `RIF/USD(TMA)` or `RIF/USD(TBMA)` coinpair as the final for `RIF/USD`
- [ ] Delete this file (`branch_notes_(new-coinpair-rif_usd_tma).md`) before merging to develop

