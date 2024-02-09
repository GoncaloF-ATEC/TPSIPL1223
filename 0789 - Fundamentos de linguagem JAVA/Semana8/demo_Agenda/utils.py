from datetime import datetime
class Log:
    def add_error(erro:str, msg:str):
        file = open("ErrorLog.csv", "a")
        msgErro = f"{datetime.now()};{erro};{msg}"
        file.write(msgErro + "\n")
        file.close()

class myException(Exception):
    def __init__(self, msg):
        Log.add_error(self.__class__.__name__, msg)
        super().__init__(msg)


class DataError(myException):
    pass

class divZero(myException):
    pass