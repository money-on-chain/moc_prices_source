import pkgutil, traceback, importlib
from pathlib import Path
from .base import Engines, CoinPairs, Coins

_pkg_dir = Path(__file__).parent

for module_info in pkgutil.iter_modules([str(_pkg_dir)]):
    name = module_info.name
    if name in ("__main__", "base"):
        continue
    try:
        importlib.import_module(f"{__name__}.{name}")
    except Exception:
        traceback.print_exc()


__all__ = ["Engines", "CoinPairs", "Coins"]
