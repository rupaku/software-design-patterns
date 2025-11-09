
# Existing incompatible class (Adaptee)
class ModernOven:
    def start_baking(self, item):
        print(f"Modern oven {item}")

#expected
class PizzaOven:
    def bake_pizza(self, pizza_name):
        print(f"bake pizza {self.pizza_name}")

# Adpater
class OvenAdapter(PizzaOven):
    def __init__(self, modern_oven):
        self.modern_oven = modern_oven

    def bake_pizza(self, pizza_name):
        # Translate the expected call to adaptee's method
        self.modern_oven.start_baking(pizza_name)

#client

def cook_pizza(oven: PizzaOven , pizza):
    oven.bake_pizza(pizza)

modern_oven = ModernOven()
adapter = OvenAdapter(modern_oven)

cook_pizza(adapter, "Margherita")