from .pairs import MOC_BTC_SOV
from .base import BaseOnChain, engine_register, EVM, Decimal



@engine_register()
class Engine(BaseOnChain):

    _description = "Sovryn onchain"
    _coinpair = MOC_BTC_SOV
    _pool_sc_addr = '0xe321442dc4793c17f41fe3fb192a856a4864ceaf'
    _wrbtc_tk_addr = '0x542fda317318ebf1d3deaf76e0b632741a7e677d'
    _moc_tk_addr = '0x9ac7fe28967b30e3a4e6e03286d715b42b453d10'

    def _get_value_from_evm(self, evm: EVM):
        moc_reserve = evm.call(self._moc_tk_addr,
                               'balanceOf(address)(uint256)',
                               self._pool_sc_addr)
        btc_reserve = evm.call(self._wrbtc_tk_addr,
                               'balanceOf(address)(uint256)',
                               self._pool_sc_addr)
        value = Decimal(btc_reserve/moc_reserve)
        return value, None # (value, str_error)