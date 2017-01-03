class Program:
    def __init__(self):
        self.bit_size_instruction = 18
        self.amount_instructions = 1024
        self.program = [[0]*self.bit_size_instruction] * self.amount_instructions
        self.program_line = -1

    def get_instruction(self):
        self.program_line += 1
        return self.program[self.program_line]
