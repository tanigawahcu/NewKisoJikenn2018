class Parser():
    # @property
    # def A_COMMAND(self):
    #     return 1
    # @property
    # def C_COMMAND(self):
    #     return 2
    # @property
    # def L_COMMAND(self):
    #     return 3
    C_ARITHMETIC = 0
    C_PUSH       = 1
    C_POP        = 2
    C_LABEL      = 3
    C_GOTO       = 4
    C_IF         = 5
    C_FUNCTION   = 6
    C_RETURN     = 7
    C_CALL       = 8
    C_UNKNOWN    = 9

    def __init__(self, fin_name):
        # 入力ファイルのストリームをオープンする
        self.fin = open(fin_name, 'r')
        self.command = ''

    # まだ命令を含むかどうか判断する
    def hasMoreCommands(self):

        while True:
            # 次の行を読み込む
            line = self.fin.readline()

            # もしlineが空行であれば，EOFに達した
            if line == '' :
                return False

            #先頭と最後にある空白などを取り除く
            self.command = line.strip()

            # もしコメント行，あるいは，空行　であれば，次の行を読み込む
            if self.command[0:2] == '//' or self.command == '':
                pass
            else:
                break

        # commandが存在すれば命令が含んでいると判断する
        return True

    # 次の命令を実際にファイルから読み込む
    def advance(self):
        #実際の取り込み操作はhasMoreCommandでやってしまう
        #ここでは命令の後ろの方にあるコメントや空白を取り除く作業をする

        # 行の途中からコメントが入っていれば，それを取り除く
        index = self.command.find('//')
        if index >= 0 :
            self.command = self.command[:index]
            # 命令とコメントまでの空白を取り除く
            self.command = self.command.strip()

        # スペースを区切り文字として，フィールドのリストとする
        self.fields = self.command.split()


    # 取り込んだ命令の種類を判別する
    def commandType(self):
        arith_lists = ['add', 'sub', 'neg', 'eq',
            'gt', 'lt', 'and', 'or', 'not']
        for op in arith_lists:
            if self.command.find(op) :
                self.type = self.C_ARITHMETIC

        if self.command.find('push') >= 0 :
            self.type = self.C_PUSH
        elif self.command.find('pop') >= 0 :
            self.type = self.C_POP
        else :
            self.type = self.C_UNKNOWN

        return self.type

    def arg1(self):
        if self.type == self.C_ARITHMETIC :
            # 算術演算の場合，コマンドそのものを返す
            return self.fields[0]

        elif self.type == self.C_POP or self.type == self.C_PUSH:
            # フィールドの1つ目を返す
            return self.fields[1]

    def arg2(self):
        # pushかpopのみ動作する
        if self.type == self.C_PUSH or self.type == self.C_POP :
            # フィールドの2つ目を返す
            return self.fields[2]
