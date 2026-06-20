from ...pairs.onchain import DOC_USD_TEC_TEST
from ...base import BaseOnChain, Engines, get_addr_env, EVM, Decimal
from ...chains import chain

@Engines.register_decorator()
class Engine(BaseOnChain):
    per_env_evm: EVM = chain.rsk_testnet.evm
    price_provider_addr = '0xaeB119cF080FDD668E6Ba845f663912C473778F8'
    _description = "DOC/USD onchain (testnet)"
    _coinpair = DOC_USD_TEC_TEST

    def _get_value_from_evm(self, evm: EVM):
        (value_wei, _) = self.per_env_evm.call(self.price_provider_addr, 'peek()(bytes32,bool)')
        value = Decimal(int.from_bytes(value_wei))/Decimal(10**18)
        return value, None # (value, str_error)
