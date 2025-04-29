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

 // vm_code/FibonacciElement/
 // function Sys.init 0
(Sys.init)
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

 // call Main.fibonacci 1
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
@Main.fibonacci
0;JMP
(CALL_LABEL2)  // (return address)

(END)
@END
0;JMP

 // Final endless loop
(LOOP3)
@LOOP3
0;JMP
 // vm_code/FibonacciElement/
 // function Main.fibonacci 0
(Main.fibonacci)
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

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

 // lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE4
D;JLT
@SP
A=M
M=0
@FALSE5
0;JMP
(TRUE4)
@SP
A=M
M=-1
(FALSE5)
@SP
M=M+1

@SP
AM=M-1
D=M
@N_LT_2
D;JNE

@N_GE_2
0;JMP

(N_LT_2)
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

(N_GE_2)
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

// push constant 2
@2
D=A
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

 // call Main.fibonacci 1
@CALL_LABEL6
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
@Main.fibonacci
0;JMP
(CALL_LABEL6)  // (return address)

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

// push constant 1
@1
D=A
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

 // call Main.fibonacci 1
@CALL_LABEL7
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
@Main.fibonacci
0;JMP
(CALL_LABEL7)  // (return address)

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
