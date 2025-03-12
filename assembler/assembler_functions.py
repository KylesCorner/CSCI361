
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

# TODO: add mirror entries, and rest of default symbols
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

    '': '000',  # Empty instruction

    'M': '001',  # Dest instructions
    'D': '010',
    'DM': '011',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'MA': '101',
    'AD': '110',
    'DA': '110',
    'ADM': '111',
    'AMD': '111',
    'MDA': '111',
    'DAM': '111',
    'DMA': '111',
    'MAD': '111',

    'JGT': '001',  # Jump instructions
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
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
    if (len(sys.argv) < 2):
        print("Please enter a file path.")

    if (len(sys.argv) > 2):
        for setting in sys.argv[2:]:
            if setting not in settings:
                print(f"{setting} not a correct argument")
            else:
                settings[setting] = True

    file_path = sys.argv[1]

    lines = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if ((line.strip() != '') and ('//') not in line):
                    lines.append(line.strip())

    except FileNotFoundError:
        print(f"Error file not found: {file_path}")

    return lines


def save_program(binaryString):
    file_path = 'prog.hack'

    with open(file_path, 'w+') as file:
        file.write(binaryString + '\n')
    return


def convert_to_binary(number):
    binary_str = bin(number)[2:]
    binary_16_bit = binary_str.zfill(15)
    return binary_16_bit


def a_instruction(instruction, index, file, variableCounter):
    if (settings['-v'] or settings['-l']):
        print(
            f"--- From a_instruction(instruction={instruction},index={index},file={file}) ---")

    binaryString = '0'
    instruction = instruction[1:]

    number_pattern = r"^[0-9]+$"
    if (bool(re.match(number_pattern, instruction))):
        binaryString += convert_to_binary(int(instruction))
    else:
        if instruction not in symbolTable:
            # print(
            #     f"Error on line {index} => {file[index]}, {instruction} not found in symbol table.")
            symbolTable[instruction] = convert_to_binary(variableCounter)
            variableCounter += 1

        binaryString += symbolTable[instruction]

    if (settings['-l']):
        print(
            f"--- Length test of {binaryString} = {len(binaryString) == 16}  ---")

    return (binaryString + '\n', variableCounter)


def c_instruction(dest, comp, jump):
    if (settings['-v'] or settings['-l']):
        print(
            f"--- From c_instruction(dest={dest},comp={comp},jump={jump}) ---")

    if (settings['-v']):
        print(f"In symbol table: comp={compTable[comp]}")
        print(f"In symbol table: dest={symbolTable[dest]}")
        print(f"In symbol table: jump={symbolTable[jump]}")
        print(
            f"Building the strings: {compTable[comp]}-{symbolTable[dest]}-{symbolTable[jump]}")

    binaryString = '111' + compTable[comp] + \
        symbolTable[dest] + symbolTable[jump]

    if (settings['-l']):
        print(
            f"--- Length test of {binaryString} = {len(binaryString) == 16}  ---")

    if (len(binaryString) != 16):
        print(
            f"Error! Length of {binaryString} != 16; {len(binaryString)}. dest={dest}, comp={comp}, jump={jump}")

    return binaryString + '\n'


def instruction_decode(file_array):
    binaryString = ''
    variableCounter = 16
    for index, line in enumerate(file_array):
        hasDest = '=' in line
        hasJmp = ';' in line
        isAinst = '@' in line
        isLabel = ('(' or ')') in line
        isCinst = (not isAinst) and (not (isLabel))

        dest = ''
        comp = ''
        jump = ''

        instrArray = re.split(r"[=;]", line)

        if (hasDest and hasJmp):
            dest, comp, jump = instrArray
        elif (hasDest):
            dest, comp = instrArray
        elif (hasJmp):
            comp, jump = instrArray

        if (settings['-v']):
            print(f"Line number: {index}")
        if (isAinst):
            temp, variableCounter = a_instruction(
                line, index, file_array, variableCounter)
            binaryString += temp

        elif (isCinst):
            binaryString += c_instruction(dest, comp, jump)

        elif (isLabel):
            print(
                f"Error on line {index} => {file_array[index]}, {line} not found in symbol table.")

    return binaryString


def fill_symbol_table(file):
    indexToDelete = []
    for index, line in enumerate(file):
        isLabel = ("(" or ")") in line
        if (not isLabel):
            continue

        fixed_line = line.replace("(", "")
        fixed_line = fixed_line.replace(")", "")

        if fixed_line not in symbolTable:

            indexToDelete.append((index, fixed_line))

    for delta, (index, line) in enumerate(indexToDelete):
        symbolTable[line] = convert_to_binary(index-delta)
        del file[(index-delta)]


def main():
    binaryString = ''

    file_array = load_file()

    fill_symbol_table(file_array)

    binaryString += instruction_decode(file_array) + "\n"

    binaryString = binaryString.strip()

    if (settings['-v']):
        for item in symbolTable:
            print(f"{item} : {symbolTable[item]}")

    save_program(binaryString)


if __name__ == "__main__":
    main()
