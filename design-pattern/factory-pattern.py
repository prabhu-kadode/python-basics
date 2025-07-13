from abc import ABC, abstractmethod
class DATABase(ABC):
    @abstractmethod
    def connect(self):
        pass
class MysqlDataBase(DATABase):
    def __init__(self):
        print("MysqlDataBase")
    def connect(self):
        print('connecting mysql...')
class PostgressDataBase(DATABase): 
    def __init__(self):
        print("PostgressDataBase")
    def connect(self):
        print('connecting postgress...')
class OracleDataBase(DATABase): 
    def __init__(self):
        print("OracleDataBase")
    def connect(self):
        print('connecting oracle')

class DataBasefactory:
    def __init__(self):
        pass
    def get_connecxtion(self,dbname):
        if dbname =='mysql':
            return MysqlDataBase()
        elif dbname =='postgress':
            return PostgressDataBase()
        elif dbname =='oracle':
            return OracleDataBase()
        else:
            return ValueError("Ubknown database name")
try:
    db = DataBasefactory()
    conn = db.get_connecxtion('oracle')
    conn.connect()
except:
    print("Error while connecting")


