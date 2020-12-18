from engine_base import Base, RIF_BTC


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "RSK_2"
    _uri         = "http://64.225.31.252:3000"
    _coinpair    = RIF_BTC

    def _map(self, data):
        return {
            'price': data['price']}


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(engine)