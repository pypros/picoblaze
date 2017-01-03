class ScratchpadRam:
    def __init__(self):
        self.ram = []
        self.size = 64
        for record in range(0, self.size):
            self.ram.append(0)

    def get_value(self, address):
        return self.ram[address]

    def set_value(self, address, value):
        self.ram[address] = value

