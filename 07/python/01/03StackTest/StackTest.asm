@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE0
D;JEQ
@SP
A=M-1
M=0
@StackTest.IFEND0
0;JMP
(StackTest.IFTRUE0)
@SP
A=M-1
M=-1
(StackTest.IFEND0)
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE1
D;JEQ
@SP
A=M-1
M=0
@StackTest.IFEND1
0;JMP
(StackTest.IFTRUE1)
@SP
A=M-1
M=-1
(StackTest.IFEND1)
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE2
D;JEQ
@SP
A=M-1
M=0
@StackTest.IFEND2
0;JMP
(StackTest.IFTRUE2)
@SP
A=M-1
M=-1
(StackTest.IFEND2)
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE3
D;JLT
@SP
A=M-1
M=0
@StackTest.IFEND3
0;JMP
(StackTest.IFTRUE3)
@SP
A=M-1
M=-1
(StackTest.IFEND3)
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE4
D;JLT
@SP
A=M-1
M=0
@StackTest.IFEND4
0;JMP
(StackTest.IFTRUE4)
@SP
A=M-1
M=-1
(StackTest.IFEND4)
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE5
D;JLT
@SP
A=M-1
M=0
@StackTest.IFEND5
0;JMP
(StackTest.IFTRUE5)
@SP
A=M-1
M=-1
(StackTest.IFEND5)
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE6
D;JGT
@SP
A=M-1
M=0
@StackTest.IFEND6
0;JMP
(StackTest.IFTRUE6)
@SP
A=M-1
M=-1
(StackTest.IFEND6)
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE7
D;JGT
@SP
A=M-1
M=0
@StackTest.IFEND7
0;JMP
(StackTest.IFTRUE7)
@SP
A=M-1
M=-1
(StackTest.IFEND7)
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
D=M-D
@StackTest.IFTRUE8
D;JGT
@SP
A=M-1
M=0
@StackTest.IFEND8
0;JMP
(StackTest.IFTRUE8)
@SP
A=M-1
M=-1
(StackTest.IFEND8)
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M+D
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M-D
@SP
A=M-1
M=-M
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=D&M
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=D|M
@SP
A=M-1
M=!M