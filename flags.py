class Flags:
    z = 0
    c = 0

    def __init__(self,**kwargs):
        self.z = kwargs['zero']
        self.c = kwargs['carry']

    def get_zero(self):
        return self.z

    def get_carry(self):
        return self.c

    def set_zero(self, *args):
        self.z = args[0]

    def set_carry(self, *args):
        self.c = args[0]
