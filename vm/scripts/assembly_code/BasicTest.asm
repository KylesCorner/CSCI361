// vm_code/BasicTest.vm
// push constant 10
@10 // load constant value
D=A // Put 10 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// pop local 0
@0 // load the index
D=A // D = index
@LCL // load base address of the segment
D=D+M // D = target address
@R13 // temp storage
M=D // R13 = address to store popped value
@SP // Pop to D
AM=M-1
D=M
@R13 // load temp storage
A=M // A = target address
M=D // *segment[index] = popped value

// push constant 21
@21 // load constant value
D=A // Put 21 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// push constant 22
@22 // load constant value
D=A // Put 22 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// pop argument 2
@2 // load the index
D=A // D = index
@ARG // load base address of the segment
D=D+M // D = target address
@R13 // temp storage
M=D // R13 = address to store popped value
@SP // Pop to D
AM=M-1
D=M
@R13 // load temp storage
A=M // A = target address
M=D // *segment[index] = popped value

// pop argument 1
@1 // load the index
D=A // D = index
@ARG // load base address of the segment
D=D+M // D = target address
@R13 // temp storage
M=D // R13 = address to store popped value
@SP // Pop to D
AM=M-1
D=M
@R13 // load temp storage
A=M // A = target address
M=D // *segment[index] = popped value

// push constant 36
@36 // load constant value
D=A // Put 36 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// pop this 6
@6 // load the index
D=A // D = index
@THIS // load base address of the segment
D=D+M // D = target address
@R13 // temp storage
M=D // R13 = address to store popped value
@SP // Pop to D
AM=M-1
D=M
@R13 // load temp storage
A=M // A = target address
M=D // *segment[index] = popped value

// push constant 42
@42 // load constant value
D=A // Put 42 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// push constant 45
@45 // load constant value
D=A // Put 45 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// pop that 5
@5 // load the index
D=A // D = index
@THAT // load base address of the segment
D=D+M // D = target address
@R13 // temp storage
M=D // R13 = address to store popped value
@SP // Pop to D
AM=M-1
D=M
@R13 // load temp storage
A=M // A = target address
M=D // *segment[index] = popped value

// pop that 2
@2 // load the index
D=A // D = index
@THAT // load base address of the segment
D=D+M // D = target address
@R13 // temp storage
M=D // R13 = address to store popped value
@SP // Pop to D
AM=M-1
D=M
@R13 // load temp storage
A=M // A = target address
M=D // *segment[index] = popped value

// push constant 510
@510 // load constant value
D=A // Put 510 into D
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// pop temp 6
@SP // Pop to D
AM=M-1
D=M
@11 // load pointer address
M=D // *address = D

// push local 0
@0 // load the index
D=A // D = index
@LCL // load the base address of the segment
A=M // get base pointer
A=D+A // final target address
D=M // D = value at target address
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// push that 5
@5 // load the index
D=A // D = index
@THAT // load the base address of the segment
A=M // get base pointer
A=D+A // final target address
D=M // D = value at target address
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

// push argument 1
@1 // load the index
D=A // D = index
@ARG // load the base address of the segment
A=M // get base pointer
A=D+A // final target address
D=M // D = value at target address
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// sub
@SP // Pop to D
AM=M-1
D=M
A=A-1
M=M-D

// push this 6
@6 // load the index
D=A // D = index
@THIS // load the base address of the segment
A=M // get base pointer
A=D+A // final target address
D=M // D = value at target address
@SP // Push D to stack
A=M
M=D
@SP
M=M+1

// push this 6
@6 // load the index
D=A // D = index
@THIS // load the base address of the segment
A=M // get base pointer
A=D+A // final target address
D=M // D = value at target address
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

// sub
@SP // Pop to D
AM=M-1
D=M
A=A-1
M=M-D

// push temp 6
@11 // load pointer address
D=M // D = *address
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
