class House:
    def __init__(self):
        self.walls = None
        self.roof = None

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Concrete"
        return self

    def build_roof(self):
        self.house.roof = "Tiles"
        return self

    def get_house(self):
        return self.house

if __name__ == "__main__":
    h = HouseBuilder().build_walls().build_roof().get_house()
    print(h.walls, h.roof)