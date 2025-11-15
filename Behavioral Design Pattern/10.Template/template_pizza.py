"""
   To define the skeleton of an algorithm in a method (the template),
letting subclasses override specific steps of the algorithm without changing its structure.

👉 In simple terms: The parent class defines what happens, and subclasses define how it happens.     
"""

from abc import ABC, abstractmethod

class PizzaMaker(ABC):
    # Template Method
    def make_pizza(self):
        self.prepare_dough()
        self.add_sauce()
        self.add_toppings()
        self.bake()
        print("🍕 Pizza is ready!\n")

    def prepare_dough(self):
        print("🥣 Preparing dough...")

    def add_sauce(self):
        print("🍅 Adding tomato sauce...")

    @abstractmethod
    def add_toppings(self):
        pass

    def bake(self):
        print("🔥 Baking the pizza at 250°C...")

class MargheritaPizza(PizzaMaker):
    def add_toppings(self):
        print("🧀 Adding mozzarella and basil...")

class PepperoniPizza(PizzaMaker):
    def add_toppings(self):
        print("🍖 Adding cheese and pepperoni...")
   
# client code

pizza1 = MargheritaPizza()
pizza1.make_pizza()

pizza2 = PepperoniPizza()
pizza2.make_pizza()