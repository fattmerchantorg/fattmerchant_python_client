from __future__ import absolute_import

import logging.config

from os import path, getenv
from json import load


def setup_logging(
    default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'
):
    """
    Setup logging configuration
    """
    log_path = default_path
    value = getenv(env_key, None)

    if value:
        log_path = value

    log_path = path.join(path.dirname(path.abspath(__file__)), log_path)

    if path.exists(log_path):
        with open(log_path, 'rt') as f:
            config = load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


setup_logging()
