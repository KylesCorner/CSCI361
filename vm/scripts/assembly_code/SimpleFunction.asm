// vm_code/SimpleFunction.vm
// SimpleFunction.test 2
(SimpleFunction.test)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// push local 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@LCL
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
AM=M-1
D=M
A=A-1
M=D+M

// not
@SP
A=M-1
M=!M

// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
AM=M-1
D=M
A=A-1
M=D+M

// push argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

// return
// FRAME = LCL
@LCL
D=M
@R13
M=D// RET = *(FRAME - 5)
@5
A=D-A
D=M
@R14   // R!$ =RET
M=D

// *ARG = pop()
@SP
AM=M-1
D=M
@ARG
A=M
M=D

// SP = ARG + 1
@ARG
D=M+1
@SP
M=D

// Restore THAT = *(FRAME - 1)
@R13
AM=M-1
D=M
@THAT
M=D

// Restore THIS = *(FRAME - 2)
@R13
AM=M-1
D=M
@THIS
M=D

// Restore ARG = *(FRAME - 3)
@R13
AM=M-1
D=M
@ARG
M=D

// Restore LCL = *(FRAME - 4)
@R13
AM=M-1
D=M
@LCL
M=D

// goto RET
@R14
A=M
0;JMP

// Final endless loop
(LOOP0)
@LOOP0
0;JMP
