// vm_code/NestedCall.vm
// function Sys.init 0
(Sys.init)
// push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
AM=M-1
D=M
@3
M=D

// push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
AM=M-1
D=M
@4
M=D

// call Sys.main 0
@CALL_LABEL0
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// ARG = SP - nArgs - 5
@SP
D=M
@5
D=D-A
@ARG
M=D

// LCL = SP
@SP
D=M
@LCL
M=D

// goto Fn
@Sys.main
0;JMP
// (return address)
(CALL_LABEL0)

// pop temp 1
@SP
AM=M-1
D=M
@6
M=D

(LOOP)
@LOOP
0;JMP
// function Sys.main 5
(Sys.main)
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

@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
AM=M-1
D=M
@3
M=D

// push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
AM=M-1
D=M
@4
M=D

// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 1
@1
D=A
@LCL
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 2
@2
D=A
@LCL
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 3
@3
D=A
@LCL
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Sys.add12 1
@CALL_LABEL1
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// ARG = SP - nArgs - 5
@SP
D=M
@6
D=D-A
@ARG
M=D

// LCL = SP
@SP
D=M
@LCL
M=D

// goto Fn
@Sys.add12
0;JMP
// (return address)
(CALL_LABEL1)

// pop temp 0
@SP
AM=M-1
D=M
@5
M=D

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

// push local 2
@LCL
D=M
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 3
@LCL
D=M
@3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 4
@LCL
D=M
@4
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

// add
@SP
AM=M-1
D=M
A=A-1
M=D+M

// add
@SP
AM=M-1
D=M
A=A-1
M=D+M

// add
@SP
AM=M-1
D=M
A=A-1
M=D+M

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

// function Sys.add12 0
(Sys.add12)
// push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
AM=M-1
D=M
@3
M=D

// push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
AM=M-1
D=M
@4
M=D

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

// push constant 12
@12
D=A
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
(LOOP2)
@LOOP2
0;JMP
