"""
To add new operations to existing object structures without modifying their classes.

👉 You keep object structures stable, and add new behaviors through “visitors.”
"""

from abc import ABC, abstractmethod

# --- Visitor Interface ---
class Visitor(ABC):
    @abstractmethod
    def visit_pizza(self, pizza):
        pass

    @abstractmethod
    def visit_drink(self, drink):
        pass


# --- Element Interface ---
class MenuItem(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


# --- Concrete Elements ---
class Pizza(MenuItem):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def accept(self, visitor: Visitor):
        visitor.visit_pizza(self)


class Drink(MenuItem):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def accept(self, visitor: Visitor):
        visitor.visit_drink(self)


# --- Concrete Visitor 1 (Print) ---
class PrintVisitor(Visitor):
    def visit_pizza(self, pizza):
        print(f"🍕 Pizza: {pizza.name} ({pizza.calories} kcal)")

    def visit_drink(self, drink):
        print(f"🥤 Drink: {drink.name} ({drink.calories} kcal)")


# --- Concrete Visitor 2 (Calorie Sum) ---
class CalorieCountVisitor(Visitor):
    def __init__(self):
        self.total = 0

    def visit_pizza(self, pizza):
        self.total += pizza.calories

    def visit_drink(self, drink):
        self.total += drink.calories


# --- Client Code ---
items = [
    Pizza("Margherita", 250),
    Pizza("Pepperoni", 300),
    Drink("Coke", 150)
]

# Print menu
print_visitor = PrintVisitor()
for item in items:
    item.accept(print_visitor)

# Count calories
calorie_visitor = CalorieCountVisitor()
for item in items:
    item.accept(calorie_visitor)

print(f"\n🔥 Total Calories: {calorie_visitor.total}")