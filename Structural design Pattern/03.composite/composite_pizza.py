# --- Component Interface ---
class MenuComponent:
    def show_details(self):
        pass

# Leaf Class
class MenuItem(MenuComponent):
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def show_details(self):
        print(f"🍕 {self.name}: ₹{self.price}")

# --- Composite Class ---
class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self , component : MenuComponent):
        self.items.append(component)

    def remove_item(self , component : MenuComponent):
        self.items.remove(component)

    def show_details(self):
        print(f"\n📖 {self.name}")
        print("-" * (len(self.name) + 4))
        for item in self.items:
            item.show_details()

# --- Client Code ---
pizza_menu = Menu("Pizza Menu")
pizza_menu.add_item(MenuItem("Margherita", 250))
pizza_menu.add_item(MenuItem("Pepperoni", 300))

drinks_menu = Menu("Drinks Menu")
drinks_menu.add_item(MenuItem("Coke", 80))
drinks_menu.add_item(MenuItem("Lemonade", 70))

main_menu = Menu("Main Menu")
main_menu.add_item(pizza_menu)
main_menu.add_item(drinks_menu)

# Display the full menu
main_menu.show_details()