from picoblaze import PicoBlaze


def test_CALL_program_counter_value():
    cpu = PicoBlaze()
    #         "11000000aaaaaaaaaa"
    program = "110000001111111111"  # CALL 1023
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_CALL_top_of_stack_value():
    cpu = PicoBlaze()
    #         "11000000aaaaaaaaaa"
    program = "110000001111111111"  # CALL 1023
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program)
    expected_value_top_of_stack = 50
    assert expected_value_top_of_stack == cpu._PicoBlaze__top_of_stack.get()


def test_CALL_C_executed_program_counter_value():
    cpu = PicoBlaze()
    #         "11000110aaaaaaaaaa"
    program = "110001101111111111"  # CALL C 1023
    cpu._PicoBlaze__flag_carry = 1
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_CALL_C_not_executed_top_of_stack_value():
    cpu = PicoBlaze()
    #         "11000110aaaaaaaaaa"
    program = "110001101111111111"  # CALL C 1023
    cpu._PicoBlaze__flag_carry = 0
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program)
    empty = True
    expected_value_top_of_stack = empty
    assert expected_value_top_of_stack == cpu._PicoBlaze__top_of_stack.empty()


def test_CALL_NC_executed_program_counter_value():
    cpu = PicoBlaze()
    #         "11000111aaaaaaaaaa"
    program = "110001111111111111"  # CALL NC 1023
    cpu._PicoBlaze__flag_carry = 0
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_CALL_NC_not_executed_top_of_stack_value():
    cpu = PicoBlaze()
    #         "11000111aaaaaaaaaa"
    program = "110001111111111111"  # CALL NC 1023
    cpu._PicoBlaze__flag_carry = 1
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program)
    empty = True
    expected_value_top_of_stack = empty
    assert expected_value_top_of_stack == cpu._PicoBlaze__top_of_stack.empty()


def test_CALL_Z_executed_program_counter_value():
    cpu = PicoBlaze()
    #         "11000100aaaaaaaaaa"
    program = "110001001111111111"  # CALL NC 1023
    cpu._PicoBlaze__flag_zero = 1
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_CALL_Z_not_executed_top_of_stack_value():
    cpu = PicoBlaze()
    #         "11000100aaaaaaaaaa"
    program = "110001001111111111"  # CALL NC 1023
    cpu._PicoBlaze__flag_zero = 0
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program)
    empty = True
    expected_value_top_of_stack = empty
    assert expected_value_top_of_stack == cpu._PicoBlaze__top_of_stack.empty()


def test_CALL_NZ_executed_program_counter_value():
    cpu = PicoBlaze()
    #         "11000101aaaaaaaaaa"
    program = "110001011111111111"  # CALL NC 1023
    cpu._PicoBlaze__flag_zero = 0
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_CALL_NZ_not_executed_top_of_stack_value():
    cpu = PicoBlaze()
    #         "11000101aaaaaaaaaa"
    program = "110001011111111111"  # CALL NC 1023
    cpu._PicoBlaze__flag_zero = 1
    cpu.run(program)
    empty = True
    expected_value_top_of_stack = empty
    assert expected_value_top_of_stack == cpu._PicoBlaze__top_of_stack.empty()


def test_COUNTER_increase():
    cpu = PicoBlaze()
    program = ["000000000000000000"]*1024
    #         "011000xxxxkkkkkkkk"
    program[0] = "011000000001111111"  # ADD s0, kk
    cpu.run_program(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_COUNTER_max_value():
    cpu = PicoBlaze()
    program = ["000000000000000000"]*1024
    #         "011000xxxxkkkkkkkk"
    program[1023] = "011000000001111111"  # ADD s0, kk
    cpu._PicoBlaze__program_counter = 1022
    cpu.run_program(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_COUNTER_overflow():
    cpu = PicoBlaze()
    program = ["000000000000000000"]*1024
    #         "011000xxxxkkkkkkkk"
    program[1023] = "011000000001111111"  # ADD s0, kk
    cpu._PicoBlaze__program_counter = 1023
    cpu.run_program(program)
    expected_value_program_counter = 0
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_INTERRUPT_event_executed_program_counter_value():
    cpu = PicoBlaze()
    #         "111100000000000001"
    program = "111100000000000001"  # ENABLE INTERRUPT
    cpu.run(program)
    enable = 1
    cpu.i_interrupt(enable)
    expected_value_program_counter = 0x3FF
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_INTERRUPT_event_executed_top_of_stack_value():
    cpu = PicoBlaze()
    #         "111100000000000001"
    program = "111100000000000001"  # ENABLE INTERRUPT
    cpu._PicoBlaze__program_counter = 50
    cpu.run(program) # program_counter = 50
    enable = 1
    cpu.i_interrupt(enable) # program_counter += 1 == 51
    expected_value_program_counter = 51
    assert expected_value_program_counter == cpu._PicoBlaze__top_of_stack.get()


def test_INTERRUPT_event_executed_preserved_flag_carry_value():
    cpu = PicoBlaze()
    #         "111100000000000001"
    program = "111100000000000001"  # ENABLE INTERRUPT
    cpu._PicoBlaze__flag_carry = 1
    cpu.run(program) # program_counter = 50
    enable = 1
    cpu.i_interrupt(enable) # program_counter += 1 == 51
    expected_value_preserved_flag_carry = 1
    assert expected_value_preserved_flag_carry == cpu._PicoBlaze__preserved_flag_carry


def test_INTERRUPT_event_executed_preserved_flag_zero_value():
    cpu = PicoBlaze()
    #         "111100000000000001"
    program = "111100000000000001"  # ENABLE INTERRUPT
    cpu._PicoBlaze__flag_zero = 1
    cpu.run(program) # program_counter = 50
    enable = 1
    cpu.i_interrupt(enable) # program_counter += 1 == 51
    expected_value_preserved_flag_zero = 1
    assert expected_value_preserved_flag_zero == cpu._PicoBlaze__preserved_flag_zero


def test_INTERRUPT_event_executed_flag_interrupt_value():
    cpu = PicoBlaze()
    #         "111100000000000001"
    program = "111100000000000001"  # ENABLE INTERRUPT
    cpu._PicoBlaze__flag_interrupt = 0
    cpu.run(program) # flag_interrupt = 1
    enable = 1
    cpu.i_interrupt(enable) # flag_interrupt = 0
    expected_value_flag_interrupt = 0
    assert expected_value_flag_interrupt == cpu._PicoBlaze__flag_interrupt

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


def test_JUMP():
    cpu = PicoBlaze()
    #         "11010000aaaaaaaaaa"
    program = "110100001111111111"  # JUMP 1023
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_JUMP_C_executed():
    cpu = PicoBlaze()
    #         "11010110aaaaaaaaaa"
    program = "110101101111111111"  # JUMP C 1023
    cpu._PicoBlaze__flag_carry = 1
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_JUMP_C_not_executed():
    cpu = PicoBlaze()
    #         "11010110aaaaaaaaaa"
    program = "110101101111111111"  # JUMP C 1023
    cpu._PicoBlaze__flag_carry = 0
    cpu.run(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_JUMP_NC_executed():
    cpu = PicoBlaze()
    #         "11010111aaaaaaaaaa"
    program = "110101111111111111"  # JUMP NC 1023
    cpu._PicoBlaze__flag_carry = 0
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_JUMP_NC_not_executed():
    cpu = PicoBlaze()
    #         "11010111aaaaaaaaaa"
    program = "110101111111111111"  # JUMP NC 1023
    cpu._PicoBlaze__flag_carry = 1
    cpu.run(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_JUMP_Z_executed():
    cpu = PicoBlaze()
    #         "11010100aaaaaaaaaa"
    program = "110101001111111111"  # JUMP Z 1023
    cpu._PicoBlaze__flag_zero = 1
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_JUMP_Z_not_executed():
    cpu = PicoBlaze()
    #         "11010100aaaaaaaaaa"
    program = "110101001111111111"  # JUMP Z 1023
    cpu._PicoBlaze__flag_zero = 0
    cpu.run(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_JUMP_NZ_executed():
    cpu = PicoBlaze()
    #         "11010101aaaaaaaaaa"
    program = "110101011111111111"  # JUMP NZ 1023
    cpu._PicoBlaze__flag_zero = 0
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_JUMP_NZ_not_executed():
    cpu = PicoBlaze()
    #         "11000101aaaaaaaaaa"
    program = "110001011111111111"  # JUMP NZ 1023
    cpu._PicoBlaze__flag_zero = 1
    cpu.run(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


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


def test_RESET_top_of_stack_empty():
    cpu = PicoBlaze()
    #         "10101000aaaaaaaaaa"
    program = "101010001111111111"  # RETURN 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    cpu.i_reset()
    empty = True
    expected_value_top_of_stack = empty
    assert expected_value_top_of_stack == cpu._PicoBlaze__top_of_stack.empty()


def test_RESET_program_counter_equal_zero():
    cpu = PicoBlaze()
    #         "10101000aaaaaaaaaa"
    program = "101010001111111111"  # RETURN 1023
    cpu._PicoBlaze__program_counter = 50
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    cpu.i_reset()
    expected_value_program_counter = 0
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RESET_flag_zero_equal_zero():
    cpu = PicoBlaze()
    #         "10101000aaaaaaaaaa"
    program = "101010001111111111"  # RETURN 1023
    cpu._PicoBlaze__flag_zero = 1
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    cpu.i_reset()
    expected_value_flag_zero = 0
    assert expected_value_flag_zero == cpu._PicoBlaze__flag_zero


def test_RESET_flag_carry_equal_zero():
    cpu = PicoBlaze()
    #         "10101000aaaaaaaaaa"
    program = "101010001111111111"  # RETURN 1023
    cpu._PicoBlaze__flag_carry = 1
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    cpu.i_reset()
    expected_value_flag_carry = 0
    assert expected_value_flag_carry == cpu._PicoBlaze__flag_carry

def test_RETURN():
    cpu = PicoBlaze()
    #         "10101000aaaaaaaaaa"
    program = "101010001111111111"  # RETURN 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURN_C_executed():
    cpu = PicoBlaze()
    #         "10101110aaaaaaaaaa"
    program = "101011101111111111"  # RETURN C 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu._PicoBlaze__flag_carry = 1
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURN_C_not_executed():
    cpu = PicoBlaze()
    #         "10101110aaaaaaaaaa"
    program = "101011101111111111"  # RETURN C 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu._PicoBlaze__flag_carry = 0
    cpu.run(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURN_NC_executed():
    cpu = PicoBlaze()
    #         "10101111aaaaaaaaaa"
    program = "101011111111111111"  # RETURN NC 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu._PicoBlaze__flag_carry = 0
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURN_NC_not_executed():
    cpu = PicoBlaze()
    #         "10101111aaaaaaaaaa"
    program = "101011111111111111"  # RETURN NC 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu._PicoBlaze__flag_carry = 1
    cpu.run(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURN_Z_executed():
    cpu = PicoBlaze()
    #         "10101100aaaaaaaaaa"
    program = "101011001111111111"  # RETURN Z 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu._PicoBlaze__flag_zero = 1
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURN_Z_not_executed():
    cpu = PicoBlaze()
    #         "10101100aaaaaaaaaa"
    program = "101011001111111111"  # RETURN Z 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu._PicoBlaze__flag_zero = 0
    cpu.run(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURN_NZ_executed():
    cpu = PicoBlaze()
    #         "10101101aaaaaaaaaa"
    program = "101011011111111111"  # RETURN NZ 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu._PicoBlaze__flag_zero = 0
    cpu.run(program)
    expected_value_program_counter = 1023
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURN_NZ_not_executed():
    cpu = PicoBlaze()
    #         "10101101aaaaaaaaaa"
    program = "101011011111111111"  # RETURN NZ 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu._PicoBlaze__flag_zero = 1
    cpu.run(program)
    expected_value_program_counter = 1
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURNI_DISABLE_program_counter_value():
    cpu = PicoBlaze()
    #         "111000000000000000"
    program = "111000000000000000"  # RETURN NZ 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_program_counter = 1022
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURNI_DISABLE_flag_carry_value():
    cpu = PicoBlaze()
    #         "111000000000000000"
    program = "111000000000000000"  # RETURN NZ 1023
    cpu._PicoBlaze__preserved_flag_carry = 1
    cpu._PicoBlaze__flag_carry = 0
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_flag_carry = 1
    assert expected_value_flag_carry == cpu._PicoBlaze__flag_carry


def test_RETURNI_DISABLE_flag_zero_value():
    cpu = PicoBlaze()
    #         "111000000000000000"
    program = "111000000000000000"  # RETURN NZ 1023
    cpu._PicoBlaze__preserved_flag_zero = 1
    cpu._PicoBlaze__flag_zero = 0
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_flag_zero = 1
    assert expected_value_flag_zero == cpu._PicoBlaze__flag_zero


def test_RETURNI_DISABLE_flag_interrupt_disable():
    cpu = PicoBlaze()
    #         "111000000000000000"
    program = "111000000000000000"  # RETURN NZ 1023
    cpu._PicoBlaze__preserved_flag_zero = 1
    cpu._PicoBlaze__flag_interrupt = 1
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_flag_interrupt = 0
    assert expected_value_flag_interrupt == cpu._PicoBlaze__flag_interrupt


def test_RETURNI_ENABLE_program_counter_value():
    cpu = PicoBlaze()
    #         "111000000000000001"
    program = "111000000000000001"  # RETURN NZ 1023
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_program_counter = 1022
    assert expected_value_program_counter == cpu._PicoBlaze__program_counter


def test_RETURNI_ENABLE_flag_carry_value():
    cpu = PicoBlaze()
    #         "111000000000000001"
    program = "111000000000000001"  # RETURN NZ 1023
    cpu._PicoBlaze__preserved_flag_carry = 1
    cpu._PicoBlaze__flag_carry = 0
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_flag_carry = 1
    assert expected_value_flag_carry == cpu._PicoBlaze__flag_carry


def test_RETURNI_ENABLE_flag_zero_value():
    cpu = PicoBlaze()
    #         "111000000000000001"
    program = "111000000000000001"  # RETURN NZ 1023
    cpu._PicoBlaze__preserved_flag_zero = 1
    cpu._PicoBlaze__flag_zero = 0
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_flag_zero = 1
    assert expected_value_flag_zero == cpu._PicoBlaze__flag_zero


def test_RETURNI_ENABLE_flag_interrupt_enable():
    cpu = PicoBlaze()
    #         "111000000000000001"
    program = "111000000000000001"  # RETURN NZ 1023
    cpu._PicoBlaze__preserved_flag_zero = 1
    cpu._PicoBlaze__flag_interrupt = 1
    cpu._PicoBlaze__top_of_stack.put(1022)
    cpu.run(program)
    expected_value_flag_interrupt = 1
    assert expected_value_flag_interrupt == cpu._PicoBlaze__flag_interrupt


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
