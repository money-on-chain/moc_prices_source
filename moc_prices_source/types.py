from json import dumps as base_json_dumps
from json import loads as json_loads
from decimal import Decimal, ROUND_HALF_UP
from typing import Any
from datetime import timedelta



class Serializable():
    
    serializable_class = str
    _frozen = True
    
    @property
    def as_serializable(self):
        return self.serializable_class(self)
    
    @as_serializable.setter
    def as_serializable(self, value):
        if self._frozen:
            self._attribute_error()
        if not(isinstance(value, self.serializable_class)):
            raise ValueError(f"value must be {self.serializable_class.__name__}")
        self._set_new_value(value)

    @staticmethod
    def _attribute_error():
        raise AttributeError("can't set attribute")

    def _set_new_value(self, value):
        self._attribute_error()    


class SerializableDecimal(Decimal, Serializable):
    serializable_class = float


class FancyDecimal(SerializableDecimal):

    def __new__(cls, value):
        return super().__new__(cls, value)

    def __str__(self) -> str:
        value = Decimal(self)
        out = f"{value:,.6f}"
        if out=="0.000000":
            out = f"{value}"
            if 'E-' in out:
                out = out.split('E-')
                out[1] = ''.join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[int(i)] for i in out[1]])
                out = f"{float(out[0]):.3f} × 10⁻{out[1]}"
        return out        


class PercentageDecimal(SerializableDecimal):

    UP_SYMBOL = "▲"
    DOWN_SYMBOL = "▼"
    ZERO_SYMBOL = "~"

    def __new__(cls, value):
        return super().__new__(cls, value)

    def __str__(self) -> str:
        
        percent_value = (self * Decimal("100")).quantize(
            Decimal("0.00"),
            rounding=ROUND_HALF_UP,
        )

        if percent_value > 0:
            symbol = self.UP_SYMBOL
            value = percent_value
        elif percent_value < 0:
            symbol = self.DOWN_SYMBOL
            value = abs(percent_value)
        else:
            symbol = self.ZERO_SYMBOL
            value = percent_value

        return f"{symbol} {value:.2f}%"


class Bool(Serializable):

    serializable_class = bool
    TRUE_TEXT = "true"
    FALSE_TEXT = "false"

    def __init__(self, value: bool, frozen: bool = False):
        self._value = bool(value)
        self._frozen = bool(frozen)

    def __bool__(self):
        return self._value

    def __repr__(self):
        return self.TRUE_TEXT if self._value else self.FALSE_TEXT
    
    def __int__(self):
        return 1 if self._value else 0
    
    def __float__(self):
        return 1.0 if self._value else 0.0
    
    def _set_new_value(self, value):
        self._value = bool(value)


class YesNo(Bool):

    TRUE_TEXT = "Yes"
    FALSE_TEXT = "No"


Yes = YesNo(True, frozen = True)


No = YesNo(False, frozen = True)


def json_dumps(obj: Any,
               indent = 4,
               sort_keys = True) -> str:

    def clean_keys(obj):
        """keys must be str, int, float, bool or None"""
        if isinstance(obj, dict):
            new_dict = {}
            for key, value in obj.items():
                if isinstance(key, (str, int, float, bool)) or key is None:
                    safe_key = key
                else:
                    safe_key = str(key)
                new_dict[safe_key] = clean_keys(value)
            return new_dict
        elif isinstance(obj, list):
            return [clean_keys(item) for item in obj]
        elif isinstance(obj, tuple):
            return tuple(clean_keys(item) for item in obj)
        elif isinstance(obj, set):
            return [clean_keys(item) for item in obj]  # JSON has no sets
        else:
            return obj

    def default(value):
        if isinstance(value, Serializable):
            value: Serializable
            return value.as_serializable
        elif isinstance(value, timedelta):
            value: timedelta
            return value.seconds + value.microseconds/1000000        
        elif isinstance(value, Decimal):
            value: Decimal
            return float(value)
        return str(value)

    obj = clean_keys(obj)

    return base_json_dumps(obj,
                           default = default,
                           indent = indent,
                           sort_keys = sort_keys)


def normalize_obj(obj: Any) -> Any:
    return json_loads(json_dumps(obj))
