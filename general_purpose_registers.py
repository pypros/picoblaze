class SixteenByteWideRegisters:
    def __init__(self):
        self.register = {
                "s0": 0,
                "s1": 0,
                "s2": 0,
                "s3": 0,
                "s4": 0,
                "s5": 0,
                "s6": 0,
                "s7": 0,
                "s8": 1,
                "s9": 0,
                "sA": 0,
                "sB": 0,
                "sC": 0,
                "sD": 0,
                "sE": 0,
                "sF": 0
            }

    def get_value(self, register_name):
        return self.register[register_name]

    def set_value(self, register_name, value):
        self.register[register_name] = value

    def rename_register(self, old_register_name, new_register_name):
        value = self.register[old_register_name]
        del self.register[old_register_name]
        self.register[new_register_name] = value
