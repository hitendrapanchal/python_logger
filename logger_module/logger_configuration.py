import time
import logging
import os
from logging import config as logging_config

#levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

logger = logging.getLogger()

def getLogger():
    return logger

def setupLoggerforApp():
    here = os.path.abspath(os.path.dirname(__file__))
    LOGGING_CONFIG = os.path.abspath(os.path.join(here, 'logger.conf'))
    #LOGGING_CONFIG='logger.conf'
    logging_config.fileConfig(LOGGING_CONFIG)

# #main setup function which will configure logger 
# def setupLogger():
#     file_handler=addHandler('FILE')
#     logger.addHandler(file_handler)
#     setLogLevel(file_handler)
#     setLogformatter(file_handler)

# #handler could be file/stream
# def setLogLevel(handler):
#     handler.setLevel(logging.WARNING)
#     handler.setLevel(logging.ERROR)
    
# def setLogformatter(handler):
#     my_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#     handler.setFormatter(my_format)
 
# def addHandler(handler_name):
#     handler=None
#     if handler_name == 'CONSOLE':
#         handler=addStreamHandler()
#     elif handler_name == 'FILE':
#         handler=addFileHandler()
#     elif handler_name == "STREAM":
#         handler=addStreamHandler()
#     elif handler_name == "DATABASE":
#         handler=addStreamHandler()
#     else:
#         handler=addStreamHandler()

#     return handler 


# def addFileHandler(filename):
#     return logging.FileHandler(filename)
    
   
# def addStreamHandler():
#     return logging.StreamHandler()
    