"""
    To define a one-to-many dependency between objects so that when one object (the subject) changes state,
    all its dependents (observers) are notified automatically and updated.
"""

from abc import ABC , abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# --- Concrete Observers ---
class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"👩‍💼 {self.name} received notification: {message}")


class DeliveryPartner(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"🚚 {self.name} (Delivery): {message}")

# subject
class PizzaOrderSystem:
    def __init__(self):
        self._observers = []
        self._order_status = None

    def attach(self , observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._order_status)

    def update_status(self, status):
        self._order_status = status
        print(f"\n📢 Order Status Updated: {status}")
        self.notify()

# client
order_system = PizzaOrderSystem()

customer = Customer("Alice")
delivery = DeliveryPartner("Charlie")

order_system.attach(customer)
order_system.attach(delivery)

order_system.update_status("Your pizza is being prepared 🍳")
order_system.update_status("Your pizza is out for delivery 🚗")
order_system.update_status("Your pizza has been delivered! 🍕")
