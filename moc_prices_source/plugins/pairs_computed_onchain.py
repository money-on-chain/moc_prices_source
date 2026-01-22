from .chains import chain, EVM
from .base import CoinPair, Formula, register_pairs
from .pairs import BTC_ARS, BTC_COP, BTC_USD
from .pairs_onchain import BPRO_BTC
from .base import get_addr_env, Decimal
from ..types import PercentageDecimal, Yes, No
from ..evm import addr_zero
import random



### Computed onchain pairs

class BTC_USD_24h_Formula(Formula):

    max_steps = 3
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
                self.oracle_addr, 'peek()(bytes32,bool)')
            self._namespace = f"{self.hours}h ago"
            self.evm.multicall.reset_executed_once(self._namespace)
        elif step==2:
            self.evm.multicall.run_only_first_time(
                block_identifier = self.block,
                namespace = self._namespace)
            value_b, ok = self.evm.multicall.get_call(
                self.call_id, namespace = self._namespace)
            if ok:
                self.btc_usd_before = Decimal(int(value_b.hex(), 16)
                                              )/Decimal(10**18)
            else:
                raise ValueError('invalid or expired price')
        else:
            self.evm.multicall.clear_calls()
            return PercentageDecimal((btc_usd - self.btc_usd_before
                                      ) / self.btc_usd_before)


BTC_USD_24h = CoinPair(
    name = "BTC/USD(24h)",
    short_description = "test",
    requirements = [BTC_USD],
    formula = BTC_USD_24h_Formula)


requirements_flip = [BTC_ARS, BTC_COP, BTC_USD, BPRO_BTC]

class ISLIQ_FLIP_Formula(Formula):
    """
        MultiCollateralGuard.readyToLiquidate([
            [bpro_ars, bpro_cop],
            [usd_ars, usd_cop]
        ])
    """

    evm: EVM = chain.rsk_mainnet.evm
    mcg_addr = get_addr_env(
        'MULTI_COLLATERAL_GUARD_ADDR',
        addr_zero)
    
    max_steps = 3

    def step_run(self, value, step, btc_ars, btc_cop, btc_usd, bpro_btc):
        if step==1:
            
            wei = lambda value: int(value * Decimal("1e18"))

            usd_ars = wei(btc_ars / btc_usd)
            usd_cop = wei(btc_cop / btc_usd)
            bpro_ars =  wei(bpro_btc * btc_ars)
            bpro_cop = wei(bpro_btc * btc_cop)
            
            ...
            fn_spec = 'readyToLiquidate(uint256[][])(bool)' or \
                'readyToMicroLiquidate(uint256[][])(bool)'
            call_args = [
                    [bpro_ars, bpro_cop],
                    [usd_ars, usd_cop]
                ]
            self.call_id = self.evm.multicall.add_call(
                self.mcg_addr, fn_spec, call_args)
            ...
            
            self.evm.multicall.reset_executed_once()
        elif step==2:
            self.evm.multicall.run_only_first_time()
            
            ...
            #self.out_value = self.evm.multicall.get_call(self.call_id)
            self.out_value = random.randint(1, 10) == 1
            ...
            
        else:
            self.evm.multicall.clear_calls()
            if self.out_value is None:
                return None
            return Yes if self.out_value else No


ISLIQ_FLIP = CoinPair(
    name="ISLIQ_FLIP",
    short_description = "If FLip is in liquidation (mainnet)",
    requirements = requirements_flip,
    formula = ISLIQ_FLIP_Formula)


class ISLIQ_FLIP_TEST_Formula(ISLIQ_FLIP_Formula):
    """
        MultiCollateralGuardTestnet.readyToLiquidate([
            [bpro_ars, bpro_cop],
            [usd_ars, usd_cop]
        ])
    """

    evm: EVM = chain.rsk_testnet.evm
    mcg_addr = get_addr_env(
        'MULTI_COLLATERAL_GUARD_TESTNET_ADDR',
        addr_zero)


ISLIQ_FLIP_TEST = CoinPair(
    name="ISLIQ_FLIP",
    variant="test",
    short_description = "If FLip is in liquidation (testnet)",
    requirements = requirements_flip,
    formula = ISLIQ_FLIP_TEST_Formula)


register_pairs()
