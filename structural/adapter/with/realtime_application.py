from abc import ABC, abstractmethod


# 🔹 Target Interface (what your system expects)
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, user, amount):
        pass


# 🔹 Existing System (your app expects this format)
class StripeProcessor(PaymentProcessor):
    def pay(self, user, amount):
        print(f"[Stripe] {user} paid ₹{amount}")


# 🔹 Third-party / Legacy API (incompatible interface)
class LegacyPay:
    def make_payment(self, username, value):
        print(f"[LegacyPay] Payment of ₹{value} done for {username}")


# 🔹 Adapter (makes LegacyPay compatible with your system)
class LegacyPayAdapter(PaymentProcessor):
    def __init__(self, legacy_service: LegacyPay):
        self.legacy_service = legacy_service

    def pay(self, user, amount):
        # Convert interface
        self.legacy_service.make_payment(user, amount)


# 🔹 Client Code (your application)
if __name__ == "__main__":
    # Using modern processor
    processor1 = StripeProcessor()
    processor1.pay("Ravi", 1000)

    # Using legacy system via adapter
    legacy = LegacyPay()
    processor2 = LegacyPayAdapter(legacy)
    processor2.pay("Ravi", 2000)