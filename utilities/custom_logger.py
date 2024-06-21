import inspect
import logging


def Get_Logger(log_level):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # fileHandler = logging.FileHandler("logfile1.log")
    fileHandler = logging.FileHandler("logfile.log")
    logger.setLevel(log_level)
    formatter = logging.Formatter("%(asctime)s %(levelname)s - %(name)s - %(funcName)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
