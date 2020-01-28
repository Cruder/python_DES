import sys
from DES.key import Key
from DES.encrypt import Encrypt

if __name__ == '__main__':
    message = "Hello World my friend :)"

    key_filename = sys.argv[1]
    key = Key.from_file(key_filename)

    # key = Key("0101111001011011010100100111111101010001000110101011110010010001")

    encrypt = Encrypt()
    result = encrypt(message, key, "encrypt")

    print('result', result)

    # result = ''
    # f = open(sys.argv[2])
    # line = f.readline()
    # while line != '':
    #     result += line
    #     line = f.readline()

    decrypt = Encrypt()
    result2 = decrypt(result, key, "decrypt")

    print('result 2 ', result2)
