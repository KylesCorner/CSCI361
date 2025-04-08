// vm_code/StaticTest.vm
// push constant 111
@111 // load constant value
D=A // Put 111 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 333
@333 // load constant value
D=A // Put 333 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 888
@888 // load constant value
D=A // Put 888 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// pop static 8
@SP // Pop to D
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@StaticTest.8 // load variable location
M=D // *variable = D

// pop static 3
@SP // Pop to D
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@StaticTest.3 // load variable location
M=D // *variable = D

// pop static 1
@SP // Pop to D
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@StaticTest.1 // load variable location
M=D // *variable = D

// push static 3
@StaticTest.3 // load variable
D=M // D = *variable
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push static 1
@StaticTest.1 // load variable
D=M // D = *variable
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

// push static 8
@StaticTest.8 // load variable
D=M // D = *variable
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
