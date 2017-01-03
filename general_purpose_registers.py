class SixteenByteWideRegisters:
    def __init__(self):
        self.registers = []
        self.size = 16
        for register in range(0, self.size):
            self.ram.append(0)

    def get_value(self, register_name):
        return self.register[register_name]

    def set_value(self, register, value):
        self.register[register] = value


