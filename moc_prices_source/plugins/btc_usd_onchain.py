from .pairs import BTC_USD_OCH
from .base import BaseOnChain, engine_register, get_addr_env, EVM, Decimal



@engine_register()
class Engine(BaseOnChain):

    _description = "MOC onchain"
    _coinpair = BTC_USD_OCH
    _addr = get_addr_env('BTC_USD_ORACLE_ADDR',
                         '0xe2927A0620b82A66D67F678FC9b826B0E01B1bFD')

    def _get_value_from_evm(self, evm: EVM):
        value, str_error = None, None
        value_b, ok = evm.call(self._addr, 'peek()(bytes32,bool)')
        if ok:
            value = Decimal(int(value_b.hex(), 16))/Decimal(10**18)
        else:
            str_error = 'invalid or expired price'
        return value, str_error
