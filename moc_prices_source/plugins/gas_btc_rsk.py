from .pairs import GAS_BTC
from .base import BaseOnChain, engine_register, Decimal



@engine_register()
class Engine(BaseOnChain):

    _description = "RSK onchain"
    _coinpair = GAS_BTC
    _max = 2*(10**10) #20Gwei


    def _get_price(self):

        try:
            eth = self.make_web3_obj_with_uri().eth
        except Exception as e:
            self._error = str(e)
            return None

        # Fix: backcompatibility with various web3 versions
        value = None
        attributes = ['gas_price', 'gasPrice']
        not_get = True
        for g in attributes:
            if hasattr(eth, g):
                try:
                    value = getattr(eth, g)
                except Exception as e:
                    self._error = str(e)
                    return None
                not_get = False
                break
        if not_get:
            self._error = f"'Eth' object has none of these attributes: {', '.join(map(repr, attributes))}"
            return None

        if not value:
            self._error = f"No gas price value given from {self._uri}"
            return None
        elif value >= self._max:
            self._error = f"Gas price value >= {self._max}"
            return None
        else:
            return Decimal(value) / (10**18)
