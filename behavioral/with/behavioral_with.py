class PaymentStrategy:
    def pay(self):
        pass


class UPI(PaymentStrategy):
    def pay(self):
        print("UPI payment")


class Card(PaymentStrategy):
    def pay(self):
        print("Card payment")


class Payment:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self):
        self.strategy.pay()


if __name__ == "__main__":
    p = Payment(UPI())
    p.pay()