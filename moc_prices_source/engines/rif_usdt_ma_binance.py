from engine_base import BaseWithFailover, RIF_USDT_MA
from decimal import Decimal

base_uri = "https://{}/api/v3/depth?symbol=RIFUSDT"
max_quantity = Decimal('100000')

class Engine(BaseWithFailover):

    _name         = BaseWithFailover._name_from_file(__file__)
    _description  = "Binance"
    _uri          = base_uri.format("api.binance.com")
    _uri_failover = base_uri.format("moc-proxy-api-binance.moneyonchain.com")
    _coinpair     = RIF_USDT_MA
    _max_time_without_price_change = 0 # zero means infinity


    def _map(self, data):
        types_ = ['asks', 'bids']
        if all(map(lambda t: isinstance(data.get(t), list) and data.get(t), types_)):
            total = Decimal('0')
            values = []
            for type_ in types_:
                data[type_].sort(reverse=(type_=='bids'))
                spent, accumulated = Decimal('0'), Decimal('0')
                for x in data[type_]:
                    price, quantity = list(map(Decimal, x))
                    if (accumulated + quantity) >= max_quantity:
                        quantity = max_quantity - accumulated
                    spent += price * quantity
                    accumulated += quantity
                    if accumulated >= max_quantity:
                        break               
                total += accumulated
                values.append(spent * accumulated)
            return {'price': (sum(values)/total)/max_quantity}


if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    engine = Engine()
    engine()
    print(f"URI = {repr(engine.uri)}")
    print()
    print(engine)
    print()
    if engine.error:
        print()
        print(engine.error)
        print()
