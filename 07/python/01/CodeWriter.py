import Parser

class CodeWriter():
    def __init__(self, fname):
        self.fout = open(fname, 'w')

    def writeArithmetic(self, command):
        pass

    def writePushPop(self, command, segment, index):
        if command == Parser.Parser.C_PUSH :
            if segment == 'constant' :
                self.fout.write('@'+index+'\n')
                self.fout.write('D=A\n')
                self.fout.write('@SP\n')
                self.fout.write('A=M\n')
                self.fout.write('M=D\n')
                self.fout.write('@SP\n')
                self.fout.write('M=M+1')

    def close(self):
        self.fout.close()
