// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


	// Psudo code
	//while( 1 )
//		if KBD == 0
//			for i=0, i<512*256/16, i=i+1
//				SCREEN[i] = 0
//		else
//			for i=0, i<512*256/16, i=i+1
//				SCREEN[i] = -1

	// Psudo assembly code
//LOOP:
//	D = @KBD
//	if D != 0 then goto ELSE
//	paint = -1
//	goto IFEND
//ELSE:
//	paint = 0
//IFEND:
//	i=0
//FORLOOP:	
//	i >= 8192; then FOREND
//	D=paint
//	SCREEN[i] = D
//	i = i + 1
//	goto FORLOOP
//FOREND:
//	goto LOOP

	(LOOP)
	@KBD
	D=M
	@ELSE
	D;JNE
	@i
	M=0
	(FORLOOP0)
	@8192
	D=A
	@i
	D=M-D
	@FOREND0
	D; JGE
	@SCREEN
	D=A
	@i
	A=M+D
	M=0
	@i
	M=M+1
	@FORLOOP0
	0; JMP
	(FOREND0)
	@IFEND
	0; JMP
	(ELSE)
	@i
	M=0
	(FORLOOP1)
	@8192
	D=A
	@i
	D=M-D
	@FOREND1
	D; JGE 
	@SCREEN
	D=A
	@i
	A=M+D
	M=-1
	@i
	M=M+1
	@FORLOOP1
	0; JMP
	(FOREND1)
	(IFEND)
	@LOOP
	0; JMP
	
