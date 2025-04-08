// vm_code/StackTest.vm
// push constant 17
@17 // load constant value
D=A // Put 17 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 17
@17 // load constant value
D=A // Put 17 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// eq
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE0
D;JEQ // Jump to TRUE0 if condition met
@SP
A=M
M=0 // false = 0
@FALSE0
0;JMP
(TRUE0)
@SP
A=M
M=-1 // true = -1
(FALSE0)
@SP
M=M+1 // push result
 SP++

// push constant 17
@17 // load constant value
D=A // Put 17 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 16
@16 // load constant value
D=A // Put 16 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// eq
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE1
D;JEQ // Jump to TRUE1 if condition met
@SP
A=M
M=0 // false = 0
@FALSE1
0;JMP
(TRUE1)
@SP
A=M
M=-1 // true = -1
(FALSE1)
@SP
M=M+1 // push result
 SP++

// push constant 16
@16 // load constant value
D=A // Put 16 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 17
@17 // load constant value
D=A // Put 17 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// eq
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE2
D;JEQ // Jump to TRUE2 if condition met
@SP
A=M
M=0 // false = 0
@FALSE2
0;JMP
(TRUE2)
@SP
A=M
M=-1 // true = -1
(FALSE2)
@SP
M=M+1 // push result
 SP++

// push constant 892
@892 // load constant value
D=A // Put 892 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 891
@891 // load constant value
D=A // Put 891 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// lt
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE3
D;JLT // Jump to TRUE3 if condition met
@SP
A=M
M=0 // false = 0
@FALSE3
0;JMP
(TRUE3)
@SP
A=M
M=-1 // true = -1
(FALSE3)
@SP
M=M+1 // push result
 SP++

// push constant 891
@891 // load constant value
D=A // Put 891 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 892
@892 // load constant value
D=A // Put 892 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// lt
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE4
D;JLT // Jump to TRUE4 if condition met
@SP
A=M
M=0 // false = 0
@FALSE4
0;JMP
(TRUE4)
@SP
A=M
M=-1 // true = -1
(FALSE4)
@SP
M=M+1 // push result
 SP++

// push constant 891
@891 // load constant value
D=A // Put 891 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 891
@891 // load constant value
D=A // Put 891 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// lt
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE5
D;JLT // Jump to TRUE5 if condition met
@SP
A=M
M=0 // false = 0
@FALSE5
0;JMP
(TRUE5)
@SP
A=M
M=-1 // true = -1
(FALSE5)
@SP
M=M+1 // push result
 SP++

// push constant 32767
@32767 // load constant value
D=A // Put 32767 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 32766
@32766 // load constant value
D=A // Put 32766 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// gt
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE6
D;JGT // Jump to TRUE6 if condition met
@SP
A=M
M=0 // false = 0
@FALSE6
0;JMP
(TRUE6)
@SP
A=M
M=-1 // true = -1
(FALSE6)
@SP
M=M+1 // push result
 SP++

// push constant 32766
@32766 // load constant value
D=A // Put 32766 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 32767
@32767 // load constant value
D=A // Put 32767 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// gt
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE7
D;JGT // Jump to TRUE7 if condition met
@SP
A=M
M=0 // false = 0
@FALSE7
0;JMP
(TRUE7)
@SP
A=M
M=-1 // true = -1
(FALSE7)
@SP
M=M+1 // push result
 SP++

// push constant 32766
@32766 // load constant value
D=A // Put 32766 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 32766
@32766 // load constant value
D=A // Put 32766 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// gt
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
@SP // Pop x
AM=M-1
D=M-D // D = x - y
@TRUE8
D;JGT // Jump to TRUE8 if condition met
@SP
A=M
M=0 // false = 0
@FALSE8
0;JMP
(TRUE8)
@SP
A=M
M=-1 // true = -1
(FALSE8)
@SP
M=M+1 // push result
 SP++

// push constant 57
@57 // load constant value
D=A // Put 57 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 31
@31 // load constant value
D=A // Put 31 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// push constant 53
@53 // load constant value
D=A // Put 53 into D
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

// push constant 112
@112 // load constant value
D=A // Put 112 into D
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

// neg
@SP // address stack pointer
A=M-1 // address X
M=-M // X = -X

// and
@SP // Pop Y
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
A=A-1 // address X
M=D&M // X = Y and X

// push constant 82
@82 // load constant value
D=A // Put 82 into D
@SP // Push D to stack
A=M // address stack
M=D // add D to stack
@SP
M=M+1 // increment stack pointer

// or
@SP // Pop to D
AM=M-1 // Decrement stack pointer
D=M // D = RAM[stack pointer]
A=A-1 // address X
M=D|M // X = Y or X

// not
@SP // address stack pointer
A=M-1 // address X
M=!M // X = not X

// Final endless loop
(LOOP9)
@LOOP9
0;JMP
