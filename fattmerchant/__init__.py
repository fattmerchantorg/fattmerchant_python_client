import logging.config

from os import path

name = "fattmerchant"

file_dir = path.split(path.realpath(__file__))[0]
logging.config.fileConfig(path.join(file_dir, 'logging.config'),
                          disable_existing_loggers=False)
