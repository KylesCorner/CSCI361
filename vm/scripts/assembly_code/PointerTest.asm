// vm_code/PointerTest.vm
// push constant 3030
@3030 // load constant value
D=A // Put 3030 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// pop pointer 0
@SP // Pop to D
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@3 // load pointer address
M=D // *address = D

// push constant 3040
@3040 // load constant value
D=A // Put 3040 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// pop pointer 1
@SP // Pop to D
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@4 // load pointer address
M=D // *address = D

// push constant 32
@32 // load constant value
D=A // Put 32 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// pop this 2
@2 // load the index
D=A // D = index
@THIS // load base address of the segment
D=D+M // D = target address
@R13 // temp storage
M=D // R13 = address to store popped value
@SP // Pop to D
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@R13 // load temp storage
A=M // A = target address
M=D // *segment[index] = popped value

// push constant 46
@46 // load constant value
D=A // Put 46 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// pop that 6
@6 // load the index
D=A // D = index
@THAT // load base address of the segment
D=D+M // D = target address
@R13 // temp storage
M=D // R13 = address to store popped value
@SP // Pop to D
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@R13 // load temp storage
A=M // A = target address
M=D // *segment[index] = popped value

// push pointer 0
@3 // load pointer address
D=M // D = *address
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push pointer 1
@4 // load pointer address
D=M // D = *address
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// add
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
A=A-1 // address X
M=D+M // X = Y + X

// push this 2
@2 // load the index
D=A // D = index
@THIS // load the base address of the segment
A=M // get base pointer
A=D+A // final target address
D=M // D = value at target address
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// sub
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
A=A-1 // address X
M=M-D // X = X - Y

// push that 6
@6 // load the index
D=A // D = index
@THAT // load the base address of the segment
A=M // get base pointer
A=D+A // final target address
D=M // D = value at target address
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// add
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
A=A-1 // address X
M=D+M // X = Y + X

// Final endless loop
(LOOP0)
@LOOP0
0;JMP
