import logging.config

from os import path, getenv
from json import load


def setup_logging(
    default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'
):
    """
    Setup logging configuration
    """
    value = getenv(env_key, None)
    log_path = default_path if value is None else value

    root_path = path.dirname(path.abspath(__file__))
    log_config_path = path.join(root_path, log_path)

    info_log_path = path.join(path.dirname(root_path), 'logs/info.log')
    error_log_path = path.join(path.dirname(root_path), 'logs/error.log')

    if path.exists(log_config_path):
        with open(log_config_path, 'rt') as f:
            config = load(f)
        config['handlers']['info_file']['filename'] = info_log_path
        config['handlers']['error_file']['filename'] = error_log_path
        logging.config.dictConfig(config)

    else:
        logging.basicConfig(level=default_level)


setup_logging()
