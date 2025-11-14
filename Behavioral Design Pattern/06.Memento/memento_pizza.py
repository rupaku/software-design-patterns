"""
    To capture and restore an object’s internal state without violating its encapsulation,
    so you can undo or rollback changes when needed.

"""

#Memento
class PizzaMemento:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = list(toppings)

#Originator
class PizzaOrder:
    def __init__(self):
        self.size = "medium"
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        print(f"Added topping: {topping}")
    
    def set_size(self, size):
        self.size = size
        print(f"Size is set {self.size}")

    def save(self):
        print(f"Order saved")
        return PizzaMemento(self.size, self.toppings)
       
    def restore(self, memento):
        self.size = memento.size
        self.toppings = memento.toppings
        print("↩️ Pizza order restored to a previous state.")

    def show(self):
        print(f"Pizza(size='{self.size}', toppings={self.toppings})")

# Caretaker
class OrderHistory:
    def __init__(self):
        self._history = []

    def save(self, memento):
        self._history.append(memento)

    def undo(self):
        if not self._history:
            print("No previous states to restore.")
            return None
        return self._history.pop()
    
order = PizzaOrder()
history = OrderHistory()

order.set_size("large")
order.add_topping("cheese")
order.add_topping("mushrooms")

# save curent state
history.save(order.save())

# Make more changes
order.add_topping("pepperoni")
order.show()

# Undo changes
memento = history.undo()
if memento:
    order.restore(memento)
order.show()