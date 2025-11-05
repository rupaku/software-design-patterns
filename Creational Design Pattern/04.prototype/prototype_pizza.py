import copy

class Pizza:
    def __init__(self, size , crust , toppings = None):
        self.size = size
        self.crust = crust
        self.toppings = None or []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"Pizza(size='{self.size}', crust='{self.crust}', toppings={self.toppings})"
    
base_pizza = Pizza("regular","thin",["tomato","onion"])

veggie_pizza = base_pizza.clone()
veggie_pizza.add_topping("capsicum")

cheese_pizza = base_pizza.clone()
cheese_pizza.add_topping("cheese")

print("Pizza ordered")
print(base_pizza)
print(veggie_pizza)
print(cheese_pizza)