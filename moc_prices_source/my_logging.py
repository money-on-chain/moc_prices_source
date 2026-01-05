import logging, types
from logging import INFO, WARNING, CRITICAL, DEBUG
from os.path import basename

VERBOSE = INFO - 5

def make_log(name, level = VERBOSE):

    logging.addLevelName(VERBOSE, "VERBOSE")

    logging.basicConfig(
        level   = level,
        format  = '%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger(name)

    def verbose(self, *args, **kargs):
        return logger.log(VERBOSE, *args, **kargs) 

    logger.verbose = types.MethodType(verbose, logger)

    return logger
