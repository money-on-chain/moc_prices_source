from .simple import RIF_USDT_MA, BTC_USD
from .onchain import DOC_USD_TEC, DOC_USD_TEC_TEST
from ..chains import EVM, chain
from ..base import CoinPairs, CoinPair, Formula, Decimal
from ...types import PercentageDecimal, Yes, No
from ...evm import Address

### Computed onchain pairs

# BTC_USD_24h
if chain.rsk_mainnet.enabled and \
    chain.rsk_mainnet.btc_usd_oracle_addr!=Address(0):

    class BTC_USD_24h_Formula(Formula):

        evm: EVM = chain.rsk_mainnet.evm
        oracle_addr = chain.rsk_mainnet.btc_usd_oracle_addr
        coinpair = BTC_USD
        requirements = [coinpair]
        hours: int = 24

        __doc__ = (f"({coinpair}@NOW - {coinpair}@{hours}hAGO)"
                f" / {coinpair}@{hours}hAGO")

        def init(self, btc_usd):
            self.block = (self.evm.latest_block_number
                        - int(3600 * self.hours / 25))
            self.call_id = self.evm.multicall.add_call(
                self.oracle_addr, 'peek()(bytes32,bool)')
            self._namespace = f"{self.hours}h ago"

        def step(self, value, btc_usd):
            self.evm.multicall.run_only_first_time(
                block_identifier = self.block,
                namespace = self._namespace)
            value_b, ok = self.evm.multicall.get_call(
                self.call_id, namespace = self._namespace)
            if ok:
                btc_usd_before = (Decimal(int(value_b.hex(), 16))
                                / Decimal(10**18))
            else:
                raise ValueError('invalid or expired price')
            return PercentageDecimal((btc_usd - btc_usd_before)
                                     / btc_usd_before)
        
        def cleanup(self):
            self.evm.multicall.clear_calls()

    BTC_USD_24h = CoinPair(
        name = "BTC/USD(24h)",
        description = "BTC/USD percentage difference over 24 hours",
        requirements = BTC_USD_24h_Formula.requirements,
        formula = BTC_USD_24h_Formula)


class ISLIQ_ROC_Formula(Formula):
    evm: EVM = ...
    roc_mcg_addr = ...
    roc_mcg_addr_env = ...
    requirements = ...

    fn_list = ['readyToLiquidate(uint256[][])(bool)',
               'readyToMicroLiquidate(uint256[][])(bool)']

    def init(self, rif_usd, doc_usd):
                       
        wei = lambda value: int(value * Decimal("1e18"))

        call_args = [[wei(rif_usd)], [wei(doc_usd)]]
        
        self.call_ids = []
        for fn_spec in self.fn_list:
            self.call_ids.append(
                self.evm.multicall.add_call(self.roc_mcg_addr, fn_spec, call_args)
            )
        
    def step(self, *args):
        self.evm.multicall.run_only_first_time()
        values = list(map(self.evm.multicall.get_call, self.call_ids))

        if all([ans is not None for ans in values]):
            return Yes if any(values) else No
        else:
            env = self.roc_mcg_addr_env
            addr = Address(self.roc_mcg_addr).make_abbreviation(sep='...')
            fn_list = [f"{fn.split('(')[0]}(...)" for v, fn in zip(
                values, self.fn_list) if v is None]
            fn_str = (' and '.join([', '.join(fn_list[:-1]), fn_list[-1]]
                                   ) if len(fn_list)>1 else fn_list[-1])
            msg = (f"Error calling {fn_str} in multiCollateralGuard({addr}). "
                   f"Maybe the address passed by the {env} environment "
                   "variable is incorrect.")
            raise ValueError(msg)

    def cleanup(self):
        self.evm.multicall.clear_calls()


# ISLIQ_ROC
if chain.rsk_mainnet.enabled and chain.rsk_mainnet.roc_mcg_addr!=Address(0):

    class ISLIQ_ROC_MAIN_Formula(ISLIQ_ROC_Formula):
        """
            MultiCollateralGuard.readyToLiquidate([
                [rif_usdt_ma],
                [doc_usd_tec]
            ])
        """

        evm: EVM = chain.rsk_mainnet.evm
        roc_mcg_addr = chain.rsk_mainnet.roc_mcg_addr
        roc_mcg_addr_env = chain.rsk_mainnet.env.roc_mcg_addr.name
        requirements = [RIF_USDT_MA, DOC_USD_TEC]

    ISLIQ_ROC = CoinPair(
        name="ISLIQ_ROC",
        short_description = "If RoC is in liquidation (mainnet)",
        requirements = ISLIQ_ROC_MAIN_Formula.requirements,
        formula = ISLIQ_ROC_MAIN_Formula)


# ISLIQ_ROC_TEST
if chain.rsk_testnet.enabled and chain.rsk_testnet.roc_mcg_addr!=Address(0):

    class ISLIQ_ROC_TEST_Formula(ISLIQ_ROC_Formula):
        """
            MultiCollateralGuardTestnet.readyToLiquidate([
                [rif_usdt_ma],
                [doc_usd_tec_test]
            ])
        """

        evm: EVM = chain.rsk_testnet.evm
        roc_mcg_addr = chain.rsk_testnet.roc_mcg_addr
        roc_mcg_addr_env = chain.rsk_testnet.env.roc_mcg_addr.name
        requirements = [RIF_USDT_MA, DOC_USD_TEC_TEST]
    
    ISLIQ_ROC_TEST = CoinPair(
        name="ISLIQ_ROC",
        variant="test",
        short_description = "If RoC is in liquidation (testnet)",
        requirements = ISLIQ_ROC_TEST_Formula.requirements,
        formula = ISLIQ_ROC_TEST_Formula)


CoinPairs.register()
