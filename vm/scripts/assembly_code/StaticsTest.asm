@256
D=A
@SP
M=D
A=A+1
M=-1
A=A+1
M=-1
A=A+1
M=-1
A=A+1
M=-1
 // call Sys.init 0
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
@LCL
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
@Sys.init
0;JMP
(CALL_LABEL0)  // (return address)

@HALT1
 (HALT1)
 0;JMP

 // vm_code/StaticsTest/
 // function Sys.init 0
(Sys.init)
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

 // call Class1.set 2
@CALL_LABEL2
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
@LCL
@7
D=D-A
@ARG
M=D

 // LCL = SP
@SP
D=M
@LCL
M=D

 // goto Fn
@Class1.set
0;JMP
(CALL_LABEL2)  // (return address)

// pop temp 0
@SP
AM=M-1
D=M
@5
M=D

// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

 // call Class2.set 2
@CALL_LABEL3
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
@LCL
@7
D=D-A
@ARG
M=D

 // LCL = SP
@SP
D=M
@LCL
M=D

 // goto Fn
@Class2.set
0;JMP
(CALL_LABEL3)  // (return address)

// pop temp 0
@SP
AM=M-1
D=M
@5
M=D

 // call Class1.get 0
@CALL_LABEL4
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
@LCL
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
@Class1.get
0;JMP
(CALL_LABEL4)  // (return address)

 // call Class2.get 0
@CALL_LABEL5
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
@LCL
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
@Class2.get
0;JMP
(CALL_LABEL5)  // (return address)

(END)
@END
0;JMP

 // Final endless loop
(LOOP6)
@LOOP6
0;JMP
 // vm_code/StaticsTest/
 // function Class2.set 0
(Class2.set)
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

// pop static 0
@SP
AM=M-1
D=M
@Class2.0
M=D

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

// pop static 1
@SP
AM=M-1
D=M
@Class2.1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

 // return
 // FRAME = LCL
@LCL
D=M
@R14
M=D // RET = *(FRAME - 5)
@5
A=D-A
D=M
@R15   // R!$ =RET
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
@R14
AM=M-1
D=M
@THAT
M=D

 // Restore THIS = *(FRAME - 2)
@R14
AM=M-1
D=M
@THIS
M=D

 // Restore ARG = *(FRAME - 3)
@R14
AM=M-1
D=M
@ARG
M=D

 // Restore LCL = *(FRAME - 4)
@R14
AM=M-1
D=M
@LCL
M=D

 // goto RET
@R15
A=M
0;JMP

 // function Class2.get 0
(Class2.get)
// push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@Class2.1
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
@R14
M=D // RET = *(FRAME - 5)
@5
A=D-A
D=M
@R15   // R!$ =RET
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
@R14
AM=M-1
D=M
@THAT
M=D

 // Restore THIS = *(FRAME - 2)
@R14
AM=M-1
D=M
@THIS
M=D

 // Restore ARG = *(FRAME - 3)
@R14
AM=M-1
D=M
@ARG
M=D

 // Restore LCL = *(FRAME - 4)
@R14
AM=M-1
D=M
@LCL
M=D

 // goto RET
@R15
A=M
0;JMP

 // Final endless loop
(LOOP7)
@LOOP7
0;JMP
 // vm_code/StaticsTest/
 // function Class1.set 0
(Class1.set)
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

// pop static 0
@SP
AM=M-1
D=M
@Class1.0
M=D

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

// pop static 1
@SP
AM=M-1
D=M
@Class1.1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

 // return
 // FRAME = LCL
@LCL
D=M
@R14
M=D // RET = *(FRAME - 5)
@5
A=D-A
D=M
@R15   // R!$ =RET
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
@R14
AM=M-1
D=M
@THAT
M=D

 // Restore THIS = *(FRAME - 2)
@R14
AM=M-1
D=M
@THIS
M=D

 // Restore ARG = *(FRAME - 3)
@R14
AM=M-1
D=M
@ARG
M=D

 // Restore LCL = *(FRAME - 4)
@R14
AM=M-1
D=M
@LCL
M=D

 // goto RET
@R15
A=M
0;JMP

 // function Class1.get 0
(Class1.get)
// push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@Class1.1
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
@R14
M=D // RET = *(FRAME - 5)
@5
A=D-A
D=M
@R15   // R!$ =RET
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
@R14
AM=M-1
D=M
@THAT
M=D

 // Restore THIS = *(FRAME - 2)
@R14
AM=M-1
D=M
@THIS
M=D

 // Restore ARG = *(FRAME - 3)
@R14
AM=M-1
D=M
@ARG
M=D

 // Restore LCL = *(FRAME - 4)
@R14
AM=M-1
D=M
@LCL
M=D

 // goto RET
@R15
A=M
0;JMP

 // Final endless loop
(LOOP8)
@LOOP8
0;JMP
