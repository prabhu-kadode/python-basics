class RealBank:
    def __init__(self):
        pass
    def deposit(self,amount):
        print("Deposit...",amount)
    def widhraw(self,amount):
        print("Deposit...",amount)
class ProxyBank:
    def __init__(self,bank):
        self.bank = bank
    def deposit(self,amount):
        if self.authenticate(1):
            self.bank.deposit(amount)
        else:
            ValueError("Error in authenticate")
    def widhraw(self,amount):
        self.bank.widhraw(amount)
    def authenticate(self,account):
        return False
realBank = RealBank()
proxy = ProxyBank(realBank)
proxy.deposit(100)

