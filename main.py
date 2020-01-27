import sys
from DES.key import Key
from DES.encrypt import Encrypt, Decrypt

from DES.ConvAlphaBin import conv_bin, nib_vnoc

if __name__ == '__main__':
    message = "Hello World my friend"

    key_filename = sys.argv[1]
    key = Key.from_file(key_filename)

    key = Key("0101111001011011010100100111111101010001000110101011110010010001")

    encrypt = Encrypt()
    result = encrypt(message, key)

    print('result', result)

    # decrypt = Decrypt()
    # result2 = decrypt(result, key)
    #
    # print('result 2 ', result2)
    #
    #
    # print(nib_vnoc("1101110010111011110001001101010111100110111101111100001000110010100111010010101101101011111000110011101011011111"))
    # print(conv_bin("!LvE.eb!wjKdK,vjOtè"))
