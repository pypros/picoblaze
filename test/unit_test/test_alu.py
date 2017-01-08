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
    # assert True == True


def test_ADDCY_sx_sy():
    #         "011011xxxxyyyy0000" ADD
    assert True == True

def test_ADDCY_sx_kk_flag_zero():
    #         "011010xxxxkkkkkkkk"
    assert True == True


def test_ADDCY_sx_sy_flag_carry():
    #         "011011xxxxyyyy0000"
    assert True == True