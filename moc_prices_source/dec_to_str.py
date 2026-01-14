from decimal import Decimal
from typing import Any



def dec_to_str(value: Any) -> str: 
    
    if not isinstance(value, Decimal):
        return value
    
    out = f"{value:,.6f}"
        
    if out=="0.000000":
        out = f"{value}"
        if 'E-' in out:
            out = out.split('E-')
            out[1] = ''.join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[int(i)] for i in out[1]])
            out = f"{float(out[0]):.3f} × 10⁻{out[1]}"                
    
    return out