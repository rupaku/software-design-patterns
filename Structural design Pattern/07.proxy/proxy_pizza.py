from time import sleep

class PizzaShop:
    def order_pizza(self, customer_name , pizza_type):
        raise NotImplementedError
    
class RealPizzaShop(PizzaShop):
    def order_pizza(self, customer_name , pizza_type):
        print(f"preparing {pizza_type} for {customer_name}")
        sleep(5)
        print(f"ordered {pizza_type} for {customer_name}")

class ProxyPizzaShop(PizzaShop):
    def __init__(self):
        self.real_shop = RealPizzaShop()
        self.order_history ={}

    def order_pizza(self, customer_name, pizza_type):
        print(f" Proxy preparing {pizza_type} for {customer_name}")

        #access control
        if pizza_type.lower() == "extra spicy" and customer_name.lower() == "kid":
            print("Order Not allowed for kids")
            return
        
        #caching
        key = (customer_name,pizza_type)
        if key in self.order_history:
            print("order already placed")
        else:
            self.real_shop.order_pizza(customer_name, pizza_type)
            self.order_history[key] = "ready"
        print("order completed")

if __name__ == "__main__":
    proxy = ProxyPizzaShop()
    proxy.order_pizza("rupa","margarita")
    proxy.order_pizza("kid","extra spicy")
    proxy.order_pizza("rupa","margarita")