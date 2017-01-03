class ProgramCounter:
    def __init__(self):
        self.pc = 0

    def increment_value(self):
        self.pc += 1

    def get_value(self):
        return self.pc

    def set_value(self, value):
        self.pc = value