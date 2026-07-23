from ...pairs.onchain import DOC_USD_TEC
from ...base import BaseOnChain, Engines, EVM, Decimal
from ...chains import chain


if chain.rsk_mainnet.enabled:

    @Engines.register_decorator()
    class Engine(BaseOnChain):

        _description = "DOC/USD onchain"
        _coinpair = DOC_USD_TEC
        _addr = '0x6a343488338b944c6FCc89906646Fac1e8e91cE5'

        def _get_value_from_evm(self, evm: EVM):
            value, str_error = None, None
            value_b, ok = evm.call(self._addr, 'peek()(bytes32,bool)')
            if ok:
                value = Decimal(int(value_b.hex(), 16))/Decimal(10**18)
            else:
                str_error = 'invalid or expired price'
            return value, str_error
