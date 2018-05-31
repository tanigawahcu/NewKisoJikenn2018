class Code():
    def __init__(self):
        pass

    def dest(self, mnemonic):
        dest_dict = {'':'000',  'M':'001',  'D':'010',  'MD':'011',
                'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111'}
        return dest_dict[mnemonic]

    def comp(self, mnemonic):
        comp_dict = {'0':'101010', '1':'111111', '-1':'111010',
            'X':'001100', 'Y':'110000', '!X':'001101',
            '!Y':'110001', '-X':'001111', '-Y':'110011',
            'X+1':'011111', 'Y+1':'110111', 'X-1':'001110',
            'Y-1':'110010', 'X+Y':'000010', 'X-Y':'010011',
            'Y-X':'000111', 'X&Y':'000000', 'X|Y':'010101'}

        # aフィールドの判定
        if mnemonic.find('M') > -1 :
            a = '1'
        else :
            a = '0'

        # 'D'→’X’に，'A/M'を'Y'に置き換える
        comp0 = mnemonic.replace('D','X').replace('A','Y').replace('M','Y')

        return a+comp_dict[comp0]

    def jump(self, mnemonic):
        jump_dict = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011',
                    'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}
        return jump_dict[mnemonic]
