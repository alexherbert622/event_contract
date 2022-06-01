import inspect
import logging

import allure
import pytest


@pytest.mark.usefixtures("setup")
class Baseclass:
    def loggerdemo(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        File_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        File_handler.setFormatter(formatter)
        logger.addHandler(File_handler)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.ERROR)
        return logger