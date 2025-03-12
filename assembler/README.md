# Assembler Functions

This repository contains a Python implementation of a basic assembler for
converting assembly code into binary machine code, specifically for a
hypothetical machine similar to the Hack computer architecture used in the book
*The Elements of Computing Systems* by Nisan and Schocken.

## Features

- **Symbol Table**: The assembler uses a symbol table for handling variables, labels, and predefined symbols.
- **A-Instructions**: Supports A-instructions (e.g., `@value`), converting numeric constants or labels to 16-bit binary machine code.
- **C-Instructions**: Supports C-instructions (e.g., `D=A+1;JGT`), converting computations, destinations, and jumps to their binary representations.
- **Label Handling**: Processes labels (e.g., `(LOOP)`) and assigns them memory addresses, removing them from the final instructions.
- **Verbose Output**: Displays detailed debug information when the `-v` flag is set.
- **Length Verification**: Verifies that each binary instruction is exactly 16 bits long when the `-l` flag is set.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the `assembler_functions.py` file.
2. Create a source assembly file (e.g., `program.asm`) with the assembly code to be assembled.
3. Run the assembler script from the command line with the following command:

    ```bash
    python assembler_functions.py [assembly_file] [-v] [-l]
    ```

   - `assembly_file`: The path to the assembly source file (e.g., `program.asm`).
   - `-v`: (Optional) Enables verbose output for debugging.
   - `-l`: (Optional) Verifies that each binary string instruction is 16 bits long.

### Example
```{bash}
python3 assembler_functions.py program.asm
```

It will make a file `prog.hack` in the same directory as the python file.

```{bash}
./test.sh
```

This is a linux bash shell script that runs each program in the `/programs`
directory. Checking the binary output to the corresponding file in
`/difftables`.

