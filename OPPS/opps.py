class Item:
    pay_rate = 0.8 #pay rate after 20% dicount
    all = []
    def __init__(self, name: str, price: float, quantity):
        print(f"An instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not a valid value."
        assert quantity >= 0, f"Quantity {quantity} is not a valid value."

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
#item1.apply_discount()
#print(item1.price)

item2 = Item("Laptop", 1000, 3)
#item2.pay_rate = 0.7
#item2.apply_discount()
#print(item2.price)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

#print(Item.__dict__)   #all attributes for class level
#print(item1.__dict__)  #all attributes for instance level
print(Item.all)
#for instance in Item.all:
   # print(instance.name)

