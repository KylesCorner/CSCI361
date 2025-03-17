
"""
Kyle Krstulich
3/7/25
assembler_functions.py

"""
import re
import sys

settings = {
    '-v': False,  # Verbose output
    '-l': False,  # Verify each binary string length
}

symbolTable = {
    'R0': '000000000000000',
    'SP': '000000000000000',
    'R1': '000000000000001',
    'LCL': '000000000000001',
    'R2': '000000000000010',
    'ARG': '000000000000010',
    'R3': '000000000000011',
    'THIS': '000000000000011',
    'R4': '000000000000100',
    'THAT': '000000000000100',
    'R5': '000000000000101',
    'R6': '000000000000110',
    'R7': '000000000000111',
    'R8': '000000000001000',
    'R9': '000000000001001',
    'R10': '000000000001010',
    'R11': '000000000001011',
    'R12': '000000000001100',
    'R13': '000000000001101',
    'R14': '000000000001110',
    'R15': '000000000001111',
    'SCREEN': '100000000000000',
    'KBD': '110000000000000',
}

jump_table = {
    '': '000',  # Empty instruction
    'JGT': '001',  # Jump instructions
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}
dest_table = {
    '': '000',  # Empty instruction
    'M': '001',  # Dest instructions
    'D': '010',
    'DM': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'ADM': '111',
}
compTable = {

    '0': '0101010',  # Comp Instructions
    '1': '0111111',
    '-1': '0111010',
    'D': '0001100',
    'A': '0110000',
    'M': '1110000',
    '!D': '0001101',
    '!A': '0110001',
    '!M': '1110001',
    '-D': '0001111',
    '-A': '0110011',
    '-M': '1110011',
    'D+1': '0011111',
    '1+D': '0011111',
    'A+1': '0110111',
    '1+A': '0110111',
    'M+1': '1110111',
    '1+M': '1110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'M-1': '1110010',
    'D+A': '0000010',
    'A+D': '0000010',
    'D+M': '1000010',
    'M+D': '1000010',
    'D-A': '0010011',
    'D-M': '1010011',
    'A-D': '0000111',
    'M-D': '1000111',
    'D&A': '0000000',
    'A&D': '0000000',
    'D&M': '1000000',
    'M&D': '1000000',
    'D|A': '0010101',
    'A|D': '0010101',
    'D|M': '1010101',
    'M|D': '1010101',
}


def load_file():
    """
    Loads an assembly source file, processes it by removing empty lines and comments, 
    and returns the cleaned lines as a list.

    If additional arguments are provided, it checks them against predefined settings 
    and updates the settings dictionary if they are valid.

    Returns:
        list: A list of cleaned lines from the file, excluding comments and empty lines.
    """
    if len(sys.argv) < 2:
        print("Please enter a file path.")

    # Process additional arguments if provided
    if len(sys.argv) > 2:
        for setting in sys.argv[2:]:
            if setting not in settings:
                print(f"{setting} not a correct argument")
            else:
                settings[setting] = True  # Update valid settings

    file_path = sys.argv[1]  # Get the file path from command-line arguments

    lines = []

    try:
        # Open the file and read its lines
        with open(file_path, 'r') as file:
            for line in file:
                # Strip whitespace and ignore empty lines and comments
                if line.strip() != '' and '//' not in line:
                    lines.append(line.strip())

    except FileNotFoundError:
        print(f"Error file not found: {file_path}")

    return lines


def save_program(binaryString):
    """
    Saves the given binary string representation of the assembled program to a file.

    The output file is named 'prog.hack' and will be overwritten if it already exists.

    Args:
        binary_string (str): The binary representation of the assembled program.

    Returns:
        None
    """
    file_path = 'prog.hack'  # Output file name

    with open(file_path, 'w+') as file:
        file.write(binaryString + '\n')  # write the binary string to the file


def convert_to_binary(number):
    """
    Converts a given integer to a 15-bit binary string with leading zeros.

    Args:
        number (int): The integer to convert to binary.

    Returns:
        str: A 15-bit binary string representation of the number.
    """

    # converts number to binary and string removing '0b'
    binary_str = bin(number)[2:]

    # pad with leading zeros to ensure 15 bit length
    binary_15_bit = binary_str.zfill(15)
    return binary_15_bit


def a_instruction(instruction, index, variable_counter):
    """
    Processes an A-instruction from assembly and converts it into a 16-bit binary string.

    If the instruction is a numeric constant, it is directly converted to binary. 
    If it is a variable or label, it is stored in the symbol table with an assigned address.

    Args:
        instruction (str): The A-instruction (e.g., "@value").
        index (int): The line number of the instruction in the source file.
        variable_counter (int): The next available memory address for new variables.

    Returns:
        tuple: A tuple containing:
            - str: The 16-bit binary representation of the instruction.
            - int: The updated variable counter.
    """

    # Debug flags
    if (settings['-v'] or settings['-l']):
        print(
            f"--- From a_instruction(instruction={instruction},index={index} ---")

    binaryString = '0'  # A-instructions start with 0
    instruction = instruction[1:]  # remove '@' prefix

    number_pattern = r"^[0-9]+$"
    if (re.match(number_pattern, instruction)):  # if instruction is a number
        binaryString += convert_to_binary(int(instruction))
    else:
        if instruction not in symbolTable:
            symbolTable[instruction] = convert_to_binary(variable_counter)
            variable_counter += 1

        binaryString += symbolTable[instruction]

    if (settings['-l']):
        print(
            f"--- Length test of {binaryString} = {len(binaryString) == 16}  ---")

    return (binaryString + '\n', variable_counter)


def c_instruction(dest, comp, jump):
    """
    Converts a C-instruction into its 16-bit binary representation.

    A C-instruction consists of a computation (`comp`), an optional destination (`dest`), 
    and an optional jump condition (`jump`). It is assembled into the format:

        111 | comp bits | dest bits | jump bits

    Args:
        dest (str): The destination mnemonic (e.g., "D", "M", "A" or empty).
        comp (str): The computation mnemonic (e.g., "D+A", "M-1").
        jump (str): The jump mnemonic (e.g., "JGT", "JEQ", or empty).

    Returns:
        str: The 16-bit binary representation of the C-instruction.
    """

    # Debug flags
    if (settings['-v'] or settings['-l']):
        print(
            f"--- From c_instruction(dest={dest},comp={comp},jump={jump}) ---")
    if (settings['-v']):
        print(f"In symbol table: comp={compTable[comp]}")
        print(f"In symbol table: dest={dest_table[dest]}")
        print(f"In symbol table: jump={jump_table[jump]}")
        print(
            f"Building the strings: {compTable[comp]}-{dest_table[dest]}-{jump_table[jump]}")

    # Construct binary instruction
    binaryString = '111' + compTable[comp] + \
        dest_table[dest] + jump_table[jump]

    # More debug flags
    if (settings['-l']):
        print(
            f"--- Length test of {binaryString} = {len(binaryString) == 16}  ---")

    if (len(binaryString) != 16):
        print(
            f"Error! Length of {binaryString} != 16; {len(binaryString)}. dest={dest}, comp={comp}, jump={jump}")
        exit()

    return binaryString + '\n'


def instruction_decode(file_array):
    """
    Decodes a list of assembly instructions and converts them into binary machine code.

    This function processes both A-instructions and C-instructions, distinguishing between 
    them based on their format. It also handles variable assignment for A-instructions.

    Args:
        file_array (list of str): List of assembly instructions, each as a string.

    Returns:
        str: A concatenated binary representation of the entire program.
    """

    binaryString = ''
    variableCounter = 16  # Starting memory address for variables

    for index, line in enumerate(file_array):

        # Label was skipped on first pass
        is_label = line.startswith('(') and line.endswith(')')
        if (is_label):
            print(
                f"Error on line {index} => {file_array[index]}, {line} not found in symbol table.")
            exit()

        # Process A-instruction if necessary
        isAinst = '@' in line
        if (isAinst):
            temp, variableCounter = a_instruction(
                line, index, variableCounter)
            binaryString += temp
        hasDest = '=' in line
        hasJmp = ';' in line

        # C-instruction
        # Default values
        dest = ''
        comp = ''
        jump = ''

        # Split the instruction into its components based on '=' (dest) or ';' (jump)
        instrArray = re.split(r"[=;]", line)
        if (hasDest and hasJmp):
            dest, comp, jump = instrArray
        elif (hasDest):
            dest, comp = instrArray
        elif (hasJmp):
            comp, jump = instrArray

        # Process C-instruction if necessary
        isCinst = comp in compTable
        if (isCinst):

            # Sort dest to save memory space
            dest = "".join(sorted(dest))

            # Invalid jump
            if (jump not in jump_table):
                print(
                    f"Error on line {index} => {file_array[index]}, {line} : {jump} not found in jump table.")
                exit()

            # Invalid dest
            if (dest not in dest_table):
                print(
                    f"Error on line {index} => {file_array[index]}, {line} : {dest} not found in dest table.")
                exit()

            binaryString += c_instruction(dest, comp, jump)

        # Invalid instruction
        if ((not isAinst) and (not isCinst)):
            print(
                f"Error on line {index} => {file_array[index]}, {line} is an invalid instruction.")
            exit()
        if (isAinst and isCinst):
            print(
                f"Error on line {index} => {file_array[index]}, {line} is an invalid instruction.")
            exit()

        # Debug flags
        if (settings['-v']):
            print(f"Line number: {index}")

    return binaryString + "\n"


def fill_symbol_table(file):
    """
    Processes labels in the assembly file and fills the symbol table with their corresponding addresses.

    This function scans the file for label declarations (enclosed in parentheses, e.g., "(LOOP)"),
    assigns them memory addresses, and removes them from the instruction list.

    Args:
        file (list of str): The list of assembly instructions.

    Modifies:
        symbolTable (dict): Adds label names as keys and their corresponding binary addresses as values.
        file (list of str): Removes label declarations from the instruction list.
    """

    indexToDelete = []

    for index, line in enumerate(file):
        # Label check
        is_label = line.startswith('(') and line.endswith(')')

        if not is_label:
            continue

        # Extract label name
        fixed_line = line.replace("(", "").replace(")", "")

        # Add to symbol table if not already
        if fixed_line not in symbolTable:
            indexToDelete.append((index, fixed_line))

    # Remove labels from file and update symbol table with adjusted addresses
    for delta, (index, line) in enumerate(indexToDelete):
        symbolTable[line] = convert_to_binary(index-delta)
        del file[(index-delta)]


def main():
    binaryString = ''

    file_array = load_file()

    fill_symbol_table(file_array)

    binaryString = instruction_decode(file_array)

    binaryString = binaryString.strip()

    if (settings['-v']):
        for item in symbolTable:
            print(f"{item} : {symbolTable[item]}")

    save_program(binaryString)


if __name__ == "__main__":
    main()
