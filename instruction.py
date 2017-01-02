def add(sx, operand):
    sx = (sx + operand) % 256
    return sx


def addcy(sx, operand, carry_in):
    sx = (sx + operand) % 256
    if carry_in:
        sx = (sx + operand + 1) % 256
    else:
        sx = (sx + operand) % 256
    return sx
