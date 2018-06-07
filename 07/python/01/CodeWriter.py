import Parser
import os

class CodeWriter():
    def __init__(self, fname):
        self.fout = open(fname, 'w')
        self.label_num = 0
        label = os.path.basename(fname)     # ディレクトリ名を削除
        label,ext = os.path.splitext(label) # 拡張子を分離
        self.label_index = label+'.'

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
            self.writeCompInst('JEQ')

        elif command.find('gt') >= 0 :
            self.writeCompInst('JGT')

        elif command.find('lt') >= 0 :
            self.writeCompInst('JLT')

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

    # 比較命令の実装（分岐命令の種類の違いしかないので共通化
    def writeCompInst(self, branch) :
        self.writeMicroPop()
        true_label = str(self.label_index)+'IFTRUE'+str(self.label_num)
        end_label  = str(self.label_index)+'IFEND'+str(self.label_num)

        list = ['@SP', 'A=M-1', 'D=M-D','@'+true_label,
                'D;'+branch, '@SP', 'A=M-1', 'M=0', '@'+end_label,
                '0;JMP', '('+true_label+')', '@SP', 'A=M-1', 'M=-1',
                '('+end_label+')']
        self.writeVMinst(list)

        self.label_num = self.label_num + 1
