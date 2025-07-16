from abc import ABC, abstractmethod

class MakeBewarage(ABC):
    def start_making(self):
        self.boil_water()
        self.add_sugar()
        self.add_condiments()
    def boil_water(self):
        print('boiling water..')
    def add_sugar(self):
        print('adding sugar..')
    @abstractmethod
    def add_condiments(self):
        pass
class Tea(MakeBewarage):
    def add_condiments(self):
        print('Adding Lemon')
class Coffee(MakeBewarage):
    def add_condiments(self):
        print('Adding milk')
tea = Tea()
tea.start_making()