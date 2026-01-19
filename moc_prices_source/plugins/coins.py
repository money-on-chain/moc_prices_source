from .base import Coin, register_coins



BTC = Coin('Bitcoin', 'btc', '₿')
USD = Coin('Dollar', 'usd', '$')
RIF = Coin('RIF', 'rif')
MOC = Coin('MOC', 'moc')
ETH = Coin('Ether', 'eth', '⟠')
USDT = Coin('Tether', 'usdt', '₮')
BNB = Coin('BinanceCoin', 'bnb', 'Ƀ')
ARS = Coin('Peso Arg.', 'ars', '$')
MXN = Coin('Peso Mex.', 'mxn', '$')
COP = Coin('Peso Col.','cop', '$')
GAS = Coin('Gas', 'gas')
BPRO = Coin('BPro', 'bpro')
DOC = Coin('DOC', 'doc')

register_coins()
