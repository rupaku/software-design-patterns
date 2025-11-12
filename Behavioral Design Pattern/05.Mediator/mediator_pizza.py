"""
    To define an object (the Mediator) that centralizes communication between multiple objects (called Colleagues),
    so they don’t communicate directly with each other.
"""

class Mediator:
    def notify(self,sender,event):
        pass

class PizzaOrderMediator(Mediator):
    def __init__(self, customer,chef,delivery):
        self.customer = customer
        self.chef = chef
        self.delivery = delivery

        #connect all participants
        self.customer.mediator =self
        self.chef.mediator = self
        self.delivery.mediator = self

    def notify(self, sender, event):
        if event == "order_pizza":
            print("Mediator: Notifying Chef to prepare pizza...")
            self.chef.prepare_pizza()
        elif event == "pizza_ready":
            print("Mediator: Notifying Delivery to deliver pizza...")
            self.delivery.deliver_pizza()
        elif event == "delivered":
            print("Mediator: Notifying Customer that pizza is delivered!")
            self.customer.receive_pizza()

# --colleagues
class Customer:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def order_pizza(self):
        print(f"👩‍💼 {self.name}: I'd like to order a pizza.")
        self.mediator.notify(self, "order_pizza")

    def receive_pizza(self):
        print(f"🍕 {self.name}: Yay! My pizza has arrived!")


class Chef:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def prepare_pizza(self):
        print(f"👨‍🍳 {self.name}: Preparing the pizza...")
        self.mediator.notify(self, "pizza_ready")


class DeliveryPerson:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def deliver_pizza(self):
        print(f"🚚 {self.name}: Delivering the pizza...")
        self.mediator.notify(self, "delivered")

#client code
customer = Customer("Alice")
chef = Chef("Bob")
delivery = DeliveryPerson("Charlie")

Mediator = PizzaOrderMediator(customer,chef,delivery)

customer.order_pizza()