(Sys.init)
@4000
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
@3
D=A
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

@5000
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

@Sys.main$return0
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

@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
1;JMP
(Sys.main$return0)
@SP
M=M-1
@SP
A=M
D=M

@R13
M=D
@5
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

(04NestedCall.LOOP)
@04NestedCall.LOOP
0;JMP

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

@4001
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
@3
D=A
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

@5001
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

@200
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
@LCL
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

@40
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
@LCL
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

@6
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
@LCL
D=M
@3
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

@123
D=A
@SP
A=M
M=D
@SP
M=M+1

@Sys.add12$return1
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

@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
1;JMP
(Sys.add12$return1)
@SP
M=M-1
@SP
A=M
D=M

@R13
M=D
@5
D=A
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

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

@SP
A=M-1
M=M+D
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

@SP
A=M-1
M=M+D
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
M=M-1
@SP
A=M
D=M

@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
//goto RET
@R14
A=M
1;JMP
(Sys.add12)
@4002
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
@3
D=A
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D

@5002
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

@12
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
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
M=M-1
@SP
A=M
D=M

@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
//goto RET
@R14
A=M
1;JMP
