from internal_element_picoblaze.instruction_program_store import Program
from internal_element_picoblaze.general_purpose_registers import SixteenByteWideRegisters
from internal_element_picoblaze.instruction_decoder import Decoder


class PicoBlaze:
    def __init__(self):
        self.i_in_port = 0
        self.i_interrupt = 0
        self.i_reset = 0
        self.i_clk = 0
        self.o_out_port = 0
        self.o_port_id = 0
        self.o_read_strobe = 0
        self.o_write_strobe = 0
        self.o_interrupt_ack = 0
        self.__Program = Program()
        self.__Decoder = Decoder()
        self.__SixteenByteWideRegisters = SixteenByteWideRegisters()

    def run(self):
        pass