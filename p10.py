class Inventory:
    def __init__(self):
        self.items={}


    def add_item(self ,name ,qty,price):
        self.items[name]=(qty,price)



    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named { name}")
        del self.items[name]




    def total_value(self):
        total=0


        for qty,price in self.items.values():
                                     total+=qty * price


        return total
 


        
    def __len__(self):
        return len(self.items)


inventory=Inventory()
with open ("stock.txt") as file:
    for line in file:
        name,qty,price=line.strip().split(",")



        try:
            qty=int(qty)
            price=int(price)

            inventory.add_item(name,qty,price)
        except ValueError:
            print(f"skipping {name}: bad number")
 


print(f"{len(inventory)} items, total value {inventory.total_value()}")
inventory.remove_item("pen")
print(f"{len(inventory)} items, total value {inventory.total_value()}")
try:
    inventory.remove_item("laptop")
except KeyError as e:
    print("Error: ", e)


