class Prodcut:
    def __init__(self,name,price):
        self.name= name
        self.price = price
    def get_price(self):
        return self.price
class TaxDecorator:
    def __init__(self,wrapped,tax):
        self.wrapped = wrapped
        self.tax = tax
    def get_price(self):
        price = self.wrapped.get_price()
        print('Base price is:',price)
        print('Total after tax',price+self.tax)
        return price + self.tax
class GSTTax:
    def __init__(self,wrapped,tax):
        self.wrapped = wrapped
        self.tax = tax
    def get_price(self):
        price = self.wrapped.get_price()
        print('Total after gst',price+self.tax)
        return price + self.tax
product = Prodcut('laptop',1000)
taxDecorator = TaxDecorator(product,10)
gSTTax = GSTTax(taxDecorator,10)

print(gSTTax.get_price())

medicine = Prodcut('Medicine',1000)
medicinetax = TaxDecorator(medicine,10)
print(medicinetax.get_price())



