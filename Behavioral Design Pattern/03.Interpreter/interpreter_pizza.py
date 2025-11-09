"""
It helps evaluate expressions or parse structured data by representing rules and grammar as classes

Let’s say we want to evaluate pizza orders using expressions like:
Margherita + Cheese or Pepperoni + Cheese + Olives
"""

from abc import ABC, abstractmethod

# --- Context ---
class Context:
    prices = {
        "Margherita": 250,
        "Pepperoni": 300,
        "Cheese": 50,
        "Olives": 40,
        "Mushrooms": 60
    }


# --- Abstract Expression ---
class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context):
        pass


# --- Terminal Expression ---
class PizzaExpression(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context: Context):
        price = context.prices.get(self.name, 0)
        print(f"{self.name}: ₹{price}")
        return price


# --- Non-Terminal Expression ---
class AddExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: Context):
        left_price = self.left.interpret(context)
        right_price = self.right.interpret(context)
        return left_price + right_price


# --- Client Code ---
context = Context()

# Expression: Margherita + Cheese + Olives
expr = AddExpression(
    AddExpression(PizzaExpression("Margherita"), PizzaExpression("Cheese")),
    PizzaExpression("Olives")
)

total = expr.interpret(context)
print(f"💰 Total Price: ₹{total}")