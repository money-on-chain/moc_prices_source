from ...pairs.onchain import DOC_USD_TEC_TEST
from ...base import BaseOnChain, Engines, EVM, Decimal
from ...chains import chain


if chain.rsk_testnet.enabled: 

    @Engines.register_decorator()
    class Engine(BaseOnChain):

        _evm: EVM = chain.rsk_testnet.evm
        _description = "DOC/USD onchain (testnet)"
        _coinpair = DOC_USD_TEC_TEST
        _addr = '0xaeB119cF080FDD668E6Ba845f663912C473778F8'

        def _get_value_from_evm(self, evm: EVM):
            value, str_error = None, None
            value_b, ok = evm.call(self._addr, 'peek()(bytes32,bool)')
            if ok:
                value = Decimal(int(value_b.hex(), 16))/Decimal(10**18)
            else:
                str_error = 'invalid or expired price'
            return value, str_error