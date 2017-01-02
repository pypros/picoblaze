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
    return int(rl_sx, 2)


def RR(sx):
    str_sx = format(sx, 'b').zfill(8)
    rr_sx = str_sx[7] + str_sx[0:7]
    return int(rr_sx, 2)


def SL0(sx):
    return sx << 1


def SL1(sx):
    str_sx = format(sx, 'b').zfill(8)
    sl1_sx = str_sx[1:] + '1'
    return int(sl1_sx, 2)


def SLX(sx):
    str_sx = format(sx, 'b').zfill(8)
    sl1_sx = str_sx[1:] + str_sx[7]
    return int(sl1_sx, 2)


def SLA(sx, carry_in):
    str_sx = format(sx, 'b').zfill(8)
    sl1_sx = str_sx[1:] + str(carry_in)
    return int(sl1_sx, 2)


def SR0(sx):
    return sx >> 1


def SR1(sx):
    str_sx = format(sx, 'b').zfill(8)
    sl1_sx = '1' + str_sx[0:7]
    return int(sl1_sx, 2)

def SRX(sx):
    str_sx = format(sx, 'b').zfill(8)
    srx_sx = str_sx[0] + str_sx[0:7]
    return int(srx_sx, 2)


def SRA(sx, carry_in):
    str_sx = format(sx, 'b').zfill(8)
    sra_sx = str(carry_in) + str_sx[0:7]
    return int(sra_sx, 2)