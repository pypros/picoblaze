class Decoder:
    def __init__(self):
        self.bit_size_instruction = 0
        self.instruction = 0
        self.absolute_instruction_address = 0
        self.register_sx = 0
        self.register_sy = 0
        self.immediate_constant = 0
        self.port_address = 0
        self.scratchpad_ram_address = 0
        self.operation = 0
        self.component_responsible_for_operation = {
            'ADD': 'ALU',
            'ADDCY': 'ALU',
            'AND': 'ALU',
            'CALL': '',
            'COMPARE': 'ALU',
            'INTERRUPT': '',
            'FETCH': '',
            'INPUT': '',
            'JUMP': '',
            'LOAD': '',
            'OR': 'ALU',
            'OUTPUT': '',
            'RETURN': '',
            'RETURNI': '',
            'SHIFT': 'ALU',
            'STORE': '',
            'SUB': 'ALU',
            'SUBCY': 'ALU',
            'TEST': 'ALU',
            'XOR': 'ALU',

        }
        self.operations_use_register_sx = [
            'ADD',
            'ADDCY',
            'AND',
            'COMPARE',
            'FETCH',
            'INPUT',
            'LOAD',
            'OR',
            'OUTPUT',
            'SHIFT',
            'STORE',
            'SUB',
            'SUBCY',
            'TEST',
            'XOR'

        ]

        self.operations_use_register_sy = [
            'ADD',
            'ADDCY',
            'AND',
            'COMPARE',
            'FETCH',
            'INPUT',
            'LOAD',
            'OR',
            'OUTPUT',
            'STORE',
            'SUB',
            'SUBCY',
            'TEST',
            'XOR'
        ]

        self.operations_use_immediate_constant_kk = [
            'ADD',
            'ADDCY',
            'AND',
            'COMPARE',
            'LOAD',
            'OR',
            'SUB',
            'SUBCY',
            'TEST',
            'XOR'
        ]

        self.operations_use_absolute_instruction_address = [
            'CALL',
            'JUMP'
        ]
        self.operations_use_port_address = [
            'INPUT',
            'OUTPUT'
        ]
        self.operations_use_scratchpad_ram_address = [
            'FETCH',
            'STORE'
        ]

    def decode(self, instruction):
        # operatioself.decode_operation(instruction[12:18])
        pass

    def decode_operation(self, code_operation):
        operation = {
            '01100': 'ADD',
            '01101': 'ADDCY',
            '00101': 'AND',
            '11000': 'CALL',
            '01010': 'COMPARE',
            '11110': 'INTERRUPT',
            '00011': 'FETCH',
            '00010': 'INPUT',
            '11010': 'JUMP',
            '00000': 'LOAD',
            '00110': 'OR',
            '10110': 'OUTPUT',
            '10101': 'RETURN',
            '11100': 'RETURNI',
            '10000': 'SHIFT',
            '10111': 'STORE',
            '01110': 'SUB',
            '01111': 'SUBCY',
            '01001': 'TEST',
            '00111': 'XOR'
        }
        return operation[code_operation]

    def is_operation_use_register_sy(self, operation):
        if operation in self.operations_use_register_sy:
            return True
        else:
            return False

    def use_register_sy(self, operation):
        pass

    def is_operation_use_immediate_constant_kk(self, operation):
        if operation in self.operations_use_immediate_constant_kk:
            return True
        else:
            return False

    def is_operation_use_register_sx(self, operation):
        if operation in self.operations_use_register_sx:
            return True
        else:
            return False

    def is_operation_use_absolute_instruction_address(self, operation):
        if operation in self.operations_use_absolute_instruction_address:
            return True
        else:
            return False

    def is_operation_use_port_address(self, operation):
        if operation in self.operations_use_port_address:
            return True
        else:
            return False

    def is_operation_scratchpad_ram_address(self, operation):
        if operation in self.operations_use_scratchpad_ram_address:
            return True
        else:
            return False

    def calculate_value(self, value):
        return int(value)


# dec = Decoder()
# print dec.decode_operation('11000')
# print dec.is_operation_use_register_sx(dec.decode_operation('11000'))
