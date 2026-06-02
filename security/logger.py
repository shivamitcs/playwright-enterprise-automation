import logging


def get_logger():
    logger = logging.getLogger("automation")

    logger.setLevel(logging.INFO)

    return logger
