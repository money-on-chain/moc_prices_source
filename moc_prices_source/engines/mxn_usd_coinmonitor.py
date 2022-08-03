from engine_base import Base, MXN_USD


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "CoinMonitor.info"
    _uri         = "https://mx.coinmonitor.info/data_ar_chart_DOLAR.json"
    _coinpair    = MXN_USD
    
    _max_age                       = 3600 # 1hs.
    _max_time_without_price_change = 0    # zero means infinity
    _ssl_verify                    = False

    def _map(self, data):
        return {
            'price':  data[0][1]
        }


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(engine)
    if engine.error:
        print(engine.error)
