# Chain of responsibility pattern
from abc import ABC, abstractmethod
class LogData:
    def __init__(self,handler=None):
        self.handler = handler
    @abstractmethod
    def handle(self,data):
       raise NotImplementedError("Subclasses must implement 'handle' method")
class Error(LogData):
    def handle(self,data):
        if data['type'] =='error':
            print("Error")
        else:
            return self.handler.handle(data)

class WarnError(LogData):
    def handle(self,data):
        if data['type'] =='warn':
            print("warn")
        else:
            return self.handler.handle(data)
class DebuggError(LogData):
    def handle(self, data):
            if data['type']=='debug':
                 print("error debbuger")
                 return
            return self.handler.handle(data)

class NormalLog(LogData):
    def handle(self,data):
            print(data)

e = Error(WarnError(DebuggError(NormalLog())))

e.handle({"type":"error"})
e.handle({"type":"warn"})
e.handle({"type":"debug"})
e.handle({"type":"normal"})
