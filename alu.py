def ADD(sx, operand):
    sx = (sx + operand) % 256

    if (sx + operand) > 255:
        carry = 1
    else:
        carry = 0

    if (sx + operand) == 0 or (sx + operand) == 256:
        zero = 1
    else:
        zero = 0

    return sx, zero, carry


def ADDCY(sx, operand, carry):
    sx = (sx + operand) % 256

    if carry:
        sx = (sx + operand + 1) % 256
    else:
        sx = (sx + operand) % 256

    if (sx + operand + carry) > 255:
        carry = 1
    else:
        carry = 0

    if (sx + operand + carry) == 0 or (sx + operand + carry) == 256:
        zero = 1
    else:
        zero = 0

    return sx, zero, carry


def AND(sx, operand):
    carry = 0

    if sx == 0:
        zero = 1
    else:
        zero = 0

    return sx & operand, zero, carry


def COMPARE(sx, operand):
    if operand > sx:
        carry = 1
    else:
        carry = 0

    if sx == operand:
        zero = 1
    else:
        zero = 0

    return zero, carry


def OR(sx, operand):
    carry = 0

    if sx == 0:
        zero = 1
    else:
        zero = 0

    return sx | operand, zero, carry


def RL(sx):
    str_sx = format(sx, 'b').zfill(8)
    rl_sx = str_sx[1:] + str_sx[0]

    carry = int(str_sx[0])
    if sx == 0:
        zero = 1
    else:
        zero = 0

    return int(rl_sx, 2), zero, carry


def RR(sx):
    str_sx = format(sx, 'b').zfill(8)
    rr_sx = str_sx[7] + str_sx[0:7]

    carry = int(str_sx[7])
    if sx == 0:
        zero = 1
    else:
        zero = 0

    return int(rr_sx, 2), zero, carry


def SL0(sx):
    return sx << 1


def SL1(sx):
    str_sx = format(sx, 'b').zfill(8)
    sl1_sx = str_sx[1:] + '1'
    return int(sl1_sx, 2)


def SLX(sx):
    str_sx = format(sx, 'b').zfill(8)
    slx_sx = str_sx[1:] + str_sx[7]
    return int(slx_sx, 2)


def SLA(sx, carry):
    str_sx = format(sx, 'b').zfill(8)
    sla_sx = str_sx[1:] + str(carry)
    return int(sla_sx, 2)


def SR0(sx):
    return sx >> 1


def SR1(sx):
    str_sx = format(sx, 'b').zfill(8)
    sr1_sx = '1' + str_sx[0:7]
    return int(sr1_sx, 2)


def SRX(sx):
    str_sx = format(sx, 'b').zfill(8)
    srx_sx = str_sx[0] + str_sx[0:7]
    return int(srx_sx, 2)


def SRA(sx, carry):
    str_sx = format(sx, 'b').zfill(8)
    sra_sx = str(carry) + str_sx[0:7]
    return int(sra_sx, 2)


def SUB(sx, operand):
    sx = (sx - operand) % 256
    return sx


def SUBCY(sx, operand, carry):
    sx = (sx + operand) % 256
    if carry:
        sx = (sx - operand - 1) % 256
    else:
        sx = (sx - operand) % 256
    return sx


def XOR(sx, operand):
    return sx ^ operand
