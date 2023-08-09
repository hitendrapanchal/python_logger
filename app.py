import logging
import logger_module.logger_configuration  as myapplog_config
import logger_module.loggerUtils  as logger
from loggertest.mylogtest import mylogstatement, mylogserrortatement


myapplog_config.setupLoggerforApp()
applogger = logger.Logger(__name__)

def logger_testing2(value):
    applogger.LogInfo('Hello from logging2 : ' + value)

if __name__ == '__main__':
    logger_testing2('myvalue')
    mylogstatement()
    mylogserrortatement()