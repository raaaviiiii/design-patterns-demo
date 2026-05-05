class CPU:
    def start(self): print("CPU started")

class Memory:
    def load(self): print("Memory loaded")

class HardDrive:
    def read(self): print("Reading data")

class ComputerFacade:
    def start(self):
        CPU().start()
        Memory().load()
        HardDrive().read()

if __name__ == "__main__":
    ComputerFacade().start()