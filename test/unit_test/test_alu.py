from picoblaze import PicoBlaze


def test_ADD_sx_kk():
    cpu = PicoBlaze()
    #         "011000xxxxkkkkkkkk"
    program = "011000000001111111"  # OUTPUT s0, kk
    value_register_sx = 1
    number_register_sx = 0
    cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
    cpu.run(program)
    expected_register_sx = value_register_sx + int(program[10:], 2)
    assert expected_register_sx == cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx]


# def test_ADD_sx_sy():
#     cpu = PicoBlaze()
#     #         "011001xxxxyyyy0000"
#     program = "101101000011110000"  # OUTPUT sx, sy
#     value_register_sx = 255
#     number_register_sx = 0
#     value_register_sy = 127
#     number_register_sy = 15
#     out_port_id = 127
#     cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sx] = value_register_sx
#     cpu._PicoBlaze__sixteen_byte_wide_registers[number_register_sy] = value_register_sy
#     cpu.run(program)
#     assert (value_register_sx, out_port_id) == (cpu.o_out_port, cpu.o_port_id)
