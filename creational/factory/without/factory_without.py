class Payment:
    def pay(self, payment_type):
        if payment_type == "credit":
            print("Paid using Credit Card")
        elif payment_type == "debit":
            print("Paid using Debit Card")
        elif payment_type == "upi":
            print("Paid using UPI")


if __name__ == "__main__":
    p = Payment()
    p.pay("credit")