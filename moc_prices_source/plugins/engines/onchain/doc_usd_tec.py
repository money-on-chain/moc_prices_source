from ...pairs.onchain import DOC_USD_TEC
from ...base import BaseOnChain, Engines, get_addr_env, EVM, Decimal
from ...chains import chain

@Engines.register_decorator()
class Engine(BaseOnChain):
    per_env_evm: EVM = chain.rsk_mainnet.evm
    price_provider_addr = '0x6a343488338b944c6FCc89906646Fac1e8e91cE5'
    _description = "DOC/USD onchain"
    _coinpair = DOC_USD_TEC

    def _get_value_from_evm(self, evm: EVM):
        (value_wei, _) = self.per_env_evm.call(self.price_provider_addr, 'peek()(bytes32,bool)')
        value = Decimal(int.from_bytes(value_wei))/Decimal(10**18)
        return value, None # (value, str_error)
