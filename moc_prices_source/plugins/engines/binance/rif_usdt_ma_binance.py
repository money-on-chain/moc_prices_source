from typing import Dict, List, Any, Optional
from ...pairs.simple import RIF_USDT_MA
from .base import EngineBinance, Engines, Decimal, uri, envs


# Some params
max_quantity = Decimal(envs.value_of('RIF_USD_MA_DEPTH'))
allow_degraded = envs('MA_ALLOW_DEGRADED', False, bool)

@Engines.register_decorator()
class Engine(EngineBinance):

    _uri = uri(symbol="RIFUSDT", path="api/v3/depth")
    _uri_failover = uri(symbol="RIFUSDT", failover=True, path="api/v3/depth")
    _coinpair = RIF_USDT_MA
    _max_quantity = max_quantity
    _allow_degraded = allow_degraded


    def _map(self, data: Dict[str, List[List[Any]]]
             ) -> Dict[str, Optional[Decimal]]:
        """
        Compute DWAP up to self._max_quantity on both sides of the order book.

        Expected input:
            data = {
                "asks": [[price, qty], ...],  # best ask (unsorted)
                "bids": [[price, qty], ...],  # best bid (unsorted)
            }
        
        Reference in `docs/fundamentals/dwap.md`
        """
        types_ = ['asks', 'bids']
        if all(map(lambda t: isinstance(data.get(t), list
                                        ) and data.get(t), types_)):
            total = Decimal('0')
            values = []
            max_quantity = self._max_quantity
            for type_ in types_:
                data[type_].sort(reverse=(type_=='bids'))
                spent, accumulated = Decimal('0'), Decimal('0')
                for x in data[type_]:
                    price, quantity = list(map(Decimal, x))
                    if (accumulated + quantity) >= max_quantity:
                        quantity = max_quantity - accumulated
                    accumulated += quantity
                    if accumulated >= max_quantity:
                        break               
                if accumulated<max_quantity:
                    max_quantity=accumulated
            for type_ in types_:
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
            degraded = bool(max_quantity<self._max_quantity)
            if self._allow_degraded or not(degraded):
                return {'price': (sum(values)/total)/max_quantity}
