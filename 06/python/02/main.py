# -*- coding: utf-8 -*-

import sys
import os

import Parser
import Code
import SymbolTable

if __name__ == '__main__' :

    # 引数の個数が1個でなければ，使い方を説明する内容を出力して，終了する
    # 引数には入力ファイル名が指定される仕様とする
    if len(sys.argv) != 2 :
        print('Usage: python '+sys.argv[0]+'file.asm')
        sys.exit(1)

    # 入力ファイル名の決定
    input_file_name = sys.argv[1]

    ######################## pass 1 ###########################
    # Parserオブジェクトを生成する
    parser = Parser.Parser(input_file_name)

    # Symbolオブジェクトを生成する
    symbolTable = SymbolTable.SymbolTable()

    # 現在の命令の位置を記憶する変数を定義
    current_pc = 0

    # 入力ファイルがコマンド（命令）を読み取れる限り，以下の処理を繰り返す
    while( parser.hasMoreCommands()):
        # 次の命令をフェッチする
        parser.advance()

        # 取得した命令のタイプを取得する
        inst_type = parser.commandType()

        if inst_type == parser.A_COMMAND :
            # A命令の場合は，current_pcを１増やす
            current_pc = current_pc + 1

        elif inst_type == parser.C_COMMAND :
            # C命令の場合は，current_pcを１増やす
            current_pc = current_pc + 1

        elif inst_type == parser.L_COMMAND :
            label = parser.symbol()
            symbolTable.addEntry(label, current_pc)

    ######################## pass 2 ###########################

    # Parserオブジェクトを生成する
    parser = Parser.Parser(input_file_name)

    # 入力ファイル名から出力ファイル名を作成する
    name, ext = os.path.splitext(input_file_name)
    output_file_name = name + '.hack'

    # 出力ファイルストリームをオープンする
    fout = open(output_file_name, 'w')

    code = Code.Code()

    # データメモリの現在使用可能な変数領域を表すアドレス
    var_address = 16

    # 入力ファイルがコマンド（命令）を読み取れる限り，以下の処理を繰り返す
    while( parser.hasMoreCommands()):
        # 次の命令をフェッチする
        parser.advance()

        # 取得した命令のタイプを取得する
        inst_type = parser.commandType()

        if inst_type == parser.A_COMMAND :
            # Aタイプの命令の場合，指定された10進数の値，
            # あるいは，ラベル名を取得する
            symbol = parser.symbol()

            # もしシンボルが数値であれば，整数値に変換する．
            # そうでなく，シンボルがラベル名である場合，
            # シンボルテーブルを参照して１0進数の数値を得る
            if symbol.isdigit() :
                val = int(symbol)
            else :
                # シンボルテーブルにラベル名が登録されていれば，
                # その数値を２進数に変換する
                if symbolTable.contains(symbol) :
                    val = symbolTable.getAddress(symbol)
                else :
                    # シンボルテーブルにラベル名がない場合
                    # 新規の変数名と判断して，新しいRAM領域を割り当て，
                    # 次に使用可能なRAM領域情報を更新する
                    symbolTable.addEntry(symbol, var_address)
                    val = var_address
                    var_address = var_address + 1

            # 得られた１０進数の数値を15ビットの2進数に変換する
            symbol = format(val, '015b')

            # 数値の値の先頭に0をつけたものが機械命令になる
            machine_inst = "0"+symbol

            # 変換した機械命令をファイルに書き込む．
            fout.write(machine_inst+'\n')

        elif inst_type == parser.C_COMMAND :
            # Cタイプの命令の場合，各フィールドの文字列を取得する
            dest = parser.dest()
            comp = parser.comp()
            jump = parser.jump()

            # 各フィールドの値を2進数に変換し，文字列として受け取る
            dest_bit = code.dest(dest)
            comp_bit = code.comp(comp)
            jump_bit = code.jump(jump)

            # 各フィールドの値を連結して，機械語に変換する
            machine_inst = "111"+comp_bit+dest_bit+jump_bit

            # 変換した機械命令をファイルに書き込む．
            fout.write(machine_inst+'\n')



    fout.close()
