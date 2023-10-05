import dis

def magic_calculation(a, b):
    # Load the constant 98
    result = 98
    
    # Calculate a ** b
    result = result + (a ** b)
    
    # Return the result
    return result

# Disassemble the bytecode to verify
dis.dis(magic_calculation)
