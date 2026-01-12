from .pairs import BPRO_BTC
from .base import BaseOnChain, engine_register, get_env, Decimal, Address



@engine_register()
class Engine(BaseOnChain):

    _description   = "MOC onchain"
    _coinpair = BPRO_BTC
    _uri = get_env('RSK_NODE', 'https://public-node.rsk.co')
    _sc_addr = get_env('MOC_STATE_ADDR',
                       '0xb9C42EFc8ec54490a37cA91c423F7285Fa01e257',
                       cast=Address)

    def _get_price(self):

        str_error = None
        value = None

        try:
            evm = self.make_evm_with_uri()
            value_wei = evm.call(self._sc_addr, 'bproTecPrice()(uint256)')
            value = Decimal(value_wei)/Decimal(10**18)
        except Exception as e:
            str_error = str(e)

        if value is None:
            self._error = str_error
        
        return value
