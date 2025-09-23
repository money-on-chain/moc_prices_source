from engine_base import Base, USDT_USD


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "Kraken"
    _uri         = "https://api.kraken.com/0/public/Ticker?pair=USDTUSD"
    _coinpair    = USDT_USD

    def _map(self, data):
        keys = list(data['result'].keys())
        if 1==len(keys):
            return {
                'price':  data['result'][keys[0]]['c'][0],
                'volume': data['result'][keys[0]]['v'][1] }


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(engine)
    if engine.error:
        print(engine.error)
