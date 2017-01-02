def ADD(sx, operand):
    sx = (sx + operand) % 256
    return sx


def ADDCY(sx, operand, carry_in):
    sx = (sx + operand) % 256
    if carry_in:
        sx = (sx + operand + 1) % 256
    else:
        sx = (sx + operand) % 256
    return sx


def AND(sx, operand):
    return sx & operand


def OR(sx, operand):
    return sx | operand