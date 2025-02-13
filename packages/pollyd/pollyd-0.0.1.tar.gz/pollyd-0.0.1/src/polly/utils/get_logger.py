import logging

from polly.config import ConfigHandler


def get_logger(name, config: ConfigHandler):
    logging.basicConfig(level=config.logging_mode)

    logger = logging.getLogger(name)
    return logger
