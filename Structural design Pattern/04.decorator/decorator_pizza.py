"""
    To add new behavior or responsibilities to objects dynamically at runtime,
    without modifying their original code or using inheritance.
"""

from abc import ABC , abstractmethod

# --- Component Interface ---
class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

# --- Concrete Component ---
class PlainPizza(Pizza):
    def get_description(self):
        return "Plain Pizza"

    def get_cost(self):
        return 200
    
# --- Decorator Abstract Class ---
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza =pizza

# --- Concrete Decorators ---
class CheeseDecorator(PizzaDecorator):
    def get_description(self):
        return self._pizza.get_description() + ", Extra Cheese"

    def get_cost(self):
        return self._pizza.get_cost() + 50
    
class OliveDecorator(PizzaDecorator):
    def get_description(self):
        return self._pizza.get_description() + ", Olives"

    def get_cost(self):
        return self._pizza.get_cost() + 40


class MushroomDecorator(PizzaDecorator):
    def get_description(self):
        return self._pizza.get_description() + ", Mushrooms"

    def get_cost(self):
        return self._pizza.get_cost() + 60
    
    # --- Client Code ---
pizza = PlainPizza()
print(f"🧾 {pizza.get_description()} = ₹{pizza.get_cost()}")

# Add toppings dynamically
pizza = CheeseDecorator(pizza)
pizza = OliveDecorator(pizza)
pizza = MushroomDecorator(pizza)

print(f"🧾 {pizza.get_description()} = ₹{pizza.get_cost()}")