"""
Kyle Krstulich
4/1/24
vm_functions.py

Virtual machine functions for the nand to tetris project.

Files Tested:
    SimpleAdd Passed!
    BasicTest Passed!
    StackTest Passed!
    PointerTest Passed!
    StaticTest Passed!
"""

import sys
from pathlib import Path

def getPopD(comment = "Pop to D"):
    return f"@SP // {comment},AM=M-1,D=M"

def getPushD(comment = "Push D to stack"):
    return f"@SP // {comment},A=M,M=D,@SP,M=M+1"

# The following dictionaries are used to translate VM language commands to machine language.

# This contains the binary operations add, sub, and, or as values. The keys are the Hack ML code to do them.
# Assume a getPopD() has been called prior to this lookup.
ARITH_BINARY = {
    "add": getPopD() + ",A=A-1,M=D+M,,",
    "sub": getPopD() + ",A=A-1,M=M-D,,",
    "and": getPopD() + ",A=A-1,M=D&M,,",
    "or":  getPopD() + ",A=A-1,M=D|M,,",
}

# As above, but now the keys are unary operations neg, not
# Values are sequences of Hack ML code, seperated by commas.
# In this case do not assume a getPopD() has been called prior to the lookup
ARITH_UNARY = {
    "neg": "@SP,A=M-1,M=-M,,",
    "not": "@SP,A=M-1,M=!M,,",

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

FILENAME = "" # Name of .vm file
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
    output_str = ""
    
    base_address = SEGLABEL[seg]
    if pushpop == "push":
        output_str = ",".join([
            f"@{index} // load the index",
            f"D=A // D = index",
            f"@{base_address} // load the base address of the segment",
            "A=M // get base pointer",
            f"A=D+A // final target address",
            "D=M // D = value at target address",
            getPushD()
        ])

    else:
        output_str = ",".join([
            f"@{index} // load the index",
            "D=A // D = index",
            f"@{base_address} // load base address of the segment",
            "D=D+M // D = target address",
            "@R13 // temp storage",
            "M=D // R13 = address to store popped value",
            getPopD(),
            "@R13 // load temp storage",
            "A=M // A = target address",
            "M=D // *segment[index] = popped value",
        ])

    return output_str + ",,"

def fixedSeg(pushpop,seg,index):
    """
    For pointer and temp segments
    """
    base = POINTER_BASE if seg == "pointer" else TEMP_BASE
    addr = f"@{base + index}"
    output_str = ""

    if pushpop == "push":
        output_str = ",".join([
            addr + " // load pointer address",
            "D=M // D = *address",
            getPushD(),
        ])
    else:
        output_str = ",".join([
            getPopD(),
            addr + " // load pointer address",
            "M=D // *address = D",
        ])


    
    return output_str + ",,"


def constantSeg(pushpop,seg,index):
    """
    This will do constant and static segments
    """
    output_str = ""

    if seg == "constant":
        output_str = ",".join([
            f"@{index} // load constant value",
            f"D=A // Put {index} into D",
            getPushD(),
        ])

    else:

        var = f"@{FILENAME}.{index}"

        if pushpop == "push":
            output_str = ",".join([
                var + " // load variable",
                "D=M // D = *variable",
                getPushD(),
            ])

        else:
            output_str = ",".join([
                getPopD(),
                var + " // load variable location",
                "M=D // *variable = D"
            ])

    return output_str + ",,"

def line2Command(line):
    """ This just returns a cleaned up line, removing unneeded spaces and comments"""
    line = line.split("//")[0].strip()
    return line if line else None
    
          

def uniqueLabel(id, label_number):
    """ Uses LABEL_NUMBER to generate and return a unique label"""
    label = f"{id.upper()}{label_number}"
    return label

def ParseFile(f):
    outString = f"// {sys.argv[1]},"
    label_number = 0
    for line_number, line in enumerate(f):
        err = f"File {sys.argv[1]}: Line {line_number+1} -> "
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
                outString += f"// {cmd},"
                outString += ARITH_BINARY[cmd]

            elif cmd in ARITH_UNARY.keys():
                """
                As above, but now for the unary operators (neg, not)
                """
                outString += f"// {cmd},"
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
                label_true = uniqueLabel("true",label_number)
                label_false = uniqueLabel("false",label_number)
                label_number += 1
                outString += f"// {cmd},"
                outString += ",".join([
                    getPopD("Pop Y"),
                    "@SP // Pop x",        # Pop x
                    "AM=M-1",
                    "D=M-D // D = x - y",      # D = x - y
                    f"@{label_true}",
                    f"D;{jump} // Jump to {label_true} if condition met",  # Jump to true label if condition met
                    "@SP",
                    "A=M",
                    "M=0 // false = 0",        # false = 0
                    f"@{label_false}",
                    "0;JMP",
                    f"({label_true})",
                    "@SP",
                    "A=M",
                    "M=-1 // true = -1",       # true = -1 (0xFFFF)
                    f"({label_false})",
                    "@SP",
                    "M=M+1 // push result, SP++",      # push result, SP++
                    ","
                ])

            # invalid arithmetic operation
            elif len(args) < 3:
                err += f"Invalid operation; {', '.join(args)}."
                raise ValueError(err)

            elif args[1] in SEGMENTS.keys():
                """
                Here we deal with code that's like push/pop segment index.
                You've written the functions, the code in here selects the right 
                function by picking a function handle from a dictionary. 
                """
                pushpop, seg, index = args[0:3]

                # invalid push/pop
                if pushpop not in ["push", "pop"]:
                    err += f"Invalid operation, {pushpop}. Use 'push' or 'pop'"
                    raise ValueError(err)

                # invalid segment
                if seg not in SEGMENTS.keys():
                    err += f"Invalid segment, {seg} not in {SEGMENTS.keys()}"
                    raise ValueError(err)

                # invalid index
                if (int(index) < 0 ):
                    err += f"Invalid Index, {index} must be a positive integer"
                    raise ValueError(err)


                outString += f"// {pushpop} {seg} {index},"
                outString += SEGMENTS[seg](pushpop,seg,int(index))

            # invalid segment
            else:
                err += f"Invalid segment, {args[1]} not in {SEGMENTS.keys()}"
                raise ValueError(err)

    l = uniqueLabel("loop", label_number)
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
    global FILENAME
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            FILENAME = Path(sys.argv[1]).stem

            hack = ParseFile(f)

        hack += "\n"
        write_file = open("prog.asm", "w")
        write_file.write(hack)
        write_file.close()
    else:
        print("Usage: python3 vm_translator.py filename.vm")



if __name__ == "__main__":
    main()
