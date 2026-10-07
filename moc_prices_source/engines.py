import concurrent.futures
from .my_logging import get_logger
from .plugins import Engines

all_engines = {}
session_storage = {}
modules_names = Engines.keys()

for name in modules_names:
    locals()[name] = Engines[name](session_storage=session_storage)
    all_engines[name] = locals()[name]
    del name

del modules_names


def get_coinpair_list():
    engines_list = all_engines.values()
    coinpair_list = [ engine.coinpair for engine in engines_list ]
    coinpair_list = list(set(coinpair_list))
    coinpair_list.sort()
    return coinpair_list


def get_engines_names():
    engines_list = all_engines.values()
    engines_names = [ engine.name for engine in engines_list ]
    engines_names.sort()
    return engines_names


def get_prices(coinpairs=None, engines_names=None, engines_list=None):

    if engines_list is None: 
        engines_list = []

    assert isinstance(engines_list, (list, str))
    if not engines_list:
        engines_list = all_engines.values()

    if engines_names:
        assert isinstance(engines_names, (list, str))
        engines_list = [ e for e in engines_list if (
            e.name in engines_names or e.description in engines_names) ]

    if coinpairs:
        assert isinstance(coinpairs, (list, str))
        engines_list = [ e for e in engines_list if (
            e.coinpair in coinpairs) ]

    if not engines_list:
        return []

    log = get_logger(__name__)
    stack = engines_list[:]
    retries_remaining = 1

    while stack:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(stack)) as executor:
            futures = {executor.submit(engine): engine for engine in stack}
            for future, engine in futures.items():
                try:
                    future.result()
                except Exception as error:
                    engine._clean_output_values()
                    engine._error = f"Engine error ({type(error).__name__})"
                    log.warning("Engine %s failed with %s", engine.name,
                                type(error).__name__)

        new_stack = []
        for engine in stack:
            d = engine.as_dict
            if d['price'] not in [True, False] and not(d['price']) and d['ok']:
                if retries_remaining:
                    new_stack.append(engine)
                else:
                    engine._error = "No price after retry"
                    log.warning("Engine %s returned no price after retry",
                                engine.name)
        stack = new_stack
        retries_remaining -= 1

    return [ engine.as_dict for engine in engines_list ]
