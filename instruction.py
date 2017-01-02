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


def RL(sx):
    str_sx = format(sx, 'b').zfill(8)
    rl_sx = str_sx[1:] + str_sx[0]
    return int(rl_sx)

def RR(sx):
    str_sx = format(sx, 'b').zfill(8)
    rr_sx = str_sx[7] + str_sx[0:6]
    return int(rr_sx)
