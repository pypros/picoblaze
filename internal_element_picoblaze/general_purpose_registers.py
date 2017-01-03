class SixteenByteWideRegisters:
    def __init__(self):
        self.size = 16
        self.registers = [0] * self.size

    def get_value(self, register_name):
        return self.registers[register_name]

    def set_value(self, register, value):
        self.registers[register] = value


