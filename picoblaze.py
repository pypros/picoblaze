class PicoBlaze:
    def __init__(self):
        self.i_in_port = [0] * 8
        self.i_interrupt = 0
        self.i_reset = 0
        self.i_clk = 0
        self.o_out_port = [0] * 8
        self.o_port_id = [0] * 8
        self.o_read_strobe = 0
        self.o_write_strobe = 0
        self.o_interrupt_ack = 0