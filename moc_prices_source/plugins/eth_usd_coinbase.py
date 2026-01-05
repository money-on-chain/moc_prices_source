from .pairs import ETH_USD
from .base import Base, engine_register



@engine_register()
class Engine(Base):

    _description = "Coinbase"
    _uri = "https://api.coinbase.com/v2/prices/ETH-USD/spot"
    _coinpair = ETH_USD

    def _map(self, data):
        return {
            'price': data['data']['amount']
            }
