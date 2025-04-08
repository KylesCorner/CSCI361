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
    return "@SP,AM=M-1,D=M"

def getPushD():
    return "@SP,A=M,M=D,@SP,M=M+1"

# The following dictionaries are used to translate VM language commands to machine language.

# This contains the binary operations add, sub, and, or as values. The keys are the Hack ML code to do them.
# Assume a getPopD() has been called prior to this lookup.
ARITH_BINARY = {
    "add": getPopD() + ",@SP,AM=M-1,M=M+D,,",
    "sub": getPopD() + ",@SP,AM=M-1,M=M-D,,",
    "and": getPopD() + ",@SP,AM=M-1,M=M&D,,",
    "or":  getPopD() + ",@SP,AM=M-1,M=M|D,,",
}

# As above, but now the keys are unary operations neg, not
# Values are sequences of Hack ML code, seperated by commas.
# In this case do not assume a getPopD() has been called prior to the lookup
ARITH_UNARY = {
    "neg": "@SP,AM=M-1,M=-M," + getPushD() + ",,",
    "not": "@SP,AM=M-1,M=!M," + getPushD() + ",,",
}

# Now, the code for operations gt, lt, eq as values. 
# These are assumed to be preceded by getPopD()
# The ML code corresponds very nicely to the jump conditions in 
# Hack assembly
ARITH_TEST  = {
    "eq": "JEQ",
    "lt": "JLT",
    "gt": "JGT",
}

# Base addresses for pointer-based segments
SEGLABEL = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT"
}


# This will be used to generate unique labels when they are needed.
LABEL_NUMBER = 0


POINTER_BASE = 3  # Base address for pointer segment
TEMP_BASE = 5  # Base address for temp segment


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
        print(f"Bad operation: {pushpop}")
        raise ValueError("Invalid operation. Use 'push' or 'pop'.")

    if not isinstance(index, int) or index < 0:
        print(f"Bad Index: {index}, {type(index)}")
        raise ValueError("Index must be a non-negative integer.")
    
    
    output_str = ""
    
    if seg in SEGLABEL:
        base_address = SEGLABEL[seg]
        if pushpop == "push":
            output_str = ",".join({
                f"@{index}",
                "D=A",
                f"@{base_address}",
                "A=D+M",
                "D=M",
                getPushD(),
            })

        elif pushpop == "pop":
            output_str = ",".join([
                f"@{index}",
                "D=A",
                f"@{base_address}",
                "D=D+M",
                "@R13",
                "M=D",
                getPopD(),
                "@R13",
                "A=M",
                "M=D",
            ])
    else:
        raise ValueError("Invalid segment. Supported segments: 'local', 'argument', 'this', 'that'")

    return output_str + ",,"

def fixedSeg(pushpop,seg,index):
    """
    For pointer and temp segments
    """

    if pushpop not in ["push", "pop"]:
        print(f"Invalid operation: {pushpop}. Type: {type(pushpop)}")
        raise ValueError("Invalid push/pop operation")

    base = POINTER_BASE if seg == "pointer" else TEMP_BASE
    addr = f"@{base - index}"
    output_str = ""


    if pushpop == "push":
        output_str = ",".join({
            addr,
            "D=M",
            getPushD(),
        })
    else:
        output_str = ",".join([
            getPopD(),
            addr,
            "M=D",
        ])

    
    return output_str + ",,"


def constantSeg(pushpop,seg,index):
    """
    This will do constant and static segments
    """
    output_str = ""

    if seg == "constant":
        output_str = ",".join([
            f"@{index}",
            "D=A",
            getPushD(),
        ])

    elif seg == "static":

        var = f"@Static.{index}"

        if pushpop == "push":
            output_str = ",".join([
                var,
                "D=M",
                getPushD(),
            ])

        else:
            output_str = ",".join([
                getPopD(),
                var,
                "M=D",
            ])

    return output_str + ",,"

def line2Command(line):
    """ This just returns a cleaned up line, removing unneeded spaces and comments"""
    line = line.split("//")[0].strip()
    return line if line else None
    
          

def uniqueLabel():
    """ Uses LABEL_NUMBER to generate and return a unique label"""
    global LABEL_NUMBER
    LABEL_NUMBER += 1
    return f"LABEL{LABEL_NUMBER}"

def ParseFile(f):
    outString = ""
    for line in f:
        command = line2Command(line)
        if command:
            args = [x.strip() for x in command.split()] # Break command into list of arguments, no return characters
            
            cmd = args[0]
            if cmd in ARITH_BINARY.keys():
                """
                Code that will deal with any of the binary operations (add, sub, and, or)
                do so by doing the things all have in common, then do what is specific
                to each by pulling a key from the appropriate dictionary.
                Remember, it's always about putting together strings of Hack ML code.
                """
                outString += f"//{cmd},"
                outString += ARITH_BINARY[cmd]

            elif cmd in ARITH_UNARY.keys():
                """
                As above, but now for the unary operators (neg, not)
                """
                outString += f"//{cmd},"
                outString += ARITH_UNARY[cmd]

            elif cmd in ARITH_TEST.keys():
                """
                Deals with the three simple operators (lt,gt,eq), but likely the hardest
                section because you'll have to write assembly to jump to a different part
                of the code, depending on the result.
                To define where to jump to, use the uniqueLabel() function to get labels.
                The result should be true (0xFFFF) or false (0x0000) depending on the test.
                That goes back onto the stack.
                HINT: Review the quiz for this unit!
                """
                jump = ARITH_TEST[cmd]
                label_true = uniqueLabel()
                label_end = uniqueLabel()
                outString += f"// {cmd},"
                outString += ",".join([
                    getPopD(),
                    "@SP",
                    "AM=M-1",
                    "D=M-D",
                    f"@{label_true}",
                    f"D;{jump}",
                    f"@{label_end}",
                    "0;JMP",
                    f"({label_true})",
                    "@SP",
                    "A=M",
                    "M=-1",
                    "@SP",
                    "M=M+1",
                    f"({label_end})",
                    ","
                ])

            elif args[1] in SEGMENTS.keys():
                """
                Here we deal with code that's like push/pop segment index.
                You've written the functions, the code in here selects the right 
                function by picking a function handle from a dictionary. 
                """
                pushpop, seg, index = args[0:3]
                outString += f"// {pushpop} {seg} {index},"
                outString += SEGMENTS[seg](pushpop,seg,int(index))

            else:
                print("Unknown command!")
                print(cmd)
                sys.exit(-1)

    l = uniqueLabel()
    outString += "// Final endless loop,"
    outString += '(%s)'%(l)+',@%s,0;JMP'%l # Final endless loop
    return outString.replace(',','\n')

# Mapping segment names to handling functions
SEGMENTS = {
    "local": pointerSeg,
    "argument": pointerSeg,
    "this": pointerSeg,
    "that": pointerSeg,
    "pointer": fixedSeg,
    "temp": fixedSeg,
    "constant": constantSeg,
    "static": constantSeg,
}

def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            hack = ParseFile(f)

        hack += "\n"
        write_file = open("prog.asm", "w")
        write_file.write(hack)
        write_file.close()
    else:
        print("Usage: python3 vm_translator.py filename.vm")



if __name__ == "__main__":
    main()
