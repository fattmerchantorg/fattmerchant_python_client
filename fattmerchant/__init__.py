name = "fattmerchant"
import logging.config 
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)),
 'logging.config')
logging.config.fileConfig(log_file_path,
                          disable_existing_loggers=False)