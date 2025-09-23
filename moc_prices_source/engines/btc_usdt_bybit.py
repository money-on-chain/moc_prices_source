from engine_base import Base, BTC_USDT, Decimal


class Engine(Base):

    _name        = Base._name_from_file(__file__)
    _description = "Bybit"
    _uri         = "https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT"
    _coinpair    = BTC_USDT

    def _map(self, data):
        data = data['result']['list'][0]        
        return {
            'price': (Decimal(data['bid1Price']) +
                      Decimal(data['ask1Price'])) / Decimal('2')
        }


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(engine)
    if engine.error:
        print(engine.error)
