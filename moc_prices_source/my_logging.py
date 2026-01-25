from logging import addLevelName, basicConfig
from logging import getLogger as original_get_logger
from logging import INFO, WARNING, CRITICAL, DEBUG
from types import MethodType



# Add some levels
VERBOSE = INFO - 5
OFF = 100
addLevelName(OFF, "OFF")
addLevelName(VERBOSE, "VERBOSE")


# Default config
basicConfig(
    level = OFF,
    format = '%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S')


def get_logger(name):
    logger = original_get_logger(name)
    def verbose(self, *args, **kargs):
        return logger.log(VERBOSE, *args, **kargs) 
    logger.verbose = MethodType(verbose, logger)
    return logger


def set_level(level=INFO):
    root = original_get_logger()
    root.setLevel(level)
    for h in root.handlers:
        h.setLevel(level)


class WithLogger():

    @property
    def _logger(self):
        cls = self.__class__
        return get_logger(
            f"{cls.__module__}.{cls.__qualname__}"
        )