from engine_base import Base, MXN_USD
from decimal     import Decimal


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "Wise.com"
    _uri         = "https://wise.com/rates/history+live?source=USD&target=MXN&length=1&resolution=hourly&unit=day"
    _coinpair    = MXN_USD

    _max_age                       = 3600 # 1hs.
    _max_time_without_price_change = 0    # zero means infinity

    def _map(self, data):
        value = Decimal(str(data[-1]['value']))
        return {
            'price':  value
        }


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(engine)
    if engine.error:
        print(engine.error)
