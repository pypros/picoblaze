from picoblaze import PicoBlaze


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
