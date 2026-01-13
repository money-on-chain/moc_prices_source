from .base import Coin, register_coins



BTC = Coin('Bitcoin', 'btc', '₿')
USD = Coin('Dollar', 'usd', '$')
RIF = Coin('RIF Token', 'rif')
MOC = Coin('MOC Token', 'moc')
ETH = Coin('Ether', 'eth', '⟠')
USDT = Coin('Tether', 'usdt', '₮')
BNB = Coin('Binance Coin', 'bnb', 'Ƀ')
ARS = Coin('Peso Argentino', 'ars', '$')
MXN = Coin('Peso Mexicano', 'mxn', '$')
COP = Coin('Peso Colombiano','cop', '$')
GAS = Coin('Gas', 'gas')
BPRO = Coin('Bpro', 'bpro')
DOC = Coin('DOC Token', 'doc')

register_coins()
