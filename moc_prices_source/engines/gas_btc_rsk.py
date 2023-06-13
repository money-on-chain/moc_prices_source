from engine_base import BaseOnChain, GAS_BTC, get_env, Decimal



class Engine(BaseOnChain):

    _name          = BaseOnChain._name_from_file(__file__)
    _description   = "RSK onchain"
    _coinpair      = GAS_BTC
    _uri           = get_env('RSK_NODE', 'https://public-node.rsk.co')


    def _get_price(self):

        try:
            value = self.make_web3_obj_with_uri().eth.gas_price
        except Exception as e:
            self._error = str(e)
            return None
        if value:
            return Decimal(value) / (10**18)
        else:
            self._error = f"No gas price value given from {self._uri}"
            return None




if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    if engine.error:
        print(f"{engine} Error: {engine.error}")
    else:
        print(engine)
