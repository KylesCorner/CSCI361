(init)
// Load index counter into memory
@8192
D=A
@R2
M=D

// Load screen pointer into memory
@SCREEN
D=A
@R0
M=D

(input)
@KBD
D=M

// if keyboard input > 0: goto black
@black
D;JGT

//white subroutine
@R1
M=0
@draw
0;JMP

//set color memory value to black
(black)
@R1
M=-1

(draw)
//Load color into D reg
@R1
D=M

//Set color of current pixel
@R0
A=M
M=D

//increment to next pixel
@R0
M=M+1

//decrement index counter
@R2
M=M-1
D=M

//continue drawing pixels or reset screen
@draw
D;JGT
@init
0;JMP
