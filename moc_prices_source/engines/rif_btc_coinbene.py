from engine_base import Base, RIF_BTC


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "Coinbene"
    _uri         = "http://api.coinbene.com/v1/market/ticker?symbol=RIFBTC"
    _coinpair    = RIF_BTC

    def _map(self, data):
        return {
            'price':  data['ticker'][0]['last'],
            'volume': data['ticker'][0]['24hrVol'] }


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(engine)
