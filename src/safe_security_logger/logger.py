import argparse
import logging
import sys

__author__ = "deepak.s@sasfe.security"
__copyright__ = "deepak.s@safe.security"
__license__ = "MIT"

import logging
import os.path
import traceback

from pythonjsonlogger import jsonlogger


def getLogger(name):
    logger = logging.getLogger(name)

    # Logs will be written to console
    console_handler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(name)s %(levelname)s  %(message)s  %(module)s %(funcName)s "
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # default level would be INFO
    logger.setLevel(logging.INFO)
    return logger
