class Payment:
    def pay(self):
        pass


class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")


class DebitCard(Payment):
    def pay(self):
        print("Paid using Debit Card")


class UPI(Payment):
    def pay(self):
        print("Paid using UPI")


class PaymentFactory:
    @staticmethod
    def get_payment(payment_type):
        if payment_type == "credit":
            return CreditCard()
        elif payment_type == "debit":
            return DebitCard()
        else:
            return UPI()


if __name__ == "__main__":
    p = PaymentFactory.get_payment("credit")
    p.pay()