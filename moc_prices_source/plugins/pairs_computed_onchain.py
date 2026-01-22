from .chains import chain, EVM
from .base import CoinPair, Formula, register_pairs
from .pairs import BTC_USD
from .base import get_addr_env, Decimal
from ..types import PercentageDecimal



### Computed onchain pairs

class BTC_USD_24h_Formula(Formula):

    max_steps = 2
    evm: EVM = chain.rsk_mainnet.evm
    oracle_addr = get_addr_env('BTC_USD_ORACLE_ADDR',
                               '0xe2927A0620b82A66D67F678FC9b826B0E01B1bFD')
    coinpair = BTC_USD
    hours: int = 24

    __doc__ = (f"({coinpair}@NOW - {coinpair}@{hours}hAGO)"
               f" / {coinpair}@{hours}hAGO")

    def step_run(self, value, step, btc_usd):
        if step==1:
            self.block = self.evm.latest_block_number - int(
                3600 * self.hours / 25)
            self.call_id = self.evm.multicall.add_call(
                contract_address = self.oracle_addr,
                fn_spec = 'peek()(bytes32,bool)')
            self._namespace = f"{self.hours}h ago"
            self.evm.multicall.reset_executed_once(self._namespace)
        else: # final step
            self.evm.multicall.run_only_first_time(
                block_identifier = self.block,
                namespace = self._namespace)
            value_b, ok = self.evm.multicall.get_call(
                self.call_id, namespace = self._namespace)
            if ok:
                btc_usd_before = Decimal(int(value_b.hex(), 16)
                                         )/Decimal(10**18)
            else:
                raise ValueError('invalid or expired price')
            return PercentageDecimal((btc_usd - btc_usd_before) / btc_usd_before)


BTC_USD_24h = CoinPair(
    name = "BTC/USD(24h)",
    short_description = "test",
    requirements = [BTC_USD],
    formula = BTC_USD_24h_Formula)


register_pairs()
