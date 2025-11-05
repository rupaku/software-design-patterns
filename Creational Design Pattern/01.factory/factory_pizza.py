"""
    To create objects without exposing the creation logic to the client,
    and to refer to the newly created object using a common interface.
"""
from abc import ABC , abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Concrete Products
class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita Pizza with tomato, cheese, and basil.")


class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza with cheese and pepperoni slices.")


class VeggiePizza(Pizza):
    def prepare(self):
        print("Preparing Veggie Pizza with bell peppers, onions, and olives.")

# Factory
class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == "margherita":
            return MargheritaPizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        elif pizza_type == "veggie":
            return VeggiePizza()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")

#client code
factory = PizzaFactory()

for ptype in ["margherita", "pepperoni", "veggie"]:
    pizza = factory.create_pizza(ptype)
    pizza.prepare()