class Pizza:
    def __init__(self,size,topping,crust):
        self.size = size
        self.topping = topping
        self.crust = crust

    def __repr__(self):
        return f"Pizza(size='{self.size}', topping='{self.topping}', crust='{self.crust}')"
    

class PizzaOven:
    _instance = None

    def __new__(cls, temp =200):
        if cls._instance is None:
            # create the instance only once
            cls._instance = super().__new__(cls)
            cls._instance.temp = temp
            print(f"🔥 New oven created at {temp}°C")
        else:
            print("♻️ Returning existing oven instance")
        return cls._instance

    def bake(self, pizza):
        print(f"{pizza.size} , {pizza.topping} , {pizza.crust}")


pizza1 = Pizza("large", "pepperoni", "thin")
pizza2 = Pizza("medium", "veggie", "thick")

oven1 = PizzaOven(300)
oven2 = PizzaOven(400)

print(oven1 is oven2)   # True — both refer to the same instance

oven1.bake(pizza1)
oven2.bake(pizza2)