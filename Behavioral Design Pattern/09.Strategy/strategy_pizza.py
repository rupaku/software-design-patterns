"""
     In simple terms: Replace big if-else blocks for different behaviors with swappable strategy objects.
"""

from abc import ABC, abstractmethod

# --- Strategy Interface ---
class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, base_price):
        pass


# --- Concrete Strategies ---
class NormalPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price

class DiscountPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price * 0.9   # 10% discount

class FestivalPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price * 0.8   # 20% festival discount


# --- Context ---
class PizzaOrder:
    def __init__(self, price, strategy: PricingStrategy):
        self.price = price
        self.strategy = strategy

    def set_strategy(self, strategy: PricingStrategy):
        self.strategy = strategy

    def final_price(self):
        return self.strategy.calculate(self.price)


# --- Client Code ---
order = PizzaOrder(300, NormalPricing())
print("Normal:", order.final_price())

order.set_strategy(DiscountPricing())
print("Discount:", order.final_price())

order.set_strategy(FestivalPricing())
print("Festival:", order.final_price())