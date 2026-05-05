class Coffee:
    def get_cost(self):
        return 100

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 20

if __name__ == "__main__":
    c = MilkDecorator(Coffee())
    print(c.get_cost())