#!/usr/bin/python3
def magic_calculation(a, b):
    def print_bytecode():
        bytecode = """
            3           0 LOAD_CONST               1 (98)
                        3 LOAD_FAST                0 (a)
                        6 LOAD_FAST                1 (b)
                        9 BINARY_POWER
                       10 BINARY_ADD
                       11 RETURN_VALUE
        """
        print(bytecode)
    
    # Call the print_bytecode function
    print_bytecode()

# Call the magic_calculation function with some values
magic_calculation(2, 3)
