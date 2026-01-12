from .pairs import MOC_USD_OKU
from .base import BaseOnChain, engine_register, get_env, Decimal, Address



@engine_register()
class Engine(BaseOnChain):

    _description = "Oku onchain"
    _coinpair = MOC_USD_OKU
    _uri = get_env('RSK_NODE', 'https://public-node.rsk.co')
    _oracle_addr = get_env('MOC_BTC_ORACLE_ADDR',
                           '0x11683439c9509C135ee4F7bB6e23835e1d86ECBA',
                           cast=Address)

    def _get_price(self):

        str_error = None
        value = None

        try:
            evm = self.make_evm_with_uri()
            value_b, ok = evm.call(self._oracle_addr, 'peek()(bytes32,bool)')
            if ok:
                value = Decimal(int(value_b.hex(), 16))/Decimal(10**18)
            else:
                str_error = 'invalid or expired price'
        except Exception as e:
            str_error = str(e)

        if value is None:
            self._error = str_error
        
        return value
