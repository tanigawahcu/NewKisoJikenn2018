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

@SP
M=M-1
@SP
A=M
D=M

@R13
M=D
@3
D=A
@1
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

@0
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

@R13
M=D
@THAT
D=M
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

@1
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

@R13
M=D
@THAT
D=M
@1
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

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

@2
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
M=M-1
@SP
A=M
D=M

@R13
M=D
@ARG
D=M
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

(FibonacciSeries.MAIN_LOOP_START)
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

@SP
M=M-1
@SP
A=M
D=M

@FibonacciSeries.COMPUTE_ELEMENT
D;JNE

@FibonacciSeries.END_PROGRAM
0;JMP

(FibonacciSeries.COMPUTE_ELEMENT)
@THAT
D=M
@0
A=D+A
D=M

@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@1
A=D+A
D=M

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
@SP
M=M-1
@SP
A=M
D=M

@R13
M=D
@THAT
D=M
@2
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

@3
D=A
@1
A=D+A
D=M

@SP
A=M
M=D
@SP
M=M+1

@1
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
@SP
M=M-1
@SP
A=M
D=M

@R13
M=D
@3
D=A
@1
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

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

@1
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
M=M-1
@SP
A=M
D=M

@R13
M=D
@ARG
D=M
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

@FibonacciSeries.MAIN_LOOP_START
0;JMP

(FibonacciSeries.END_PROGRAM)
