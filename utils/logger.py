import logging


def setup_logger():
    logger = logging.getLogger("api_test")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("logs/test_log.html")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('<p>%(asctime)s - %(levelname)s - %(message)s</p>', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
