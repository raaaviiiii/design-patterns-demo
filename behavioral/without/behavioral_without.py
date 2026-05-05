class Payment:
    def pay(self, method):
        if method == "upi":
            print("UPI payment")
        elif method == "card":
            print("Card payment")


if __name__ == "__main__":
    p = Payment()
    p.pay("upi")