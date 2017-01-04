class Decoder:
    def decode_operation(self, code_operation):
        operation = {
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
        return operation[code_operation]
