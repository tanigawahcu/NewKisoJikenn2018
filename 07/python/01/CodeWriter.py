import Parser

class CodeWriter():
    def __init__(self, fname):
        self.fout = open(fname, 'w')

    def writeArithmetic(self, command):
        if command.find('add') >= 0 :
            self.writeMicroPop()
            list = ['@SP','A=M-1', 'M=M+D']
            self.writeVMinst(list)

        elif command.find('sub') >= 0 :
            self.writeMicroPop()
            list = ['@SP','A=M-1', 'M=M-D']
            self.writeVMinst(list)

        elif command.find('neg') >= 0 :
            list = ['@SP','A=M-1', 'M=-M']
            self.writeVMinst(list)

        elif command.find('eq') >= 0 :
            self.writeMicroPop()
            self.fout.write('@SP\n')
            self.fout.write('A=M-1\n')
            self.fout.write('D=M-D\n')
            self.fout.write('@LOOP'+loop_num)
            D;

        elif command.find('and') >= 0 :
            self.writeMicroPop()
            list = ['@SP','A=M-1', 'M=D&M']
            self.writeVMinst(list)

        elif command.find('or') >= 0 :
            self.writeMicroPop()
            list = ['@SP','A=M-1', 'M=D|M']
            self.writeVMinst(list)

        elif command.find('not') >= 0 :
            list = ['@SP','A=M-1', 'M=!M']
            self.writeVMinst(list)

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
        list = ['@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
        self.writeVMinst(list)

    # micro pop: スタックの値をDレジスタにとってくる
    def writeMicroPop(self):
        list = ['@SP', 'M=M-1','@SP','A=M', 'D=M']
        self.writeVMinst(list)

    # 引数で渡されたリスト内の命令を改行コードをつけて
    # ファイルに出力する
    def writeVMinst(self, vmlist) :
        for vm in vmlist:
            self.fout.write(vm+'\n')
