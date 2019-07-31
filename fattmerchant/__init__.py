#test tanmay
from __future__ import absolute_import
name = u"fattmerchant"
import logging.config 
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)),
 u'logging.config')
logging.config.fileConfig(log_file_path,
                          disable_existing_loggers=False)
