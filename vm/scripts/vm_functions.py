"""
Kyle Krstulich
4/1/24
vm_functions.py

Virtual machine functions for the nand to tetris project.

Assignment details:

    Write functions that take no arguments and return strings of Hack machine
    language to achieve a pop of the stack to the D register and a push of the D
    register onto the stack. Assume a symbol "SP" which is the memory address of the
    stack pointer exists. Call these functions 'getPushD()' and 'getPopD()'
    respectively. Don't forget to keep the position of the stack pointer up-to-date
    after the push or pop is done.

    Instead of placing new line characters in your strings, just use commas (,) to
    separate the lines.
"""
def getPopD():
    return "@SP,AM=M-1,D=M,"

def getPushD():
    return "@SP,A=M,M=D,@SP,M=M+1",

def pointerSeg(pushpop, seg, index):
    """Generate Hack assembly code for push/pop operations on pointer-based segments."""
    # Base addresses for segments in Hack assembly
    SEGLABEL = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT"
    }
    
    if seg not in SEGLABEL:
        raise ValueError("Invalid segment. This function only supports 'local', 'argument', 'this', and 'that'.")
    
    base_address = SEGLABEL[seg]
    hack_code = []
    
    if pushpop == "push":
        hack_code.extend([
            f"@{index}",  # Load index
            "D=A",        # Store index in D
            f"@{base_address}",  # Load base address
            "A=M",        # Get base address value
            "A=D+A",      # Compute target address
            "D=M",        # Get value at target address
            "@SP",        # Load stack pointer
            "A=M",        # Set address to stack top
            "M=D",        # Push value to stack
            "@SP",        # Load stack pointer
            "M=M+1"       # Increment stack pointer
        ])
    
    elif pushpop == "pop":
        hack_code.extend([
            f"@{index}",  # Load index
            "D=A",        # Store index in D
            f"@{base_address}",  # Load base address
            "A=M",        # Get base address value
            "D=D+A",      # Compute target address
            "@R13",       # Store address in R13 (temp variable)
            "M=D",
            "@SP",        # Load stack pointer
            "M=M-1",      # Decrement stack pointer
            "A=M",        # Set address to stack top
            "D=M",        # Get value from stack
            "@R13",       # Retrieve target address
            "A=M",
            "M=D"         # Store value at target address
        ])
    else:
        raise ValueError("Invalid operation. Use 'push' or 'pop'.")
    
    return ",".join(hack_code)

def main():
    popD_output = getPopD()
    pushD_output = getPushD()
    print(f"Pop: {popD_output}\nPush: {pushD_output}")
    pointerseg_test = pointerSeg('pop', 'local', 1)
    print(pointerseg_test)

if __name__ == "__main__":
    main()
