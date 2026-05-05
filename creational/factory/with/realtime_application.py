from abc import ABC, abstractmethod


# 🔹 Product Interface
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, user, amount):
        pass


# 🔹 Concrete Products

class Razorpay(PaymentGateway):
    def process_payment(self, user, amount):
        print(f"[Razorpay] Processing ₹{amount} for {user}")


class Stripe(PaymentGateway):
    def process_payment(self, user, amount):
        print(f"[Stripe] Processing ₹{amount} for {user}")


class PayPal(PaymentGateway):
    def process_payment(self, user, amount):
        print(f"[PayPal] Processing ₹{amount} for {user}")


# 🔹 Factory Class
class PaymentFactory:
    @staticmethod
    def get_payment_gateway(gateway_name: str) -> PaymentGateway:
        if gateway_name.lower() == "razorpay":
            return Razorpay()
        elif gateway_name.lower() == "stripe":
            return Stripe()
        elif gateway_name.lower() == "paypal":
            return PayPal()
        else:
            raise ValueError("Unsupported payment gateway")


# 🔹 Client Code
if __name__ == "__main__":
    gateway_name = "stripe"

    gateway = PaymentFactory.get_payment_gateway(gateway_name)
    gateway.process_payment("Ravi", 5000)