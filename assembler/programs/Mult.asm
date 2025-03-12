(init)

@8192
D=A
@R2
M=D

@SCREEN
D=A
@R0
M=D

(input)
@KBD
D=M

@black
D;JGT

(white)
@R1
M=0
@draw
0;JMP

(black)
@R1
M=-1
@draw
0;JMP

(draw)
@R1
D=M

@R0
A=M
M=D

@R0
M=M+1

@R2
M=M-1
D=M

@draw
D;JGT
@init
0;JMP
