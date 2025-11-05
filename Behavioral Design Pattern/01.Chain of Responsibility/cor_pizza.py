class Handler:
    def __init__(self, next_handler):
        self.next_handler = next_handler

    def handle(self, reqest):
        if self.next_handler:
            return self.next_handler.handler(reqest)
        return None
    
class OrderHandler(Handler):
    def handle(self, reqest):
        if reqest == "order":
            print("Taking Pizza Order")
        else:
            super().handle(reqest)

class ChefHandler(Handler):
    def handle(self, reqest):
        if reqest == "cook":
            print("cooking Pizza Order")
        else:
            super().handle(reqest)

class DeliveryHandler(Handler):
    def handle(self, reqest):
        if reqest == "deliver":
            print("delivering Pizza Order")
        else:
            super().handle(reqest)

# Create the chain: OrderTaker → Chef → DeliveryPerson

chain = OrderHandler(ChefHandler(DeliveryHandler))

for request in ["order", "cook", "deliver"]:
    print(f"\nProcessing: {request}")
    chain.handle(request)
