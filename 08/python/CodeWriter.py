import Parser
import os

class CodeWriter():
    def __init__(self, fname):
        self.fout = open(fname, 'w')
        self.label_num = 0
        label = os.path.basename(fname)     # ディレクトリ名を削除
        label,ext = os.path.splitext(label) # 拡張子を分離
        self.label_prefix = label+'.'
        self.callNum = 0

    # ブートストラップを挿入する
    def writeInit(self) :
        # SP = 256
        list = ['@256', 'D=A', '@SP', 'M=D']
        self.writeVMinst(list)

        # call Sys.init
        self.writeCall('Sys.init', '0')

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
                list = ['@'+index, 'D=A']
                self.writeVMinst(list)
                self.writeMicroPush()
            elif segment == 'local' :
                self.writePushMem1('@LCL', index)
            elif segment == 'argument' :
                self.writePushMem1('@ARG', index)
            elif segment == 'this' :
                self.writePushMem1('@THIS', index)
            elif segment == 'that' :
                self.writePushMem1('@THAT', index)
            elif segment == 'pointer' :
                self.writePushMem2('@3', index)
            elif segment == 'temp' :
                self.writePushMem2('@5', index)
            elif segment == 'static' :
                self.writePushStatic(index)

        elif command == Parser.Parser.C_POP :
            if segment == 'local' :
                self.writePopMem1('@LCL', index)
            elif segment == 'argument' :
                self.writePopMem1('@ARG', index)
            elif segment == 'this' :
                self.writePopMem1('@THIS', index)
            elif segment == 'that' :
                self.writePopMem1('@THAT', index)
            elif segment == 'pointer' :
                self.writePopMem2('@3', index)
            elif segment == 'temp' :
                self.writePopMem2('@5', index)
            elif segment == 'static' :
                self.writePopStatic(index)

    def close(self):
        self.fout.close()

    # micro push: Dレジスタの値をスタックに積む
    def writeMicroPush(self):
        list = ['@SP', 'A=M', 'M=D', '@SP', 'M=M+1','']
        self.writeVMinst(list)

    # micro pop: スタックの値をDレジスタにとってくる
    def writeMicroPop(self):
        list = ['@SP', 'M=M-1','@SP','A=M', 'D=M','']
        self.writeVMinst(list)

    # 比較命令の実装（分岐命令の種類の違いしかないので共通化
    def writeCompInst(self, branch) :
        self.writeMicroPop()
        true_label = str(self.label_prefix)+'IFTRUE'+str(self.label_num)
        end_label  = str(self.label_prefix)+'IFEND'+str(self.label_num)

        list = ['@SP', 'A=M-1', 'D=M-D','@'+true_label,
                'D;'+branch, '@SP', 'A=M-1', 'M=0', '@'+end_label,
                '0;JMP', '('+true_label+')', '@SP', 'A=M-1', 'M=-1',
                '('+end_label+')']
        self.writeVMinst(list)

        self.label_num = self.label_num + 1

    # local, argument, this, thatに対するpush命令
    def writePushMem1(self, amem, index):
        list = [amem, 'D=M', '@'+index, 'A=D+A', 'D=M', '']
        self.writeVMinst(list)
        self.writeMicroPush()

    # pointer, tempに対するpush命令
    def writePushMem2(self, amem, index):
        list = [amem, 'D=A', '@'+index, 'A=D+A', 'D=M', '']
        self.writeVMinst(list)
        self.writeMicroPush()

    # static に対するpush命令
    def writePushStatic(self, index) :
        list = ['@'+self.label_prefix+index, 'D=M']
        self.writeVMinst(list)
        self.writeMicroPush()

    # local, argument, this, thatに対するpop命令
    def writePopMem1(self, amem, index):
        self.writeMicroPop()
        # PopしたデータをRAM[13]に保存する
        list = ['@R13', 'M=D']
        self.writeVMinst(list)
        # 保存先のメモリアドレスを計算後，それをRAM[14]に保存し，
        # その後，RAM[14]に保存されたアドレスに，RAM[13]の内容をストアする
        list = [amem, 'D=M', '@'+index, 'D=D+A', '@R14', 'M=D',
                '@R13','D=M', '@R14', 'A=M', 'M=D', '']
        self.writeVMinst(list)

    # local, argument, this, thatに対するpop命令
    def writePopMem2(self, amem, index):
        self.writeMicroPop()
        # PopしたデータをRAM[13]に保存する
        list = ['@R13', 'M=D']
        self.writeVMinst(list)
        # 保存先のメモリアドレスを計算後，それをRAM[14]に保存し，
        # その後，RAM[14]に保存されたアドレスに，RAM[13]の内容をストアする
        list = [amem, 'D=A', '@'+index, 'D=D+A', '@R14', 'M=D',
                '@R13','D=M', '@R14', 'A=M', 'M=D', '']
        self.writeVMinst(list)

    # staticに対するpop命令
    def writePopStatic(self, index) :
        self.writeMicroPop()
        list = ['@'+self.label_prefix+index, 'M=D']
        self.writeVMinst(list)

    # labelコマンドをアセンブリプログラムに変換する
    def writeLabel(self, label) :
        list = ['('+self.label_prefix+label+')']
        self.writeVMinst(list)

    # gotoコマンドをアセンブリプログラムに変換する
    def writeGoto(self, label) :
        list = ['@'+self.label_prefix+label, '0;JMP', '']
        self.writeVMinst(list)

    # if-gotoコマンドをアセンブリプログラムに変換する
    def writeIf(self, label) :
        self.writeMicroPop()
        list = ['@'+self.label_prefix+label, 'D;JNE', '']
        self.writeVMinst(list)

    # function コマンドをアセンブリプログラムに変換する
    def writeFunction(self, functionName, numLocals) :
        list = ['('+functionName+')']
        self.writeVMinst(list)

        for i in range(int(numLocals)) :
            # push constant 0を実装
            list = ['@0','D=A']
            self.writeVMinst(list)
            self.writeMicroPush()

    # return コマンドをアセンブリプログラムに変換する
    def writeReturn(self) :
        # 一時変数のFRAMEをR13に割り当てる
        # FRAME = LCL
        list = ['@LCL', 'D=M', '@R13', 'M=D']
        self.writeVMinst(list)

        # 一時変数のRETをR14に割り当てる
        # DレジスタにFRAMEの内容があるはず
        # RET = *(FRAME-5)
        list = ('@5', 'A=D-A', 'D=M', '@R14', 'M=D')
        self.writeVMinst(list)

        # *ARG = pop()
        self.writeMicroPop()
        list = ['@ARG', 'A=M', 'M=D']
        self.writeVMinst(list)

        # SP = ARG+1
        list = ['@ARG', 'D=M+1', '@SP', 'M=D']
        self.writeVMinst(list)

        # THAT = *(FRAME-1)
        # THIS = *(FRAME-2)
        # ARG  = *(FRAME-3)
        # LCL  = *(FRAME-4)
        pairList = [('THAT', '1'), ('THIS', '2'), ('ARG', '3'), ('LCL', '4')]
        for reg, index in pairList :
            list = ['@R13', 'D=M', '@'+index, 'A=D-A', 'D=M', '@'+reg, 'M=D']
            self.writeVMinst(list)

        # goto RET
        list = ['//goto RET','@R14', 'A=M', '1;JMP']
        self.writeVMinst(list)

    # call コマンドをアセンブリプログラムに変換する
    def writeCall(self, functionName, numLocals) :
        # push return-address
        returnLabel = functionName + '$return' + str(self.callNum)
        list = ['@'+returnLabel, 'D=A']
        self.writeVMinst(list)
        self.writeMicroPush()

        # push LCL, ARG, THIS, THAT
        targetList = ['LCL', 'ARG', 'THIS', 'THAT']
        for target in targetList :
            list = ['@'+target, 'D=M']
            self.writeVMinst(list)
            self.writeMicroPush()

        # ARG = SP-n-5
        list = ['@SP', 'D=M', '@'+numLocals, 'D=D-A',
            '@5', 'D=D-A', '@ARG', 'M=D']
        self.writeVMinst(list)

        # LCL = SP
        list = ['@SP', 'D=M', '@LCL', 'M=D']
        self.writeVMinst(list)

        # goto f
        list = ['@'+functionName, '1;JMP']
        self.writeVMinst(list)

        # (return address)
        self.writeVMinst(['('+returnLabel+')'])

        # call回数を1つ増やす
        self.callNum = self.callNum + 1


    # 引数で渡されたリスト内の命令を改行コードをつけて
    # ファイルに出力する
    def writeVMinst(self, vmlist) :
        for vm in vmlist:
            self.fout.write(vm+'\n')
