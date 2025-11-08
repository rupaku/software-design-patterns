"""
To minimize memory usage by sharing common (intrinsic) data between multiple similar objects instead of creating new ones every time.
"""

# --- Flyweight (Shared Object) ---
class PizzaType:
    def __init__(self, name, dough, sauce, toppings):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def display(self, table_number):
        # 'table_number' is extrinsic (unique per order)
        print(f"Serving {self.name} pizza to table {table_number}")

class PizzaFactory:
    _pizza_types = {}
    def get_pizza_type(self , name , dough , sauce , toppings):
        key = (name , dough , sauce , tuple(toppings))
        if key not in self._pizza_types:
            print(f"Creating new pizza type: {name}")
            self._pizza_types[key] = PizzaType(name, dough, sauce, toppings)
        return self._pizza_types[key]
    
# --- Context / Client ---
class PizzaOrder:
    def __init__(self, table_number, pizza_type):
        self.table_number = table_number
        self.pizza_type = pizza_type

    def serve(self):
        self.pizza_type.display(self.table_number)


# --- Usage ---
factory = PizzaFactory()

# Create shared pizza types
margherita_type = factory.get_pizza_type("Margherita", "thin", "tomato", ["cheese", "basil"])
pepperoni_type = factory.get_pizza_type("Pepperoni", "hand-tossed", "tomato", ["cheese", "pepperoni"])

# Place multiple orders using shared pizza types
orders = [
    PizzaOrder(1, margherita_type),
    PizzaOrder(2, margherita_type),
    PizzaOrder(3, pepperoni_type),
]

# Serve pizzas
for order in orders:
    order.serve()