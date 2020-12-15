from engine_base import Base, RIF_BTC


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "RSK_3"
    _uri         = "http://134.209.68.142:3000"
    _coinpair    = RIF_BTC

    def _map(self, data):
        return {
            'price': data['price']}


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(engine)
