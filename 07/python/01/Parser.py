class Parser():
    @property
    def A_COMMAND(self):
        return 1
    @property
    def C_COMMAND(self):
        return 2
    @property
    def L_COMMAND(self):
        return 3

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

    # 取り込んだ命令の種類を判別する
    def commandType(self):
        if self.command[0] == '@':
            self.type = self.A_COMMAND
        elif self.command[0] == '(':
            self.type = self.L_COMMAND
        else :
            self.type = self.C_COMMAND

        return self.type

    def symbol(self):
        if self.type == self.A_COMMAND :
            # 先頭の’＠’を取り除いた文字列を取り出す

            return self.command.strip('@')

        elif self.type == self.L_COMMAND :
            # 先頭と最後の()を取り除いたラベルを取得する
            label = self.command.strip('()')

            return label

    def dest(self):
        # destフィールドは'='の記号より前
        # '='を含まない場合は，空文字を返す
        if '=' in self.command:
            # '=' の位置を検索する
            index = self.command.find('=')
            # '='の位置までの文字列を取り出す
            dest_str = self.command[:index]
            # 取り出した文字列よりスペースなどを取り除き，返す
            return dest_str.strip()
        else :
            return ''

    def comp(self):
        # compフィールドは'='と';'の間．
        # '='と';'はない場合もある．

        # '=' より後の文字列を取り出す
        if '=' in self.command:
            index = self.command.find('=')
            comp0_str = self.command[index+1:]
        else:
            comp0_str = self.command

        # ';' より前の文字列を取り出す
        if ';' in comp0_str :
            index = comp0_str.find(';')
            comp1_str = comp0_str[:index]
        else :
            comp1_str = comp0_str

        # 取り出した文字列よりスペースなどを取り除き，返す
        return comp1_str.strip()

    def jump(self):
        # jumpフィールドは';'の記号より後
        # ';'を含まない場合は，空文字を返す
        if ';' in self.command:
            # ';' の位置を検索する
            index = self.command.find(';')
            # '='の位置までの文字列を取り出す
            jump_str = self.command[index+1:]
            # 取り出した文字列よりスペースなどを取り除き，返す
            return jump_str.strip()
        else :
            return ''
