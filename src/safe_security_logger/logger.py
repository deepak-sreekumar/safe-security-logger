import logging
import sys

__author__ = "deepak.s@safe.security"
__copyright__ = "deepak.s@safe.security"
__license__ = "MIT"

import logging

from pythonjsonlogger import jsonlogger


def getLogger(name):
    logger = logging.getLogger(name)

    # Logs will be written to console
    console_handler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(message)s %(name)s %(module)s %(funcName)s ",
        rename_fields={
            "levelname": "level",
            "asctime": "timestamp",
            "funcName": "functionName",
            "name": "loggerName",
        },
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # default level would be INFO
    logger.setLevel(logging.INFO)
    return logger
