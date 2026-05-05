class Light:
    def turn_on(self):
        print("Light ON")

class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

if __name__ == "__main__":
    cmd = LightOnCommand(Light())
    cmd.execute()