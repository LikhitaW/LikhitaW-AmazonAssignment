import logging
from utilities.fileFunctionUtil import FileFunctionUtil
import os
class LogGen:

    @staticmethod
    def loggen():

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        log_dir = FileFunctionUtil.get_dynamic_path("AmazonAssignment") + "/logs/"
        log_file = "automation.log"
        log_path = os.path.join(log_dir, log_file)

        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.INFO)

        log_formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(log_formatter)

        logger.addHandler(file_handler)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)

        return logger






