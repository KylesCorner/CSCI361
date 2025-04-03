"""
Kyle Krstulich
4/1/24
vm_functions.py

Virtual machine functions for the nand to tetris project.

Project 6 Assignment details:

    Write functions that take no arguments and return strings of Hack machine language to achieve a
    pop of the stack to the D register and a push of the D register onto the stack. Assume a symbol
    "SP" which is the memory address of the stack pointer exists. Call these functions 'getPushD()'
    and 'getPopD()' respectively. Don't forget to keep the position of the stack pointer up-to-date
    after the push or pop is done.

    Instead of placing new line characters in your strings, just use commas (,) to separate the
    lines.

Project 7 Assignment details:

    To accomplish our objectives, we will work with three different types of segments for VM
    language constructs like:

    push SEGMENT INDEX or,

    pop SEGMENT INDEX if SEGMENT is 'local', 'argument', 'this', or 'that':

    those are pointers, meaning the RAM address associated with them in the symbol table contains a
    RAM address where the SEGMENT begins. INDEX specifies where to go in the SEGMENT.

    if SEGMENT is 'constant' or 'static':

    Then something special occurs, in this case it is more akin to direct manipulation of the value
    in INDEX onto or off of the stack.

    if SEGMENT is 'pointer' or 'temp':

    Here, the values in the memory address specified by the segment are defined, 3 and 5
    respectively and not indirectly specified pointers.

    So, for each of the above there is a different function. For our next class, do the first set of
    segments for local, argument, this, and that. The function follows. Implement it.

    def pointerSeg(pushpop,seg,index):
        This function returns Hack ML code to push a memory location to 
        to the stack, or pop the stack to a memory location. 

        INPUTS:
            pushpop = a text string 'pop' means pop to memory location, 'push' 
                      is push memory location onto stack
            seg     = the name of the segment that will be be the base address
                      in the form of a text string
            index   = an integer that specifies the offset from the base 
                      address specified by seg

        RETURN: 
            The memory address is speficied by segment's pointer (SEGLABEL[seg]) + index (index))
            if pushpop is 'push', push the address contents to the stack
            if pushpop is 'pop' then pop the stack to the memory address.
            The string returned accomplishes this. ML commands are seperated by commas (,).

        NOTE: This function will only be called if the seg is one of:
        "local", "argument", "this", "that"
"""
def getPopD():
    return "@SP,AM=M-1,D=M,"

def getPushD():
    return "@SP,A=M,M=D,@SP,M=M+1",

def pointerSeg(pushpop, seg, index):
    """
    Generate Hack assembly code for push/pop operations on pointer-based segments.


    INPUTS:
        pushpop = a text string 'pop' means pop to memory location, 'push' 
                  is push memory location onto stack
        seg     = the name of the segment that will be be the base address
                  in the form of a text string
        index   = an integer that specifies the offset from the base 
                  address specified by seg

    RETURN: 
        The memory address is speficied by segment's pointer (SEGLABEL[seg]) + index (index))
        if pushpop is 'push', push the address contents to the stack
        if pushpop is 'pop' then pop the stack to the memory address.
        The string returned accomplishes this. ML commands are seperated by commas (,).

    NOTE: This function will only be called if the seg is one of:
    "local", "argument", "this", "that"

    """
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
