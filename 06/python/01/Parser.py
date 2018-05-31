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
        pass

    # 取り込んだ命令の種類を判別する
    def commandType(self):
        if self.command[0] == '@':
            return self.A_COMMAND
        elif self.command[0] == '(':
            return self.L_COMMAND
        else :
            return self.C_COMMAND

    def symbol(self):
        # 先頭の’＠’を取り除いた数値の文字列を取り出す
        int_string = self.command.strip('@')

        # 10進数の文字列を整数に変換する
        int_value = int(int_string)

        # 2進数の文字列に変換する（先頭に'0b'が含まれる）
        bin_string = format(int_value,'015b')

        return bin_string.replace('0b','')

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
