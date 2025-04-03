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

import sys

def getPopD():
    return "@SP,AM=M-1,D=M,"

def getPushD():
    return "@SP,A=M,M=D,@SP,M=M+1,"

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
    # Validate inputs
    if pushpop not in {"push", "pop"}:
        raise ValueError("Invalid operation. Use 'push' or 'pop'.")
    if not isinstance(index, int) or index < 0:
        raise ValueError("Index must be a non-negative integer.")
    
    # Base addresses for pointer-based segments
    SEGLABEL = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT"
    }
    
    POINTER_BASE = 3  # Base address for pointer segment
    TEMP_BASE = 5  # Base address for temp segment
    
    hack_code = []
    
    if seg in SEGLABEL:
        base_address = SEGLABEL[seg]
        if pushpop == "push":
            hack_code.extend([
                f"@{index}",
                "D=A",
                f"@{base_address}",
                "A=D+M",
                "D=M",
                getPushD()
            ])

        elif pushpop == "pop":
            hack_code.extend([
                f"@{index}",
                "D=A",
                f"@{base_address}",
                "D=D+M",
                "@R13",
                "M=D",
                getPopD(),
                "@R13",
                "A=M",
                "M=D"
            ])
    

    elif seg == "constant":
        if pushpop == "push":
            hack_code.extend([
                f"@{index}", "D=A",
                "@SP", "A=M", "M=D",
                "@SP", "M=M+1"
            ])
        else:
            raise ValueError("Cannot pop to constant segment.")

    # Need to have file name filename.index
    elif seg == "static":
        var_name = f"Static.{index}"
        if pushpop == "push":
            hack_code.extend([
                f"@{var_name}", "D=M",
                "@SP", "A=M", "M=D",
                "@SP", "M=M+1"
            ])
        elif pushpop == "pop":
            hack_code.extend([
                "@SP", "M=M-1", "A=M", "D=M",
                f"@{var_name}", "M=D"
            ])
    elif seg == "pointer":
        if index not in {0, 1}:
            raise ValueError("Pointer segment index must be 0 or 1.")
        address = POINTER_BASE + index
        if pushpop == "push":
            hack_code.extend([
                f"@{address}", "D=M",
                "@SP", "A=M", "M=D",
                "@SP", "M=M+1"
            ])
        elif pushpop == "pop":
            hack_code.extend([
                "@SP", "M=M-1", "A=M", "D=M",
                f"@{address}", "M=D"
            ])

    # location R5-R12
    elif seg == "temp":
        if index >= 8:
            raise ValueError("Temp segment index must be between 0 and 7.")
        address = TEMP_BASE + index
        if pushpop == "push":
            hack_code.extend([
                f"@{address}", "D=M",
                "@SP", "A=M", "M=D",
                "@SP", "M=M+1"
            ])
        elif pushpop == "pop":
            hack_code.extend([
                "@SP", "M=M-1", "A=M", "D=M",
                f"@{address}", "M=D"
            ])

    else:
        raise ValueError("Invalid segment. Supported segments: 'local', 'argument', 'this', 'that', 'constant', 'static', 'pointer', 'temp'.")

    return ",".join(hack_code)

def main():
    if len(sys.argv) == 4:
        op, seg, index = sys.argv[1:]
        print(op,seg,index)
        pointerseg_test = pointerSeg(op,seg,int(index))
    else:
        pointerseg_test = pointerSeg('push', 'temp', 1)


    popD_output = getPopD()
    pushD_output = getPushD()
    print(f"Pop: {type(popD_output)}\nPush: {type(pushD_output)}")
    print(pointerseg_test)

if __name__ == "__main__":
    main()
