import logging
import sys

from logger_module import logger_configuration

class Logger:
    def __init__(self, moduleName='App'):
        self.logger = logger_configuration.getLogger()
        self.moduleName=moduleName
                  
    def LogInfo(self,message,functionName='Func',**kwargs):
        self.message=message
        self.functionName=functionName
        message= self.constructLogMessage(kwargs)
        self.logger.info(message)
        
    def LogError(self,message, functionName='Func', exc_info=None, **kwargs):
        self.message=message
        self.functionName=functionName
        message= self.constructLogMessage(kwargs, exc_info)
        self.logger.error(message)

    def constructLogMessage(self,kwargs, exc_info=None):
        myAllowedAdditionalParams=[]
        returnValue= self.moduleName + ' - ' + self.functionName + ' - '+ self.message
        
        print(str(exc_info))
        if exc_info:
            returnValue=returnValue + ' - ' + str(exc_info)

        for key, value in kwargs.items():
            if (key=='SessionID'):
                myAllowedAdditionalParams.append(key +':'+ value)
            elif (key=='CustomerID'):
                myAllowedAdditionalParams.append(key +':'+ value)
        
        if  myAllowedAdditionalParams:
            returnValue = returnValue + ' - [Additional Params -  '+  ' - '.join(myAllowedAdditionalParams) + ']'
                
        return returnValue       
