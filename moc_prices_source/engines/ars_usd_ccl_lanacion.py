from engine_base import Base, ARS_USD_CCL
from decimal     import Decimal


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "LaNacion.com.ar"
    _uri         = "https://api-contenidos.lanacion.com.ar/json/V3/economia/cotizacionblue/DCCL"
    _coinpair    = ARS_USD_CCL
    _max_age     = 3600 #1h

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
