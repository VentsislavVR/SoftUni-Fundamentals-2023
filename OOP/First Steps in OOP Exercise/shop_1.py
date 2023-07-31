class Shop:
    def __init__(self,name:str,items:list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
billa = Shop("billa",["item1","item2"])
print(shop.items)
print(billa.items)
print(billa.get_items_count())
