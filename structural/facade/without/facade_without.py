class CPU:
    def start(self): print("CPU started")

class Memory:
    def load(self): print("Memory loaded")

class HardDrive:
    def read(self): print("Reading data")

if __name__ == "__main__":
    cpu = CPU()
    mem = Memory()
    hd = HardDrive()

    cpu.start()
    mem.load()
    hd.read()