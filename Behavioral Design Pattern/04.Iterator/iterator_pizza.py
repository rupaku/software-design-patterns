"""
     It lets you iterate over elements of an object without knowing how they are stored internally.
"""

class Iterator:
    def __next__(self):
        pass

    def __iter__(self):
        return self
    
class MenuIterarator(Iterator):
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        raise StopIteration
    
class PizzaMenu:
    def __init__(self):
        self._pizzas = []

    def add_pizza(self, pizza):
        self._pizzas.append(pizza)

    def __iter__(self):
        return MenuIterarator(self._pizzas)
    
# client code
menu = PizzaMenu()
menu.add_pizza("Pepperoni")
menu.add_pizza("Veggie Supreme")

print("🍕 Today's Menu:")
for pizza in menu:
    print(f"→ {pizza}")