"""
    To provide a simplified interface to a complex system of classes, libraries, or subsystems
"""

# --- Subsystems ---
class DoughMaker:
    def prepare_dough(self):
        print("🥣 Preparing pizza dough...")

class SauceMaker:
    def add_sauce(self):
        print("🍅 Adding tomato sauce...")

class ToppingAdder:
    def add_toppings(self):
        print("🧀 Adding cheese and toppings...")

class Oven:
    def bake_pizza(self):
        print("🔥 Baking pizza in the oven...")

class PaymentSystem:
    def make_payment(self, amount):
        print(f"💳 Processing payment of ₹{amount}...")


# --- Facade ---
class PizzaShopFacade:
    def __init__(self):
        self.dough_maker = DoughMaker()
        self.sauce_maker = SauceMaker()
        self.topping_adder = ToppingAdder()
        self.oven = Oven()
        self.payment_system = PaymentSystem()

    def order_pizza(self, pizza_type, amount):
        print(f"\n🍕 Order received for {pizza_type} pizza")
        self.dough_maker.prepare_dough()
        self.sauce_maker.add_sauce()
        self.topping_adder.add_toppings()
        self.oven.bake_pizza()
        self.payment_system.make_payment(amount)
        print("✅ Pizza ready! Enjoy your meal 🍽️")


# --- Client Code ---
if __name__ == "__main__":
    pizza_shop = PizzaShopFacade()
    pizza_shop.order_pizza("Margherita", 300)
