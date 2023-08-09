from  logger_module.loggerUtils import Logger

#Testing from subfolder

applogger = Logger(__name__) 
def mylogstatement():
    applogger.LogInfo('Database successfully connected', functionName="mylogstatement()", SessionID="12345")
    applogger.LogInfo('Database successfully connected', functionName="mylogstatement()", CustomerID="A123")
    applogger.LogInfo('Database successfully connected without functionaName',  SessionID="6789")
    applogger.LogInfo('Database successfully connected without any params')

def mylogserrortatement():
    applogger.LogError('Database failed', functionName="mylogstatement()", SessionID="12345")
    applogger.LogError('Database connection error', functionName="mylogstatement()", CustomerID="A123")
    applogger.LogError('Database not successfully connected without functionaName',  SessionID="6789")
    applogger.LogError('Database not successfully connected without any params')
    
    try:
        i=0
        j=10/i

    except:
        applogger.LogError('Division by zero error', functionName="MyFun")
    

    try:
        s1='Hello'
        s2 = s2+8

    except Exception as exp :
        applogger.LogError('String assignment  error',exc_info=exp)
        

# try:
#     # Some Code.... 

# except:
#     # optional block
#     # Handling of exception (if required)

# else:
#     # execute if no exception

# finally:
#     # Some code .....(always executed)


#Raising Exception
# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print ("An exception")
#     raise  # To determine whether the exception was raised or not
