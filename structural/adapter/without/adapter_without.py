class OldCharger:
    def charge_with_round_pin(self):
        print("Charging with round pin")


class Phone:
    def charge_with_type_c(self):
        print("Charging with Type-C")


if __name__ == "__main__":
    old = OldCharger()
    phone = Phone()

    # These two are incompatible (no adapter used)
    old.charge_with_round_pin()
    phone.charge_with_type_c()