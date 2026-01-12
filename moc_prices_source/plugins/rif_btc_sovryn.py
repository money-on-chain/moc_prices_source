from .pairs import RIF_BTC
from .base import BaseOnChain, engine_register, get_env



@engine_register()
class Engine(BaseOnChain):

    _description = "Sovryn onchain"
    _coinpair = RIF_BTC
    _uri = get_env('RSK_NODE', 'https://public-node.rsk.co')
    _pool_sc_addr = '0x65528e06371635a338ca804cd65958a11cb11009'
    _wrbtc_tk_addr = '0x542fda317318ebf1d3deaf76e0b632741a7e677d'
    _rif_tk_addr = '0x2acc95758f8b5f583470ba265eb685a8f45fc9d5'

    def _get_price(self):

        str_error = None
        value = None

        try:            

            evm = self.make_evm_with_uri()

            rif_reserve = evm.call(self._rif_tk_addr,
                                   'balanceOf(address)(uint256)',
                                   self._pool_sc_addr)

            btc_reserve = evm.call(self._wrbtc_tk_addr,
                                   'balanceOf(address)(uint256)',
                                   self._pool_sc_addr)
            
            value = btc_reserve/rif_reserve

        except Exception as e:
            str_error = str(e)

        if value is None:
            self._error = str_error
        
        return value
