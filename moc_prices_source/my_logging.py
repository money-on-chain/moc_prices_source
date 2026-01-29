from logging import addLevelName, basicConfig
from logging import getLogger as original_get_logger
from logging import INFO, WARNING, CRITICAL, DEBUG
from types import MethodType
from .my_envs import envs



# Add some levels
VERBOSE = INFO - 5
OFF = 100
addLevelName(OFF, "OFF")
addLevelName(VERBOSE, "VERBOSE")
def log_level(x, default = OFF):
    return {
        "OFF": OFF, "CRITICAL": CRITICAL, "WARNING": WARNING,
        "INFO": INFO, "VERBOSE": VERBOSE,"DEBUG": DEBUG,
        str(OFF): OFF, str(CRITICAL): CRITICAL, str(WARNING): WARNING,
        str(INFO): INFO, str(VERBOSE): VERBOSE, str(DEBUG): DEBUG
    }.get(str(x).upper().strip(), default)
DEFAULT_LOG_LEVEL = envs("MOC_PRICES_LOG_LEVEL", "OFF", log_level)


# Default config
basicConfig(
    level = DEFAULT_LOG_LEVEL,
    format = '%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S')


def get_logger(name):
    logger = original_get_logger(name)
    def verbose(self, *args, **kargs):
        return logger.log(VERBOSE, *args, **kargs) 
    logger.verbose = MethodType(verbose, logger)
    return logger


def set_level(level=INFO):
    root = get_logger(None)
    root.setLevel(level)
    for h in root.handlers:
        h.setLevel(level)
    str_level = {
        OFF: "OFF",
        CRITICAL: "CRITICAL",
        WARNING: "WARNING",
        INFO: "INFO",
        VERBOSE: "VERBOSE",
        DEBUG: "DEBUG"
    }.get(level, f"#{level}")
    root.verbose(f"Logging level set to {str_level}")


class WithLogger():

    @property
    def _logger(self):
        cls = self.__class__
        return get_logger(
            f"{cls.__module__}.{cls.__qualname__}"
        )