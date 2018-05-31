# -*- coding: utf-8 -*-

import sys
import os

import Parser
import Code

if __name__ == '__main__' :

    # 引数の個数が1個でなければ，使い方を説明する内容を出力して，終了する
    # 引数には入力ファイル名が指定される仕様とする
    if len(sys.argv) != 2 :
        print('Usage: python '+sys.argv[0]+'file.asm')
        sys.exit(1)

    # 入力ファイル名の決定
    input_file_name = sys.argv[1]

    # Parserオブジェクトを生成する
    parser = Parser.Parser(input_file_name)

    # 入力ファイル名から出力ファイル名を作成する
    name, ext = os.path.splitext(input_file_name)
    output_file_name = name + '.hack'

    # 出力ファイルストリームをオープンする
    fout = open(output_file_name, 'w')

    code = Code.Code()

    # 入力ファイルがコマンド（命令）を読み取れる限り，以下の処理を繰り返す
    while( parser.hasMoreCommands()):
        # 次の命令をフェッチする
        parser.advance()

        # 取得した命令のタイプを取得する
        inst_type = parser.commandType()

        if inst_type == parser.A_COMMAND :
            # Aタイプの命令の場合，指定された10進数の値を
            # 2進数で表記した文字列を取得する
            symbol = parser.symbol()

            # 数値の値の先頭に0をつけたものが機械命令になる
            machine_inst = "0"+symbol

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

        elif inst_type == parser.L_COMMAND :
            machine_inst = ''

        else :
            machine_inst = ''

        # 変換した機械命令をファイルに書き込む．
        fout.write(machine_inst+'\n')

    fout.close()
