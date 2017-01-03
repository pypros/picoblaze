class Flags:
    def __init__(self):
        self.zero = 0
        self.carry = 0
        self.preserved_zero = 0
        self.preserved_carry = 0

    def get_zero(self):
        return self.z

    def get_carry(self):
        return self.c

    def set_zero(self, value):
        self.z = value

    def set_carry(self, value):
        self.c = value
