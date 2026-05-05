# 🔹 Subsystems (Complex internal services)

class InventoryService:
    def check_stock(self, item):
        print(f"[Inventory] Checking stock for {item}")
        return True


class PaymentService:
    def process_payment(self, user, amount):
        print(f"[Payment] Charging ₹{amount} to {user}")
        return True


class ShippingService:
    def create_shipment(self, item):
        print(f"[Shipping] Shipment created for {item}")


class NotificationService:
    def send_confirmation(self, user):
        print(f"[Notification] Order confirmation sent to {user}")


# 🔹 Facade (simplified interface)

class OrderFacade:
    def __init__(self):
        self.inventory = InventoryService()
        self.payment = PaymentService()
        self.shipping = ShippingService()
        self.notification = NotificationService()

    def place_order(self, user, item, amount):
        print("\n[Facade] Starting order process...\n")

        if not self.inventory.check_stock(item):
            print("[Facade] Item out of stock")
            return

        if not self.payment.process_payment(user, amount):
            print("[Facade] Payment failed")
            return

        self.shipping.create_shipment(item)
        self.notification.send_confirmation(user)

        print("\n[Facade] Order completed successfully\n")


# 🔹 Client Code

if __name__ == "__main__":
    facade = OrderFacade()
    facade.place_order("Ravi", "Laptop", 50000)