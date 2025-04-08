// vm_code/SimpleAdd.vm
// push constant 7
@7 // load constant value
D=A // Put 7 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 8
@8 // load constant value
D=A // Put 8 into D
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
