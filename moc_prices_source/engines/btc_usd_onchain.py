from engine_base import BaseOnChain, BTC_USD_OCH, get_env
from decimal import Decimal



btc_usd_oracle_addr_options = {
    'mainnet': '0xe2927A0620b82A66D67F678FC9b826B0E01B1bFD', 
}

oracle_simplified_abi = """
  [
    {
      "constant": true,
      "inputs": [],
      "name": "peek",
      "outputs": [
        {
          "name": "",
          "type": "bytes32"
        },
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
  ]
"""

class Engine(BaseOnChain):

    _name          = BaseOnChain._name_from_file(__file__)
    _description   = "MOC onchain"
    _coinpair      = BTC_USD_OCH
    _uri           = get_env('RSK_NODE', 'https://public-node.rsk.co')
    _oracle_addr   = get_env('BTC_USD_ORACLE_ADDR', 'mainnet')

    def _get_price(self):

        oracle_addr = self.to_checksum_address(
            btc_usd_oracle_addr_options.get(
                self._oracle_addr.lower().strip(),
                self._oracle_addr.lower().strip()
            )
        )

        try:            

            w3 = self.make_web3_obj_with_uri()

            oracle = w3.eth.contract(address=oracle_addr, abi=oracle_simplified_abi)

            value, ok = oracle.functions.peek().call()

            if not ok:
                self._error = 'invalid or expired price'
                return None

            value = Decimal(int(value.hex(), 16))/Decimal(10**18)
            
            return value

        except Exception as e:
            self._error = str(e)
            return None


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    if engine.error:
        print(f"{engine} Error: {engine.error}")
    else:
        print(engine)
