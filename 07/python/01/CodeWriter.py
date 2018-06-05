import Parser

class CodeWriter():
    def __init__(self, fname):
        self.fout = open(fname, 'w')

    def writeArithmetic(self, command):
        if command.find('add') >= 0 :
            self.writeMicroPop()
            self.fout.write('@SP\n')
            self.fout.write('M=M-1\n')
            self.fout.write('@SP\n')
            self.fout.write('A=M\n')
            self.fout.write('D=M+D\n')
            self.writeMicroPush()

    def writePushPop(self, command, segment, index):
        if command == Parser.Parser.C_PUSH :
            if segment == 'constant' :
                self.fout.write('@'+index+'\n')
                self.fout.write('D=A\n')
                self.writeMicroPush()

    def close(self):
        self.fout.close()

    # micro push: Dレジスタの値をスタックに積む
    def writeMicroPush(self):
        self.fout.write('@SP\n')
        self.fout.write('A=M\n')
        self.fout.write('M=D\n')
        self.fout.write('@SP\n')
        self.fout.write('M=M+1\n')

    # micro pop: スタックの値をDレジスタにとってくる
    def writeMicroPop(self):
        self.fout.write('@SP\n')
        self.fout.write('M=M-1\n')
        self.fout.write('@SP\n')
        self.fout.write('A=M\n')
        self.fout.write('D=M\n')
