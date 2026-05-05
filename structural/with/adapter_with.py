class TypeCCharger:
    def charge(self):
        pass


class OldCharger:
    def charge_with_round_pin(self):
        print("Charging with round pin")


class ChargerAdapter(TypeCCharger):
    def __init__(self, charger: OldCharger):
        self.charger = charger

    def charge(self):
        self.charger.charge_with_round_pin()


if __name__ == "__main__":
    old = OldCharger()
    adapter = ChargerAdapter(old)
    adapter.charge()