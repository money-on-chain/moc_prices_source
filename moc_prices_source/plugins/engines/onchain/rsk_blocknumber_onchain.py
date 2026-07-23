from ...pairs.special import BLOCK_RSK
from ...base import BaseOnChain, Engines, EVM
from ...chains import chain


if chain.rsk_mainnet.enabled:

    @Engines.register_decorator()
    class Engine(BaseOnChain):

        _description = "RSK onchain"
        _coinpair = BLOCK_RSK

        def _get_value_from_evm(self, evm: EVM):
            value = evm.latest_block_number
            return value, None # (value, str_error)
