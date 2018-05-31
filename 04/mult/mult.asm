// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// Put your code here.

	// first write psudo code
	//r2=0
	//for(i=0, i<r0, i=i+1)
	//	r2=r2+r1

	// second modify high level control description
	// to simple if-then goto description
	//i=0
	//r2=0
	//LOOP:		
	//if i>=r0 then goto END
	//r2=r2+r1
	//i=i+1
	//jump LOOP
	//END:
	
	// third translate the code to Jack assembly language
	// i=0
	@i
	M=0
	// r2=0
	@R2
	M=0
	(LOOP)
	// D=i-r0
	// D=i
	// A=r0
	// D=D-M
	@i
	D=M
	@R0
	D=D-M
	@END
	// if D >= 0 then goto END
	D ; JGE
	// r2=r2+r1
	@R1
	D=M
	@R2
	M=M+D
	// i=i+1
	@i
	M=M+1
	// jump LOOP
	@LOOP
	0; JMP
	(END)
	@END
	0; JMP
	
