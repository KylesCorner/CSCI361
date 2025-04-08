// vm_code/SimpleAdd.vm
// push constant 7
@7 // load constant value
D=A // Put 7 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// push constant 8
@8 // load constant value
D=A // Put 8 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// add
@SP // Pop to D
AM=M-1
D=M
A=A-1
M=D+M

// Final endless loop
(LOOP0)
@LOOP0
0;JMP
