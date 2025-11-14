"""
    To allow an object to change its behavior dynamically when its internal state changes —
    as if it changes its class at runtime.

    👉 It helps avoid long if-else or switch statements based on state conditions.    
"""

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class OrderedState(State):
    def handle(self, context):
        print("🧾 Order placed. Pizza will start baking soon.")
        context.set_state(BakingState())
class BakingState(State):
    def handle(self, context):
        print("🔥 Pizza is baking in the oven.")
        context.set_state(ReadyState())

class ReadyState(State):
    def handle(self, context):
        print("🍕 Pizza is ready for delivery!")
        context.set_state(DeliveredState())

class DeliveredState(State):
    def handle(self, context):
        print("🚚 Pizza has been delivered! Enjoy your meal 🍽️")

#Context

class PizzaOrder:
    def __init__(self):
        self.state = OrderedState()

    def set_state(self, state):
        self.state = state

    def next_state(self):
        self.state.handle(self)

order = PizzaOrder()
order.next_state()  # Ordered → Baking
order.next_state()  # Baking → Ready
order.next_state()  # Ready → Delivered
order.next_state()  # Delivered (end)
