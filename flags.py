class Flags:
    def __init__(self):
        self.zero = 0
        self.carry = 0
        self.preserved_zero = 0
        self.preserved_carry = 0

    def get_zero(self):
        return self.zero

    def get_carry(self):
        return self.carry

    def set_zero(self, value):
        self.zero = value

    def set_carry(self, value):
        self.carry = value
