class Coffee:
    def get_cost(self):
        return 100

if __name__ == "__main__":
    c = Coffee()
    print(c.get_cost() + 20)  # milk added manually