logger_module is subfolder which need to be placed at app root level. logger_module
app/
logger_module/


logger_config.conf => contains configuration for python logging

logger_configuration.py => need to import in main-app file and invoke setupLoggerforApp only once
examples :

    #if in same folder eg. logger_module
    import logger_configuration as myapplog_config
    or 
    # in different folder
    import logger_module.logger_configuration  as myapplog_config


in app.py

myapplog_config.setupLoggerforApp()
applogger = logger.Logger(__name__)