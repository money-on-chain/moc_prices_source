from ...pairs.special import RIF_BTC_MP1P
from .base import EngineBinance, Engines, Decimal, uri
from .rif_btc_binance import Engine as RifBtcEngine



factor = 0.01

@Engines.register_decorator()
class Engine(EngineBinance):

    _uri = uri(symbol="RIFBTC", path="api/v3/depth")
    _uri_failover = uri(symbol="RIFBTC", failover=True, path="api/v3/depth")
    _coinpair = RIF_BTC_MP1P


    def __call__(self):
        price_engine = RifBtcEngine()
        ok = price_engine()
        self._error = price_engine.error
        self.base_price = price_engine.price
        if ok:
            ok = EngineBinance.__call__(self)
        return ok


    def _map(self, data):

        value = Decimal(0)

        if 'bids' in data.keys() and 'asks' in data.keys():
            lv = []
            for t in ['asks', 'bids']:
                data[t].sort(reverse=(t=='bids'))
                v = Decimal('0')
                for p, q in data[t]:
                    p, q = Decimal(str(p)), Decimal(str(q))
                    d = abs((self.base_price / p) - Decimal('1'))
                    if d>=Decimal(str(factor)):
                        q = Decimal('1')
                    v += (q*p)
                    if d>=Decimal(str(factor)):
                        break
                lv.append(v)
            value = min(lv)

        return {
            'price':  value}
