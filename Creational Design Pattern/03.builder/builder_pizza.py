class Pizza:
    def __init__(self,size,topping,crust):
        self.size = size
        self.topping = topping
        self.crust = crust

    def __repr__(self):
        return f"Pizza(size='{self.size}', topping='{self.topping}', crust='{self.crust}')"
    
class PizzaBuilder:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._size = 200
        self._topping = "tomato"
        self._crust ="thin"
        return self
    
    def size(self, v):
        self._size = v
        return self

    def topping(self, v):
        self._topping = v
        return self
    
    def crust(self, v):
        self._crust = v
        return self
    
    def build(self):
        return Pizza(self._size , self._topping, self._crust)
    
pepperoni = (PizzaBuilder()
            .size("large")
            .topping("onion")
            .crust("thick")
            .build())

print(pepperoni)