from engine_base import Base, ARS_USD
from decimal     import Decimal


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "Ambito.com"
    _uri         = "https://mercados.ambito.com/dolar/informal/variacion"
    _coinpair    = ARS_USD

    def _map(self, data):
        values = [data['compra'], data['venta']]
        values = list(map(lambda x: Decimal(str(x).replace(',', '.')), values))
        value = sum(values)/len(values)
        return {
            'price':  value
        }


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(engine)
