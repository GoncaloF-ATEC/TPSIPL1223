from datetime import datetime
class Log:
    def add_error(erro:str, msg:str):
        file = open("ErrorLog.txt", "a")
        msgErro = f"{datetime.now()}\t{erro}\t{msg}"
        file.write("\n" + msgErro)
        file.close()

class myException(Exception):
    def __init__(self, msg):
        Log.add_error(erro=self.__class__.__name__, msg=msg)
        super().__init__(msg)


class DataError(myException):
    pass

class divZero(myException):
    pass