from abc import ABC, abstractmethod


# 🔹 Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, user, amount):
        pass


# 🔹 Concrete Strategies

class UPIPayment(PaymentStrategy):
    def pay(self, user, amount):
        print(f"[UPI] {user} paid ₹{amount} using UPI")


class CardPayment(PaymentStrategy):
    def pay(self, user, amount):
        print(f"[Card] {user} paid ₹{amount} using Card")


class WalletPayment(PaymentStrategy):
    def pay(self, user, amount):
        print(f"[Wallet] {user} paid ₹{amount} using Wallet")


# 🔹 Context (Main Payment Processor)

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        print(f"[Processor] Switching strategy to {strategy.__class__.__name__}")
        self.strategy = strategy

    def process_payment(self, user, amount):
        print("[Processor] Processing payment...")
        self.strategy.pay(user, amount)


# 🔹 Client Code

if __name__ == "__main__":
    # Default strategy
    processor = PaymentProcessor(UPIPayment())

    # Payment using UPI
    processor.process_payment("Ravi", 1000)

    # Switch to Card
    processor.set_strategy(CardPayment())
    processor.process_payment("Ravi", 2000)

    # Switch to Wallet
    processor.set_strategy(WalletPayment())
    processor.process_payment("Ravi", 500)