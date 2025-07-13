class Store:
    def __init__(self):
        self.items  = []
    def add_item(self,item):
        self.items.append(item)
    def show_all(self):
        for item in self.items:
            print(item)
    def filter_item(self,name):
        ITEM_FOUND = False
        for item in self.items:
            if name == item['name']:
                print("============ ITEM IS AVAILABLE===========")
                print(item)
                ITEM_FOUND = True
                break
        
        if ITEM_FOUND== False:
            print('ITEM NOT AVAILABLE')
            

ITEM_ID_START_POINT = 100
ITEM_DATA = [
    {
        "name":"pocket",
        "price":200,
        "category":"pockets",
        "quantiy":10
    },
    {
        "name":"silicon pockets",
        "price":1000,
        "category":"pockets",
        "quantiy":10
    },
    {
        "name":"boalt",
        "price":4000,
        "category":"watches",
        "quantiy":10
    }
]
store = Store()

for index, item in enumerate(ITEM_DATA):
    item.update({"id":index + ITEM_ID_START_POINT})
    store.add_item(item)
store.show_all()
store.filter_item('silicon pockets')


