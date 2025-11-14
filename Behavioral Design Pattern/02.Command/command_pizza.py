"""
Turn a request (action) into an object so it can be stored, executed, or undone later.

Imagine a pizza restaurant app where a waiter (invoker) sends orders (commands) to the chef (receiver).
"""

from abc import ABC , abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

#Receiver
class Chef:
    def make_pizza(self):
        print("👨‍🍳 Chef: Making a delicious pizza!")

    def make_pasta(self):
        print("👨‍🍳 Chef: Cooking fresh pasta!")

# --- Concrete Commands ---
class MakePizzaCommand(Command):
    def __init__(self, chef):
        self.chef=chef

    def execute(self):
        self.chef.make_pizza()

class MakePastaCommand(Command):
    def __init__(self, chef):
        self.chef=chef

    def execute(self):
        self.chef.make_pasta()

# --- Invoker ---
class Waiter:
    def __init__(self):
        self._commands =[]

    def take_order(self,command):
        self._commands.append(command)

    def place_orders(self):
        print("\n🧾 Waiter: Placing all orders...")
        for command in self._commands:
            command.execute()
        self._commands.clear()  

#client

chef = Chef()
waiter = Waiter()

# create and queue command
waiter.take_order(MakePizzaCommand(chef))
waiter.take_order(MakePastaCommand(chef))

# Execute all commands
waiter.place_orders()