
# --- Implementor Interface ---
class Oven:
    def bake(self, pizza_type):
        pass

# --- Concrete Implementors ---
class ElectricOven(Oven):
    def bake(self, pizza_type):
        print(f"electric oven {pizza_type}")

class WoodenOven(Oven):
    def bake(self, pizza_type):
        print(f"wooden oven {pizza_type}")


# --- Abstraction ---
class Pizza:
    def __init__(self, oven : Oven):
        self.oven =oven

    def prepare(self):
        pass

# --- Refined Abstractions ---
class MargheritaPizza(Pizza):
    def prepare(self):
        self.oven.bake("Margherita")


class PepperoniPizza(Pizza):
    def prepare(self):
        self.oven.bake("Pepperoni")


# --- Client Code ---
electric_oven = ElectricOven()
wood_oven = WoodenOven()

print("🍕 Using Electric Oven:")
pizza1 = MargheritaPizza(electric_oven)
pizza1.prepare()

print("\n🍕 Using Wood-Fired Oven:")
pizza2 = PepperoniPizza(wood_oven)
pizza2.prepare()