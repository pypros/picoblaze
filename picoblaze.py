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
        self.__flag_zero = 0
        self.__flag_carry = 0
        self.__preserved_flag_zero = 0
        self.__preserved_flag_carry = 0
        self.__instruction = '0'*16
        self.__program_counter = 0
        self.__sixteen_byte_wide_registers = [0]*16
        self.__operation = {
            "01100": "ADD",
            "01101": "ADDCY",
            "00101": "AND",
            "11000": "CALL",
            "01010": "COMPARE",
            "11110": "INTERRUPT",
            "00011": "FETCH",
            "00010": "INPUT",
            "11010": "JUMP",
            "00000": "LOAD",
            "00110": "OR",
            "10110": "OUTPUT",
            "10101": "RETURN",
            "11100": "RETURNI",
            "10000": "SHIFT",
            "10111": "STORE",
            "01110": "SUB",
            "01111": "SUBCY",
            "01001": "TEST",
            "00111": "XOR"
        }

# ALU
    def __ADD(self):
        sx = int(self.__instruction[6:10], 2)
        if self.__instruction[5] == '1':
            operand = int(self.__instruction[10:14], 2)
        else:
            operand = int(self.__instruction[10:], 2)

        self.__sixteen_byte_wide_registers[sx] = (self.__sixteen_byte_wide_registers[sx]
                                                  + self.__sixteen_byte_wide_registers[operand]) % 256
        if (self.__sixteen_byte_wide_registers[sx]
                + self.__sixteen_byte_wide_registers[operand]) > 255:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        if ((self.__sixteen_byte_wide_registers[sx] + self.__sixteen_byte_wide_registers[operand] == 0) or
                (self.__sixteen_byte_wide_registers[sx] + self.__sixteen_byte_wide_registers[operand]) == 256):
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __ADDCY(self):
        sx = int(self.__instruction[6:10], 2)
        if self.__instruction[5] == '1':
            operand = int(self.__instruction[10:14], 2)
        else:
            operand = int(self.__instruction[10:], 2)

        self.__sixteen_byte_wide_registers[sx] = (self.__sixteen_byte_wide_registers[sx]
                                                  + self.__sixteen_byte_wide_registers[operand] + self.__flag_carry) % 256

        if self.__flag_carry:
            sx = (sx + operand + 1) % 256
        else:
            sx = (sx + operand) % 256

        if (self.__sixteen_byte_wide_registers[sx]
                + self.__sixteen_byte_wide_registers[operand] + self.__flag_carry) > 255:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        if ((self.__sixteen_byte_wide_registers[sx] + self.__sixteen_byte_wide_registers[operand] == 0) or
                (self.__sixteen_byte_wide_registers[sx] + self.__sixteen_byte_wide_registers[operand] + self.__flag_carry) == 256):
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __AND(self):
        sx = int(self.__instruction[6:10], 2)
        if self.__instruction[5] == '1':
            operand = int(self.__instruction[10:14], 2)
        else:
            operand = int(self.__instruction[10:], 2)

        self.__sixteen_byte_wide_registers[sx] &= self.__sixteen_byte_wide_registers[operand]
        self.__flag_carry = 0

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __COMPARE(self):
        sx = int(self.__instruction[6:10], 2)
        if self.__instruction[5] == '1':
            operand = int(self.__instruction[10:14], 2)
        else:
            operand = int(self.__instruction[10:], 2)

        if self.__sixteen_byte_wide_registers[operand] > self.__sixteen_byte_wide_registers[sx]:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        if self.__sixteen_byte_wide_registers[operand] == self.__sixteen_byte_wide_registers[sx]:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __OR(self):
        sx = int(self.__instruction[6:10], 2)
        if self.__instruction[5] == '1':
            operand = int(self.__instruction[10:14], 2)
        else:
            operand = int(self.__instruction[10:], 2)

        self.__sixteen_byte_wide_registers[sx] |= self.__sixteen_byte_wide_registers[operand]

        self.__flag_carry = 0

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __RL(self):
        sx = int(self.__instruction[6:10], 2)

        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        rl_sx = str_sx[1:] + str_sx[0]
        self.__sixteen_byte_wide_registers[sx] = int(rl_sx, 2)
        self.__flag_carry = int(str_sx[0])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __RR(self):
        sx = int(self.__instruction[6:10], 2)

        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        rr_sx = str_sx[7] + str_sx[0:7]
        self.__sixteen_byte_wide_registers[sx] = int(rr_sx, 2)
        self.__flag_carry = int(str_sx[7])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SL0(self):
        sx = int(self.__instruction[6:10], 2)
        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        sl0 = self.__sixteen_byte_wide_registers[sx] << 1
        self.__sixteen_byte_wide_registers[sx] = sl0

        self.__flag_carry = int(str_sx[0])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SL1(self):
        sx = int(self.__instruction[6:10], 2)
        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        sl1_sx = str_sx[1:] + '1'

        self.__sixteen_byte_wide_registers[sx] = int(sl1_sx, 2)
        self.__flag_carry = int(str_sx[0])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SLA(self):
        sx = int(self.__instruction[6:10], 2)
        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        sla_sx = str_sx[1:] + str(self.__flag_carry)
        self.__sixteen_byte_wide_registers[sx] = int(sla_sx, 2)

        self.__flag_carry = int(str_sx[0])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SLX(self):
        sx = int(self.__instruction[6:10], 2)
        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        slx_sx = str_sx[1:] + str_sx[7]
        self.__sixteen_byte_wide_registers[sx] = int(slx_sx, 2)

        self.__flag_carry = int(str_sx[0])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SR0(self):
        sx = int(self.__instruction[6:10], 2)
        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        sr0 = self.__sixteen_byte_wide_registers[sx] >> 1
        self.__sixteen_byte_wide_registers[sx] = sr0

        self.__flag_carry = int(str_sx[7])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SR1(self):
        sx = int(self.__instruction[6:10], 2)
        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        sr1_sx = '1' + str_sx[0:7]

        self.__sixteen_byte_wide_registers[sx] = int(sr1_sx, 2)
        self.__flag_carry = int(str_sx[7])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SRA(self):
        sx = int(self.__instruction[6:10], 2)
        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        sra_sx = str(self.__flag_carry) + str_sx[0:7]
        self.__sixteen_byte_wide_registers[sx] = int(sra_sx, 2)

        self.__flag_carry = int(str_sx[7])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SRX(self):
        sx = int(self.__instruction[6:10], 2)
        str_sx = format(self.__sixteen_byte_wide_registers[sx], 'b').zfill(8)
        srx_sx = str_sx[0] + str_sx[0:7]
        self.__sixteen_byte_wide_registers[sx] = int(srx_sx, 2)

        self.__flag_carry = int(str_sx[7])

        if self.__sixteen_byte_wide_registers[sx] == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __exec_instruction(self, name_instruction):
        if name_instruction == "ADD":
            self.__ADD()
        elif name_instruction == "ADDCY":
            self.__ADDCY()
        elif name_instruction == "AND":
            self.__AND()
        elif name_instruction == "COMPARE":
            self.__COMPARE()
        elif name_instruction == "OR":
            self.__OR()
        elif name_instruction == "SHIFT":
            if self.__instruction[14:18] == "0010":
                self.__RL()
            elif self.__instruction[14:18] == "1100":
                self.__RR()
            elif self.__instruction[14:18] == "0110":
                self.__SL0()
            elif self.__instruction[14:18] == "0111":
                self.__SL1()
            elif self.__instruction[14:18] == "0000":
                self.__SLA()
            elif self.__instruction[14:18] == "0100":
                self.__SLX()
            # elif self.__instruction[14:18] == "1110":
            #     self.__SR0()
            # elif self.__instruction[14:18] == "1111":
            #     self.__SR1()
            # elif self.__instruction[14:18] == "1000":
            #     self.__SRA()
            # elif self.__instruction[14:18] == "1010":
            #     self.__SRX()
        else:
            print "instruction unsupported"

    def run(self):
        # instruction = self.__program.get_instruction()
        print self.__sixteen_byte_wide_registers
        self.__instruction = "100000111100000110" #ADD s0,s15
        self.__sixteen_byte_wide_registers[15] = 1
        # self.__sixteen_byte_wide_registers[15] = 15
        print self.__sixteen_byte_wide_registers
        name_instruction = self.__operation[self.__instruction[0:5]]
        print name_instruction
        self.__exec_instruction(name_instruction)
        print int(self.__instruction[6:10], 2)
        print int(self.__instruction[10:14], 2)
        print self.__sixteen_byte_wide_registers

cpu = PicoBlaze()
cpu.run()
