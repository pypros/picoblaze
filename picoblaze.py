import Queue

class PicoBlaze:
    def __init__(self):
        self.i_in_port = 0
        self.i_interrupt = 0
        self.i_clk = 0
        self.o_out_port = 0
        self.o_port_id = 0
        self.o_read_strobe = 0
        self.o_write_strobe = 0
        self.o_interrupt_ack = 0
        self.__flag_zero = 0
        self.__flag_carry = 0
        self.__flag_interrupt = 0
        self.__preserved_flag_zero = 0
        self.__preserved_flag_carry = 0
        self.__instruction = '0'*16
        self.__program_counter = 0
        self.__top_of_stack = Queue.LifoQueue()
        self.__sixteen_byte_wide_registers = [0]*16
        self.__sixty_four_byte_scratchpad_ram = [0]*64
        self.__sixteen_byte_wide_registers = [0] * 16
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

    def __ADD(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        register_sx = (sx + operand) % 256

        if (sx + operand) > 255:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        if (sx + operand == 0) or (sx + operand == 256):
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__sixteen_byte_wide_registers[sx_number] = register_sx
        self.__program_counter += 1

    def __ADDCY(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        carry = self.__flag_carry

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        if carry:
            register_sx = (sx + operand + 1) % 256
        else:
            register_sx = (sx + operand) % 256

        if sx + operand + carry > 255:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        if (sx + operand + carry == 0) or (sx + operand + carry == 256):
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__sixteen_byte_wide_registers[sx_number] = register_sx
        self.__program_counter += 1

    def __AND(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        register_sx = sx & operand

        self.__flag_carry = 0

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__sixteen_byte_wide_registers[sx_number] = register_sx
        self.__program_counter += 1

    def __CALL(self):
        address = int(self.__instruction[8:], 2)
        pc = self.__program_counter
        self.__top_of_stack.put(pc)
        self.__program_counter = address

    def __CALL_C(self):
        address = int(self.__instruction[8:], 2)
        pc = self.__program_counter
        if self.__flag_carry:
            self.__top_of_stack.put(pc)
            self.__program_counter = address
        else:
            self.__program_counter += 1

    def __CALL_NC(self):
        address = int(self.__instruction[8:], 2)
        pc = self.__program_counter
        if not self.__flag_carry:
            self.__top_of_stack.put(pc)
            self.__program_counter = address
        else:
            self.__program_counter += 1

    def __CALL_Z(self):
        address = int(self.__instruction[8:], 2)
        pc = self.__program_counter
        if self.__flag_zero:
            self.__top_of_stack.put(pc)
            self.__program_counter = address
        else:
            self.__program_counter += 1

    def __CALL_NZ(self):
        address = int(self.__instruction[8:], 2)
        pc = self.__program_counter
        if not self.__flag_zero:
            self.__top_of_stack.put(pc)
            self.__program_counter = address
        else:
            self.__program_counter += 1

    def __COMPARE(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        if operand > sx:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        if operand == sx:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __INTERRUPT(self):
        self.__flag_interrupt = int(self.__instruction[-1], 2)
        self.__program_counter += 1

    def __JUMP(self):
        address = int(self.__instruction[8:], 2)
        self.__program_counter = address

    def __JUMP_C(self):
        address = int(self.__instruction[8:], 2)
        if self.__flag_carry:
            self.__program_counter = address
        else:
            self.__program_counter += 1

    def __JUMP_NC(self):
        address = int(self.__instruction[8:], 2)
        if not self.__flag_carry:
            self.__program_counter = address
        else:
            self.__program_counter += 1

    def __JUMP_Z(self):
        address = int(self.__instruction[8:], 2)
        if self.__flag_zero:
            self.__program_counter = address
        else:
            self.__program_counter += 1

    def __JUMP_NZ(self):
        address = int(self.__instruction[8:], 2)
        if not self.__flag_zero:
            self.__program_counter = address
        else:
            self.__program_counter += 1

    def __FETCH(self):
        sx_number = int(self.__instruction[6:10], 2)

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[12:], 2)

        self.__sixteen_byte_wide_registers[sx_number] = self.__sixty_four_byte_scratchpad_ram[operand]

        self.__program_counter += 1

    def __INPUT(self):
        sx_number = int(self.__instruction[6:10], 2)

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        self.__sixteen_byte_wide_registers[sx_number] = self.i_in_port
        self.o_port_id = operand

        self.__program_counter += 1

    def __LOAD(self):
        sx_number = int(self.__instruction[6:10], 2)

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        self.__sixteen_byte_wide_registers[sx_number] = operand

        self.__program_counter += 1

    def __OR(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        register_sx = sx | operand

        self.__flag_carry = 0

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__sixteen_byte_wide_registers[sx_number] = register_sx
        self.__program_counter += 1

    def __OUTPUT(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]
        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        self.o_port_id = operand
        self.o_out_port = sx

        self.__program_counter += 1

    def i_reset(self):
        self.__RESET()

    def __RESET(self):
        self.__program_counter = 0
        self.__flag_zero = 0
        self.__flag_carry = 0
        self.__flag_interrupt = 0
        while not self.__top_of_stack.empty():
            self.__top_of_stack.get()

    def __RETURN(self):
        self.__program_counter = self.__top_of_stack.get() + 1

    def __RETURN_C(self):
        if self.__flag_carry:
            self.__program_counter = self.__top_of_stack.get() + 1
        else:
            self.__program_counter += 1

    def __RETURN_NC(self):
        if not self.__flag_carry:
            self.__program_counter = self.__top_of_stack.get() + 1
        else:
            self.__program_counter += 1

    def __RETURN_Z(self):
        if self.__flag_zero:
            self.__program_counter = self.__top_of_stack.get() + 1
        else:
            self.__program_counter += 1

    def __RETURN_NZ(self):
        if not self.__flag_zero:
            self.__program_counter = self.__top_of_stack.get() + 1
        else:
            self.__program_counter += 1

    def __RETURNI_DISABLE(self):
        self.__program_counter = self.__top_of_stack.get()
        self.__flag_carry = self.__preserved_flag_carry
        self.__flag_zero = self.__preserved_flag_zero
        self.__flag_interrupt = 0

    def __RETURNI_ENABLE(self):
        self.__program_counter = self.__top_of_stack.get()
        self.__flag_carry = self.__preserved_flag_carry
        self.__flag_zero = self.__preserved_flag_zero
        self.__flag_interrupt = 1

    def __RL(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        rl_sx = str_sx[1:] + str_sx[0]
        self.__sixteen_byte_wide_registers[sx_number] = int(rl_sx, 2)
        self.__flag_carry = int(str_sx[0])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __RR(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        rr_sx = str_sx[7] + str_sx[0:7]

        self.__sixteen_byte_wide_registers[sx_number] = int(rr_sx, 2)
        self.__flag_carry = int(str_sx[7])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SL0(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        sl0 = sx << 1
        self.__sixteen_byte_wide_registers[sx_number] = sl0

        self.__flag_carry = int(str_sx[0])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SL1(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        sl1_sx = str_sx[1:] + '1'

        self.__sixteen_byte_wide_registers[sx_number] = int(sl1_sx, 2)
        self.__flag_carry = int(str_sx[0])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SLA(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        sla_sx = str_sx[1:] + str(self.__flag_carry)
        self.__sixteen_byte_wide_registers[sx_number] = int(sla_sx, 2)

        self.__flag_carry = int(str_sx[0])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SLX(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        slx_sx = str_sx[1:] + str_sx[7]
        self.__sixteen_byte_wide_registers[sx_number] = int(slx_sx, 2)

        self.__flag_carry = int(str_sx[0])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SR0(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        sr0 = self.__sixteen_byte_wide_registers[sx_number] >> 1
        self.__sixteen_byte_wide_registers[sx_number] = sr0

        self.__flag_carry = int(str_sx[7])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SR1(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        sr1_sx = '1' + str_sx[0:7]

        self.__sixteen_byte_wide_registers[sx_number] = int(sr1_sx, 2)
        self.__flag_carry = int(str_sx[7])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SRA(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        sra_sx = str(self.__flag_carry) + str_sx[0:7]

        self.__sixteen_byte_wide_registers[sx_number] = int(sra_sx, 2)
        self.__flag_carry = int(str_sx[7])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __SRX(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        str_sx = format(sx, 'b').zfill(8)
        srx_sx = str_sx[0] + str_sx[0:7]

        self.__sixteen_byte_wide_registers[sx_number] = int(srx_sx, 2)

        self.__flag_carry = int(str_sx[7])

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__program_counter += 1

    def __STORE(self):
        sx_number = int(self.__instruction[6:10], 2)

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[12:], 2)

        self.__sixty_four_byte_scratchpad_ram[operand] = self.__sixteen_byte_wide_registers[sx_number]

        self.__program_counter += 1

    def __SUB(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        register_sx = (sx - operand) % 256

        if (sx - operand) < 0:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        if (sx - operand) == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__sixteen_byte_wide_registers[sx_number] = register_sx
        self.__program_counter += 1

    def __SUBCY(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        carry = self.__flag_carry

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        if carry:
            register_sx = (sx - operand - 1) % 256
        else:
            register_sx = (sx - operand) % 256

        if sx - operand - carry < 0:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        if (sx - operand - carry == 0) or (sx - operand - carry == -256):
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__sixteen_byte_wide_registers[sx_number] = register_sx
        self.__program_counter += 1

    def __TEST(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        and_test = ""
        str_sx = str(bin(sx))[2:].zfill(8)
        str_operand = str(bin(operand))[2:].zfill(8)
        for bit_sx, bit_operand in zip(str_sx, str_operand):
            and_test += str(int(bit_sx) & int(bit_operand))

        and_test = int(and_test, 2)

        if and_test == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        xor_test = 0

        for bit_and_test in str(bin(and_test))[2:].zfill(8):
            xor_test = int(bit_and_test) ^ xor_test

        if xor_test == 1:
            self.__flag_carry = 1
        else:
            self.__flag_carry = 0

        self.__program_counter += 1

    def __XOR(self):
        sx_number = int(self.__instruction[6:10], 2)
        sx = self.__sixteen_byte_wide_registers[sx_number]

        if self.__instruction[5] == '1':
            sy_number = int(self.__instruction[10:14], 2)
            operand = self.__sixteen_byte_wide_registers[sy_number]
        else:
            operand = int(self.__instruction[10:], 2)

        register_sx = sx ^ operand

        self.__flag_carry = 0

        if sx == 0:
            self.__flag_zero = 1
        else:
            self.__flag_zero = 0

        self.__sixteen_byte_wide_registers[sx_number] = register_sx
        self.__program_counter += 1

    def __exec_instruction(self, name_instruction):
        if name_instruction == "ADD":
            self.__ADD()
        elif name_instruction == "ADDCY":
            self.__ADDCY()
        elif name_instruction == "AND":
            self.__AND()
        elif name_instruction == "CALL":
            if self.__instruction[5:8] == "000":
                self.__CALL()
            elif self.__instruction[5:8] == "110":
                self.__CALL_C()
            elif self.__instruction[5:8] == "111":
                self.__CALL_NC()
            elif self.__instruction[5:8] == "100":
                self.__CALL_Z()
            elif self.__instruction[5:8] == "101":
                self.__CALL_NZ()
        elif name_instruction == "COMPARE":
            self.__COMPARE()
        elif name_instruction == "INTERRUPT":
            self.__INTERRUPT()
        elif name_instruction == "FETCH":
            self.__FETCH()
        elif name_instruction == "INPUT":
            self.__INPUT()
        elif name_instruction == "JUMP":
            if self.__instruction[5:8] == "000":
                self.__JUMP()
            elif self.__instruction[5:8] == "110":
                self.__JUMP_C()
            elif self.__instruction[5:8] == "111":
                self.__JUMP_NC()
            elif self.__instruction[5:8] == "100":
                self.__JUMP_Z()
            elif self.__instruction[5:8] == "101":
                self.__JUMP_NZ()
        elif name_instruction == "LOAD":
            self.__LOAD()
        elif name_instruction == "OR":
            self.__OR()
        elif name_instruction == "OUTPUT":
            self.__OUTPUT()
        elif name_instruction == "RETURN":
            if self.__instruction[5:8] == "000":
                self.__RETURN()
            elif self.__instruction[5:8] == "110":
                self.__RETURN_C()
            elif self.__instruction[5:8] == "111":
                self.__RETURN_NC()
            elif self.__instruction[5:8] == "100":
                self.__RETURN_Z()
            elif self.__instruction[5:8] == "101":
                self.__RETURN_NZ()
        elif name_instruction == "RETURNI":
            if self.__instruction[-1] == "0":
                self.__RETURNI_DISABLE()
            elif self.__instruction[-1] == "1":
                self.__RETURNI_ENABLE()
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
            elif self.__instruction[14:18] == "1110":
                self.__SR0()
            elif self.__instruction[14:18] == "1111":
                self.__SR1()
            elif self.__instruction[14:18] == "1000":
                self.__SRA()
            elif self.__instruction[14:18] == "1010":
                self.__SRX()
        elif name_instruction == "STORE":
            self.__STORE()
        elif name_instruction == "SUB":
            self.__SUB()
        elif name_instruction == "SUBCY":
            self.__SUBCY()
        elif name_instruction == "TEST":
            self.__TEST()
        elif name_instruction == "XOR":
            self.__XOR()
        else:
            print "instruction unsupported"

    def run(self, instruction):
        self.__instruction = instruction
        name = self.__operation[self.__instruction[0:5]]
        self.__exec_instruction(name)