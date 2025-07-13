from abc import ABC, abstractmethod
class DataBase(ABC):
    @abstractmethod
    def connect(sefl):
        pass
class MongodbLagecy:
    def start_connect(self):
        print("Mongodb connection.....")
class MongodbAdaptor(DataBase):
    def __init__(self,adaptee:MongodbLagecy):
        self.adaptee = adaptee
    def connect(self):
        self.adaptee.start_connect()
mongo = MongodbLagecy()
conn = MongodbAdaptor(mongo)
conn.connect()