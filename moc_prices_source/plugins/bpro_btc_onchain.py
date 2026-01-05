from .pairs import BPRO_BTC
from .base import BaseOnChain, engine_register, get_env, Decimal



moc_sc_addr_options = {
    'mainnet': '0xb9C42EFc8ec54490a37cA91c423F7285Fa01e257', 
}

simplified_abi = """
[
  {
    "constant": true,
    "inputs": [],
    "name": "bproTecPrice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
]
"""

@engine_register()
class Engine(BaseOnChain):

    _description   = "MOC onchain"
    _coinpair = BPRO_BTC
    _uri = get_env('RSK_NODE', 'https://public-node.rsk.co')
    _sc_addr = get_env('MOC_STATE_ADDR', 'mainnet')

    def _get_price(self):

        sc_addr = self.to_checksum_address(
            moc_sc_addr_options.get(
                self._sc_addr.lower().strip(),
                self._sc_addr.lower().strip()
            )
        )

        str_error = None
        value = None
        try:            
            w3 = self.make_web3_obj_with_uri()
            sc = w3.eth.contract(address=sc_addr, abi=simplified_abi)
            value = Decimal(int(sc.functions.bproTecPrice().call())
                            )/Decimal(10**18)
        except Exception as e:
            str_error = str(e)

        if value is None:
            self._error = str_error
        
        return value
