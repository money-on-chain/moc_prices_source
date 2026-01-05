from .pairs import MOC_BTC_SOV
from .base import BaseOnChain, engine_register, get_env



@engine_register()
class Engine(BaseOnChain):

    _description = "Sovryn onchain"
    _coinpair = MOC_BTC_SOV
    _uri = get_env('RSK_NODE', 'https://public-node.rsk.co')
    _pool_sc_addr = '0xe321442dc4793c17f41fe3fb192a856a4864ceaf'
    _wrbtc_tk_addr = '0x542fda317318ebf1d3deaf76e0b632741a7e677d'
    _moc_tk_addr = '0x9ac7fe28967b30e3a4e6e03286d715b42b453d10'

    def _get_price(self):

        pool_sc_addr = self.to_checksum_address(self._pool_sc_addr)
        wrbtc_tk_addr = self.to_checksum_address(self._wrbtc_tk_addr)
        moc_tk_addr = self.to_checksum_address(self._moc_tk_addr)

        str_error = None
        value = None

        try:
            
            w3 = self.make_web3_obj_with_uri()

            moc_token = w3.eth.contract(address=moc_tk_addr, abi=self.erc20_simplified_abi)
            wrbtc_token = w3.eth.contract(address=wrbtc_tk_addr, abi=self.erc20_simplified_abi)

            moc_reserve = moc_token.functions.balanceOf(pool_sc_addr).call()
            btc_reserve = wrbtc_token.functions.balanceOf(pool_sc_addr).call()

            value = btc_reserve/moc_reserve

        except Exception as e:
            str_error = str(e)

        if value is None:
            self._error = str_error
        
        return value
