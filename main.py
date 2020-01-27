import sys
from DES.key import Key
from DES.constants import Constants
from DES.extractor import Extractor
from DES.packager import Packager


from DES.ConvAlphaBin import conv_bin, nib_vnoc


from DES.encrypt import Encrypt

class Round:
    def __init__(self, key, sub_matrix, expension_matrix):
        self.key = key
        self.expension_matrix = expension_matrix
        pass

    def __call__(self, message):
        # 0 Split
        left = message[0:32]
        right = message[32:]

        # 1 Expand
        e_right = self.expand(right)

        # 2 XOR
        new_block = ''
        for index in range(48):
            new_block += self.xor(e_right[index], self.key[index])

        # 3.1 Cut into 8 block 6 bits
        # 3.2 Get numbers
        blocks_pair = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)] # stub

        # 4 Substitution matrix
        substitution_numbers = ['1001', '1001', '1001', '1001', '1001', '1001', '1001', '1001'] # stub

        # 5 XOR droite
        val = ''
        for i in len(32):
            val += self.xor(substitution_numbers, left[i])

        print(new_block)

        return [right, last_result]

    def expand(self, block):
        new_block = ''
        for index in range(48):
            position = int(self.expension_matrix[index]) - 1
            new_block += block[position]
        return new_block

    @staticmethod
    def xor(a, b):
        return "0" if a == b else "1"


# if __name__ == '__main__':
#     constants = Constants()
#     extractor = Extractor(constants.cp1(), constants.cp2())
#     packager = Packager(64, constants.pi())  # 64 bits size + initial permutation
#
#     print(sys.argv[1])
#     print(sys.argv[2])
#
#     key_filename = sys.argv[1]
#     msg_filename = sys.argv[2]
#
#     # key = Key.from_file(key_filename)
#     #
#     # print(key)
#
#     message = "Hello World"
#
#     key = Key('0101111001011011010100100111111101010001000110101011110010010001')
#     print(key)
#
#     print("CP1 => ", constants.cp1())
#
#     sub_keys = key.extract_sub_keys(extractor)
#
#     message_packets = packager(message)
#     print("Message => ", message)
#     print("Message packets => ", message_packets)
#
#     print(sub_keys)
#
#     print('Permutation', packager.permutation('1101110010111011110001001101010111100110111101111100001000110010'))
#
#
#
#     print("Message a dechiffer", nib_vnoc('1101110010111011110001001101010111100110111101111100001000110010100111010010101101101011111000110011101011011111'))
#     print("Message a chiffer", conv_bin('!LvE.eb!wjKdK,vjOtè'))

if __name__ == '__main__':
    message = "Hello World my friend"

    key_filename = sys.argv[1]
    key = Key.from_file(key_filename)

    encrypt = Encrypt()
    result = encrypt(message, key)

    print('result', result)