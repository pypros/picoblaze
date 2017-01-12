from picoblaze import PicoBlaze


def test_INTERRUPT_DISABLE():
    cpu = PicoBlaze()
    #         "111100000000000000"
    program = "111100000000000000"  # DISABLE INTERRUPT
    cpu._PicoBlaze__flag_interrupt = 1
    cpu.run(program)
    expected_flag_interrupt = 0
    assert expected_flag_interrupt == cpu._PicoBlaze__flag_interrupt


def test_INTERRUPT_ENABLE():
    cpu = PicoBlaze()
    #         "111100000000000001"
    program = "111100000000000001"  # ENABLE INTERRUPT
    cpu._PicoBlaze__flag_interrupt = 0
    cpu.run(program)
    expected_flag_interrupt = 1
    assert expected_flag_interrupt == cpu._PicoBlaze__flag_interrupt


def test_FETCH_sx_kk():
    cpu = PicoBlaze()
    #         "000110xxxx00kkkkkk"
    program = "000110000000111111"  # FETCH s0, kk
    cpu._PicoBlaze__sixty_four_byte_scratchpad_ram[63] = 127
    number_register_sx = 0
    cpu.run(program)
    expected_value_register_sx = 127
    assert expected_value_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_FETCH_sx_sy():
    cpu = PicoBlaze()
    #         "000111xxxxyyyy0000"
    program = "000111000011110000"  # COMPARE sx, sy
    number_register_sx = 0
    value_register_sy = 63
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu._PicoBlaze__sixty_four_byte_scratchpad_ram[63] = 127
    cpu.run(program)
    expected_value_register_sx = 127
    assert expected_value_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]



def test_FETCH_sx_kk():
    cpu = PicoBlaze()
    #         "000110xxxx00kkkkkk"
    program = "000110000000111111"  # FETCH s0, kk
    cpu._PicoBlaze__sixty_four_byte_scratchpad_ram[63] = 127
    number_register_sx = 0
    cpu.run(program)
    expected_value_register_sx = 127
    assert expected_value_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_FETCH_sx_sy():
    cpu = PicoBlaze()
    #         "000111xxxxyyyy0000"
    program = "000111000011110000"  # COMPARE sx, sy
    number_register_sx = 0
    value_register_sy = 63
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu._PicoBlaze__sixty_four_byte_scratchpad_ram[63] = 127
    cpu.run(program)
    expected_value_register_sx = 127
    assert expected_value_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_INPUT_sx_kk():
    cpu = PicoBlaze()
    #         "000100xxxxkkkkkkkk"
    program = "000100000011111111"  # INPUT s0, kk
    cpu.i_in_port = 170
    number_register_sx = 0
    cpu.run(program)
    expected_register_sx = 170
    expected_out_port_id = 255
    assert (expected_register_sx, expected_out_port_id) == (cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx], cpu.o_port_id)


def test_INPUT_sx_sy():
    cpu = PicoBlaze()
    #         "000101xxxxyyyy0000"
    program = "000101000011110000"  # INPUT sx, sy
    cpu.i_in_port = 170
    number_register_sx = 0
    value_register_sy = 255
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_register_sx = 170
    expected_out_port_id = 255
    assert (expected_register_sx, expected_out_port_id) == (cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx], cpu.o_port_id)


def test_LOAD_sx_kk():
    cpu = PicoBlaze()
    #         "000000xxxxkkkkkkkk"
    program = "000000000011111111"  # LOAD s0, kk
    number_register_sx = 0
    cpu.run(program)
    expected_value_register_sx = 255
    assert expected_value_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


def test_LOAD_sx_sy():
    cpu = PicoBlaze()
    #         "000001xxxxyyyy0000"
    program = "000001000011110000"  # LOAD sx, sy
    number_register_sx = 0
    value_register_sy = 255
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_value_register_sx = 255
    assert expected_value_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]



def test_OUTPUT_sx_kk():
    cpu = PicoBlaze()
    #         "101100xxxxkkkkkkkk"
    program = "101100000000000000"  # OUTPUT s0, kk
    value_register_sx = 255
    number_register_sx = 0
    out_port_id = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    assert (value_register_sx, out_port_id) == (cpu.o_out_port, cpu.o_port_id)


def test_OUTPUT_sx_sy():
    cpu = PicoBlaze()
    #         "101101xxxxyyyy0000"
    program = "101101000011110000"  # OUTPUT sx, sy
    value_register_sx = 255
    number_register_sx = 0
    value_register_sy = 127
    number_register_sy = 15
    out_port_id = 127
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    assert (value_register_sx, out_port_id) == (cpu.o_out_port, cpu.o_port_id)


def test_STORE_sx_kk():
    cpu = PicoBlaze()
    #         "000110xxxx00kkkkkk"
    program = "101110000000111111"  # FETCH s0, kk
    value_register_sx = 3
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_value_record_from_sixty_four_byte_scratchpad_ram = 3
    assert expected_value_record_from_sixty_four_byte_scratchpad_ram == cpu._PicoBlaze__sixty_four_byte_scratchpad_ram[63]


def test_STORE_sx_sy():
    cpu = PicoBlaze()
    #         "000111xxxxyyyy0000"
    program = "101111000011110000"  # FETCH s0, kk
    value_register_sx = 3
    number_register_sx = 0
    value_register_sy = 63
    number_register_sy = 15
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
    cpu.run(program)
    expected_value_record_from_sixty_four_byte_scratchpad_ram = 3
    assert expected_value_record_from_sixty_four_byte_scratchpad_ram == cpu._PicoBlaze__sixty_four_byte_scratchpad_ram[63]
