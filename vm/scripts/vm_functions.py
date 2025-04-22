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

    SimpleFunction Passed!
    NestedCall Passed!
"""

import sys
from pathlib import Path

# ------------------------------------------------------------------------------------------- 
#   Helper Functions
# ------------------------------------------------------------------------------------------- 

def getPopD():
    return f"@SP,AM=M-1,D=M"

def getPushD():
    return f"@SP,A=M,M=D,@SP,M=M+1"

def _getPushMem(source):
    """ Helper function to push memory to location src to stack """
    return ",".join([
        f"@{source}",
        "D=M",
        getPushD(),
        ","
    ])

def _getPushLabel(source):
    """ Helper function to push the ROM address of a label to the stack. """
    return ",".join([
        f"@{source}",
        "D=A",
        getPushD(),
        ","
    ])

def _getRestore(destination):
    return ",".join([
        "@R13",
        "AM=M-1",
        "D=M",
        f"@{destination}",
        "M=D",
        ","
    ])
def _getPopMem(destination):
    """ Helper function to pop the stack to the memory address dest. """
    return ",".join([
        getPopD(),
        f"@{destination}",
        "A=M",
        "M=D",
        ","
    ])


def _getMoveMem(source, destination):
    """ Helper function to move the contents of src to memory location dest. """
    return ",".join([
        f"@{source}",
        "D=M",
        f"@{destination}",
        "M=D",
    ])

def line2Command(line):
    """ This just returns a cleaned up line, removing unneeded spaces and comments"""
    line = line.split("//")[0].strip()
    return line if line else None
    
          

def uniqueLabel(id):
    """ Uses LABEL_NUMBER to generate and return a unique label"""
    global LABEL_NUMBER
    label = f"{id.upper()}{LABEL_NUMBER}"
    LABEL_NUMBER += 1
    return label

# ------------------------------------------------------------------------------------------- 
#   Arithmetic Dictionaries
# ------------------------------------------------------------------------------------------- 

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

# ------------------------------------------------------------------------------------------- 
#   Constant and Global variables
# ------------------------------------------------------------------------------------------- 

FILENAME = "" # Name of .vm file
POINTER_BASE = 3  # Base address for pointer segment
TEMP_BASE = 5  # Base address for temp segment
LABEL_NUMBER = 0

# ------------------------------------------------------------------------------------------- 
#   Memory Segment Operations
# ------------------------------------------------------------------------------------------- 

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
        # output_str = ",".join([
        #     f"@{index}",
        #     f"D=A",
        #     f"@{base_address}",
        #     "A=M",
        #     f"A=D+A",
        #     "D=M",
        #     getPushD()
        # ])
        output_str = ",".join([
            f"@{base_address}",
            "D=M",
            f"@{index}",
            f"A=D+A",
            "D=M",
            getPushD()
        ])


    else:
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
            addr,
            "D=M",
            getPushD(),
        ])
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
            f"D=A",
            getPushD(),
        ])

    else:

        var = f"@{FILENAME}.{index}"

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
                "M=D"
            ])

    return output_str + ",,"

# ------------------------------------------------------------------------------------------- 
#   Keyword Functions
# ------------------------------------------------------------------------------------------- 

def getIf_goto(label):
    """
    Returns Hack ML to goto the label specified as
    an input arguement if the top entry of the stack is
    true.
    """
    return "\n".join([
    getPopD(),
    f"@{label}",  # Load the destination label
    "D;JNE", # Jump if D != 0 (i.e., if the value was true)
    ","
    ])

def getGoto(label):
    """
    Return Hack ML string that will unconditionally
    jumpt to the input label.
    """
    return f"@{label},0;JMP,,"

def getLabel(label):
    """
    Returns Hack ML for a label, eg (label)
    """
    return f"({label}),"
def getCall(function,nargs):
    """
    This function returns the Hack ML code to
    invoke the `call function nargs` type command in
    the Hack virtual machine (VM) language.
    In order for this to work, review slides
    46-58 in the Project 8 presentation available
    on the nand2tetris.org website.
    """
    outString = f"// call {function} {nargs},"
    l = uniqueLabel("Call_Label")
    segs = ["LCL", "ARG", "THIS", "THAT"]

    outString += _getPushLabel(l)

    for item in segs:
        outString += _getPushMem(item)

    outString += ",".join([
        "// ARG = SP - nArgs - 5",
        "@SP",
        "D=M",
        f"@{int(nargs) + 5}",
        "D=D-A",
        "@ARG",
        "M=D",
        ","
    ])

    outString += ",".join([
        "// LCL = SP",
        _getMoveMem("SP", "LCL"),
        ",// goto Fn",
        f"@{function}",
        "0;JMP",
        "// (return address)",
        f"({l})",
        ","
    ])



    return outString
def getFunction(function,nlocal):
    """
    Return the Hack ML code to represent a function which sets a label
    and initializes local variables to zero.
    See slides 59-63 in the nand2tetris book.
    """
    output_string = f"// function {function} {nlocal},"
    output_string += f"({function}),"

    for i in range(int(nlocal)):
        output_string += ",".join([
            SEGMENTS["constant"]("push","constant",0),
        ])

    return output_string

def getReturn():
    """
    Returns Hack ML code to perform a return, one
    of the more complex operations in this unit.
    The code restores all the memory segments to the
    calling function. It also has to restore the
    instruction pointer (IP) and reset the stack
    pointer. See slides 64-76 of nand2tetris.org
    project 8.
    """
    output_string = "// return,"

    output_string += "// FRAME = LCL,"
    output_string += _getMoveMem("LCL","R13")

    output_string += "// RET = *(FRAME - 5),"
    output_string += ",".join([
        "@5",
        "A=D-A",
        "D=M",
        "@R14   // R!$ =RET",
        "M=D",
        ","
    ])

    output_string += "// *ARG = pop(),"
    output_string += _getPopMem("ARG")

    output_string += "// SP = ARG + 1,"
    output_string += ",".join([
        "@ARG",
        "D=M+1",
        "@SP",
        "M=D",
        ","
    ])

    to_restore = ["THAT", "THIS", "ARG", "LCL"]
    for index, item in enumerate(to_restore):
        output_string += f"// Restore {item} = *(FRAME - {index + 1}),"
        output_string += _getRestore(item)

    output_string += "// goto RET,"
    output_string += ",".join([
        "@R14",
        "A=M",
        "0;JMP",
        ",",
    ])

    return output_string
# ------------------------------------------------------------------------------------------- 
#   Function Pointer Dictionaries
# ------------------------------------------------------------------------------------------- 

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
# More jank, this time to define the function pointers for flow control.
PROG_FLOW = {
    'if-goto':getIf_goto, # 1
    'goto':getGoto, # 1
    'label':getLabel, # 1
    'call':getCall, # 2
    'function':getFunction, # 2
    'return':getReturn, # 0
}

def ParseFile(f):
    outString = f"// {sys.argv[1]},"
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
                label_true = uniqueLabel("true")
                label_false = uniqueLabel("false")
                outString += f"// {cmd},"
                outString += ",".join([
                    getPopD(),
                    "@SP",        # Pop x
                    "AM=M-1",
                    "D=M-D",      # D = x - y
                    f"@{label_true}",
                    f"D;{jump}",  # Jump to true label if condition met
                    "@SP",
                    "A=M",
                    "M=0",        # false = 0
                    f"@{label_false}",
                    "0;JMP",
                    f"({label_true})",
                    "@SP",
                    "A=M",
                    "M=-1",       # true = -1 (0xFFFF)
                    f"({label_false})",
                    "@SP",
                    "M=M+1",      # push result, SP++
                    ","
                ])

            elif args[0] in PROG_FLOW.keys():
                """
                Handles project 8 keywords:
                function,
                return,
                call,
                goto,
                if-goto,
                label
                """

                # TODO: Proper Error handling

                num_params = len(args)

                if num_params == 1:
                    # return
                    outString += PROG_FLOW[args[0]]()

                elif num_params == 2:
                    # if-goto, goto, and label
                    cmd, label = args[0:2]
                    outString += PROG_FLOW[cmd](label)

                elif num_params == 3:
                    #call and function
                    cmd, fn, n = args[0:3]
                    outString += PROG_FLOW[cmd](fn, n)

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


    l = uniqueLabel("loop")
    outString += "// Final endless loop,"
    outString += '(%s)'%(l)+',@%s,0;JMP'%l # Final endless loop
    return outString.replace(',','\n')

def run():
    global FILENAME
    if len(sys.argv) == 3:
        with open(sys.argv[1], 'r') as f:
            FILENAME = Path(sys.argv[1]).stem

            hack = ParseFile(f)

        hack += "\n"
        write_file = open(sys.argv[2], "w")
        write_file.write(hack)
        write_file.close()
    else:
        print("Usage: python3 vm_translator.py filename.vm output.asm")


def main():
    run()



if __name__ == "__main__":
    main()
