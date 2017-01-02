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

   # def ADD(self, sx, operand):
   #      if (sx + operand) > 255:
   #          self.set_carry(1)
   #      else:
   #          self.set_carry(0)
   #
   #      if (sx + operand) == 0 or (sx + operand) == 256:
   #          self.set_zero(1)
   #      else:
   #          self.set_zero(0)