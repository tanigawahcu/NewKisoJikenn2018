# -*- coding: utf-8 -*-

import sys
import os

import Parser
import CodeWriter

if __name__ == '__main__' :

    # 引数の個数が1個でなければ，使い方を説明する内容を出力して，終了する
    # 引数には入力ファイル名が指定される仕様とする
    if len(sys.argv) != 2 :
        print('Usage: python '+sys.argv[0]+'file.vm')
        print('Usage: python '+sys.argv[0]+'vm_ file_directory')
        sys.exit(1)

    # 入力ファイルのリスト
    input_file_list = []

    if os.path.isfile(sys.argv[1]) :
        # ファイル名が1つ指定されているのであれば，それをリストに追加する
        input_file_list.append(sys.argv[1])

        # 入力ファイル名から出力ファイル名を作成する
        name, ext = os.path.splitext(sys.argv[1])
        output_file_name = name + '.asm'
    else :
        # ディレクトリが指定された場合，ディレクトリ内のファイルをリストに追加する
        # 作業ディレクトリ内にvmファイル以外があってもよい？？
        dir_name = sys.argv[1].strip('/')
        for fname in os.listdir(dir_name) :
            if fname.find('.vm') >= 0 :
                input_file_list.append(dir_name+'/'+fname)

        # 入力ディレクトリ名から出力ファイル名を作成する
        output_file_name = dir_name + '.asm'

    #CodeWriterモジュールをインスタンス化する
    writer = CodeWriter.CodeWriter(output_file_name)

    # 入力ファイル毎にParserを呼び出し，出力ファイルに書き込んでいく
    for fin_name in input_file_list:

        # Parserオブジェクトを生成する
        parser = Parser.Parser(fin_name)

        # 入力ファイルがコマンド（命令）を読み取れる限り，以下の処理を繰り返す
        while( parser.hasMoreCommands()):
            # 次の命令をフェッチする
            parser.advance()

            # 取得したVM命令のタイプを取得する
            vm_type = parser.commandType()

            if vm_type == parser.C_ARITHMETIC :
                # 算術命令の場合，命令を取り出す，
                op = parser.arg1()

                # 算術演算をアセンブリプログラムに変換して書き込む
                writer.writeArithmetic(op)

            elif vm_type == parser.C_PUSH or vm_type == parser.C_POP:
                # push命令，あるいは，pop命令の場合
                writer.writePushPop(vm_type, parser.arg1(), parser.arg2())

            elif vm_type == parser.C_LABEL :
                writer.writeLabel(parser.arg1())

            elif vm_type == parser.C_GOTO :
                writer.writeGoto(parser.arg1())

            elif vm_type == parser.C_IF :
                writer.writeIf(parser.arg1())

            elif vm_type == parser.C_FUNCTION :
                writer.writeFunction(parser.arg1(), parser.arg2())

            elif vm_type == parser.C_RETURN :
                writer.writeReturn()

            elif vm_type == parser.C_CALL :
                writer.writeCall(parser.arg1(), parser.arg2())


    # 出力ファイルをクローズする
    writer.close()
