"""
    To create families of related objects without specifying their concrete classes.
"""

from abc import ABC, abstractmethod

# --- Abstract Products ---
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Drink(ABC):
    @abstractmethod
    def serve(self):
        pass


# --- Concrete Products (Italian Family) ---
class ItalianPizza(Pizza):
    def prepare(self):
        print("Preparing Italian Pizza with tomato sauce and mozzarella cheese.")

class ItalianDrink(Drink):
    def serve(self):
        print("Serving Italian red wine.")


# --- Concrete Products (Indian Family) ---
class IndianPizza(Pizza):
    def prepare(self):
        print("Preparing Indian Pizza with paneer and spicy curry sauce.")

class IndianDrink(Drink):
    def serve(self):
        print("Serving Indian masala chai.")


# --- Abstract Factory ---
class RestaurantFactory(ABC):
    @abstractmethod
    def create_pizza(self):
        pass

    @abstractmethod
    def create_drink(self):
        pass


# --- Concrete Factories ---
class ItalianRestaurantFactory(RestaurantFactory):
    def create_pizza(self):
        return ItalianPizza()

    def create_drink(self):
        return ItalianDrink()


class IndianRestaurantFactory(RestaurantFactory):
    def create_pizza(self):
        return IndianPizza()

    def create_drink(self):
        return IndianDrink()


# --- Client Code ---
def order_meal(factory: RestaurantFactory):
    pizza = factory.create_pizza()
    drink = factory.create_drink()

    pizza.prepare()
    drink.serve()


# Usage
print("🍕 Ordering from Italian Restaurant:")
order_meal(ItalianRestaurantFactory())

print("\n🍛 Ordering from Indian Restaurant:")
order_meal(IndianRestaurantFactory())
