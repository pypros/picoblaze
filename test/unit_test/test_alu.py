from picoblaze import PicoBlaze


def test_ADD_sx_kk():
    cpu = PicoBlaze()
    #         "011000xxxxkkkkkkkk"
    program = "011000000001111111"  # ADD s0, kk
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = value_register_sx + int(program[10:], 2)
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_ADD_sx_sy():
    cpu = PicoBlaze()
    #         "011001xxxxyyyy0000"
    program = "011001000011110000"  # ADD sx, sy
    value_register_sx = 2
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_register_sx = value_register_sx + value_register_sy
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]

def test_ADD_sx_kk_flag_zero():
    cpu = PicoBlaze()
    #         "011000xxxxkkkkkkkk"
    program = "011000000000000000"  # ADD s0, kk
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_ADD_sx_sy_flag_carry():
    cpu = PicoBlaze()
    #         "011001xxxxyyyy0000"
    program = "011001000011110000"  # ADD sx, sy
    value_register_sx = 255
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_ADDCY_sx_kk():
    cpu = PicoBlaze()
    #         "011010xxxxkkkkkkkk"
    program = "011010000001111111"  # ADDCY s0, kk
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = value_register_sx + int(program[10:], 2) + cpu._PicoBlaze__flag_carry
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_ADDCY_sx_sy():
    cpu = PicoBlaze()
    #         "011011xxxxyyyy0000"
    program = "011011000011110000"  # ADDCY sx, sy
    value_register_sx = 2
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_register_sx = value_register_sx + value_register_sy + cpu._PicoBlaze__flag_carry
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_ADDCY_sx_kk_flag_zero():
    cpu = PicoBlaze()
    #         "011010xxxxkkkkkkkk"
    program = "011010000000000000"  # ADDCY s0, kk
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_ADDCY_sx_sy_flag_carry():
    cpu = PicoBlaze()
    #         "011011xxxxyyyy0000"
    program = "011011000011110000"  # ADDCY sx, sy
    value_register_sx = 255
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_AND_sx_kk():
    cpu = PicoBlaze()
    #         "001010xxxxkkkkkkkk"
    program = "001010000001111111"  # AND s0, kk
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = value_register_sx & int(program[10:], 2)
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_AND_sx_sy():
    cpu = PicoBlaze()
    #         "001011xxxxyyyy0000"
    program = "001011000011110000"  # AND sx, sy
    value_register_sx = 3
    number_register_sx = 0
    value_register_sy = 2
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_register_sx = value_register_sx & value_register_sy
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_AND_sx_kk_flag_zero():
    cpu = PicoBlaze()
    #         "001010xxxxkkkkkkkk"
    program = "001010000000000000"  # AND s0, kk
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_AND_sx_sy_flag_carry():
    cpu = PicoBlaze()
    #         "001011xxxxyyyy0000"
    program = "001011000011110000"  # AND sx, sy
    value_register_sx = 255
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 0
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_COMPARE_sx_kk():
    cpu = PicoBlaze()
    #         "010100xxxxkkkkkkkk"
    program = "010100000001111111"  # COMPARE s0, kk
    value_register_sx = 127
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_COMPARE_sx_sy():
    cpu = PicoBlaze()
    #         "010101xxxxyyyy0000"
    program = "010101000011110000"  # COMPARE sx, sy
    value_register_sx = 2
    number_register_sx = 0
    value_register_sy = 3
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_OR_sx_kk():
    cpu = PicoBlaze()
    #         "001100xxxxkkkkkkkk"
    program = "001100000001111111"  # OR s0, kk
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = value_register_sx | int(program[10:], 2)
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_OR_sx_sy():
    cpu = PicoBlaze()
    #         "001101xxxxyyyy0000"
    program = "001101000011110000"  # OR sx, sy
    value_register_sx = 3
    number_register_sx = 0
    value_register_sy = 2
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_register_sx = value_register_sx | value_register_sy
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_OR_sx_kk_flag_zero():
    cpu = PicoBlaze()
    #         "001100xxxxkkkkkkkk"
    program = "001100000000000000"  # OR s0, kk
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_OR_sx_sy_flag_carry():
    cpu = PicoBlaze()
    #         "001101xxxxyyyy0000"
    program = "001101000011110000"  # OR sx, sy
    value_register_sx = 255
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 0
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SL0():
    cpu = PicoBlaze()
    #         "100000xxxx00000110"
    program = "100000000000000110"  # SL0 sx
    value_register_sx = 64
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = 128
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SL0_flag_zero():
    cpu = PicoBlaze()
    #         "100000xxxx00000110"
    program = "100000000000000110"  # SL0 sx
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SL0_flag_carry():
    cpu = PicoBlaze()
    #         "100000xxxx00000110"
    program = "100000000000000110"  # SL0 sx
    value_register_sx = 192
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SL1():
    cpu = PicoBlaze()
    #         "100000xxxx00000111"
    program = "100000000000000111"  # SL1 sx
    value_register_sx = 192
    number_register_sx = 0
    cpu._PicoBlaze__flag_carry = 1
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = 129
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SL1_flag_zero():
    cpu = PicoBlaze()
    #         "100000xxxx00000111"
    program = "100000000000000111"  # SL1 sx
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SL1_flag_carry():
    cpu = PicoBlaze()
    #         "100000xxxx00000111"
    program = "100000000000000111"  # SL1 sx
    value_register_sx = 192
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SLA():
    cpu = PicoBlaze()
    #         "100000xxxx00000000"
    program = "100000000000000000"  # SLA sx
    value_register_sx = 192
    number_register_sx = 0
    cpu._PicoBlaze__flag_carry = 1
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = 129
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SLA_flag_zero():
    cpu = PicoBlaze()
    #         "100000xxxx00000000"
    program = "100000000000000000"  # SLA sx
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SLA_flag_carry():
    cpu = PicoBlaze()
    #         "100000xxxx00000000"
    program = "100000000000000000"  # SLA sx
    value_register_sx = 192
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SLX():
    cpu = PicoBlaze()
    #         "100000xxxx00000100"
    program = "100000000000000100"  # SLX sx
    value_register_sx = 192
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = 128
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]

def test_SLX_flag_zero():
    cpu = PicoBlaze()
    #         "100000xxxx00000100"
    program = "100000000000000100"  # SLX sx
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SLX_flag_carry():
    cpu = PicoBlaze()
    #         "100000xxxx00000100"
    program = "100000000000000100"  # SLX sx
    value_register_sx = 192
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SR0():
    cpu = PicoBlaze()
    #         "100000xxxx00001110"
    program = "100000000000001110"  # SR0 sx
    value_register_sx = 2
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = 1
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SR0_flag_zero():
    cpu = PicoBlaze()
    #         "100000xxxx00001110"
    program = "100000000000001110"  # SR0 sx
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SR0_flag_carry():
    cpu = PicoBlaze()
    #         "100000xxxx00001110"
    program = "100000000000001110"  # SR0 sx
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SR1():
    cpu = PicoBlaze()
    #         "100000xxxx00001111"
    program = "100000000000001111"  # SR1 sx
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = 128
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SR1_flag_zero():
    cpu = PicoBlaze()
    #         "100000xxxx00001111"
    program = "100000000000001111"  # SR1 sx
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SR1_flag_carry():
    cpu = PicoBlaze()
    #         "100000xxxx00001111"
    program = "100000000000001111"  # SR1 sx
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SRA():
    cpu = PicoBlaze()
    #         "100000xxxx00001000"
    program = "100000000000001000"  # SRA sx
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__flag_carry = 1
    cpu.run(program)
    expected_register_sx = 128
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SRA_flag_zero():
    cpu = PicoBlaze()
    #         "100000xxxx00001000"
    program = "100000000000001000"  # SRA sx
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SRA_flag_carry():
    cpu = PicoBlaze()
    #         "100000xxxx00001000"
    program = "100000000000001000"  # SRA sx
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__flag_carry = 1
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SRX():
    cpu = PicoBlaze()
    #         "100000xxxx00001010"
    program = "100000000000001010"  # SRX sx
    value_register_sx = 3
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = 3 >> 1
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]

def test_SRX_flag_zero():
    cpu = PicoBlaze()
    #         "100000xxxx00001010"
    program = "100000000000001010"  # SRX sx
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SRX_flag_carry():
    cpu = PicoBlaze()
    #         "100000xxxx00001010"
    program = "100000000000001010"  # SRX sx
    value_register_sx = 3
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry



def test_SUB_sx_kk():
    cpu = PicoBlaze()
    #         "011100xxxxkkkkkkkk"
    program = "011100000001111111"  # SUB s0, kk
    value_register_sx = 128
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = value_register_sx - int(program[10:], 2)
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SUB_sx_sy():
    cpu = PicoBlaze()
    #         "011101xxxxyyyy0000"
    program = "011101000011110000"  # SUB sx, sy
    value_register_sx = 16
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_register_sx = value_register_sx - value_register_sy
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SUB_sx_kk_flag_zero():
    cpu = PicoBlaze()
    #         "011100xxxxkkkkkkkk"
    program = "011100000000000001"  # SUB s0, kk
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SUB_sx_sy_flag_carry():
    cpu = PicoBlaze()
    #         "011101xxxxyyyy0000"
    program = "011101000011110000"  # SUB sx, sy
    value_register_sx = 1
    number_register_sx = 0
    value_register_sy = 2
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_SUBCY_sx_kk():
    cpu = PicoBlaze()
    #         "011010xxxxkkkkkkkk"
    program = "011110000001111111"  # SUBCY s0, kk
    value_register_sx = 128
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = value_register_sx - int(program[10:], 2) - cpu._PicoBlaze__flag_carry
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SUBCY_sx_sy():
    cpu = PicoBlaze()
    #         "011111xxxxyyyy0000"
    program = "011111000011110000"  # SUBCY sx, sy
    value_register_sx = 15
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_register_sx = value_register_sx - value_register_sy - cpu._PicoBlaze__flag_carry
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_SUBCY_sx_kk_flag_zero():
    cpu = PicoBlaze()
    #         "011110xxxxkkkkkkkk"
    program = "011110000000000001"  # SUBCY s0, kk
    value_register_sx = 2
    number_register_sx = 0
    cpu._PicoBlaze__flag_carry = 1
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_SUBCY_sx_sy_flag_carry():
    cpu = PicoBlaze()
    #         "011111xxxxyyyy0000"
    program = "011111000011110000"  # SUBCY sx, sy
    value_register_sx = 0
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_TEST_sx_kk_flag_zero():
    cpu = PicoBlaze()
    #         "010010xxxxkkkkkkkk"
    program = "010010000011111111"  # TEST s0, kk
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_TEST_sx_sy_flag_carry():
    cpu = PicoBlaze()
    #         "010011xxxxyyyykkkk"
    program = "010011000011110000"  # TEST s0, s15
    value_register_sx = 127
    number_register_sx = 0
    value_register_sy = 255
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 1
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry


def test_XOR_sx_kk():
    cpu = PicoBlaze()
    #         "001100xxxxkkkkkkkk"
    program = "001110000001111111"  # XOR s0, kk
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = value_register_sx ^ int(program[10:], 2)
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_XOR_sx_sy():
    cpu = PicoBlaze()
    #         "001111xxxxyyyy0000"
    program = "001111000011110000"  # XOR sx, sy
    value_register_sx = 3
    number_register_sx = 0
    value_register_sy = 2
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_register_sx = value_register_sx ^ value_register_sy
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_XOR_sx_kk_flag_zero():
    cpu = PicoBlaze()
    #         "001110xxxxkkkkkkkk"
    program = "001110000000000000"  # XOR s0, kk
    value_register_sx = 0
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_flag_zero = 1
    assert expected_flag_zero == cpu._PicoBlaze__flag_zero


def test_XOR_sx_sy_flag_carry():
    cpu = PicoBlaze()
    #         "001111xxxxyyyy0000"
    program = "001111000011110000"  # XOR sx, sy
    value_register_sx = 255
    number_register_sx = 0
    value_register_sy = 1
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_flag_carry = 0
    assert expected_flag_carry == cpu._PicoBlaze__flag_carry