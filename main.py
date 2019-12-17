import sys
from DES.key import Key
from DES.constants import Constants
from DES.extractor import Extractor


if __name__ == '__main__':
    constants = Constants()
    extractor = Extractor(constants.cp1(), constants.cp2())

    print(sys.argv[1])
    print(sys.argv[2])

    key_filename = sys.argv[1]
    msg_filename = sys.argv[2]

    # key = Key.from_file(key_filename)
    #
    # print(key)

    key = Key('0101111001011011010100100111111101010001000110101011110010010001')
    print(key)

    print(constants.cp1())

    result = key.extract_sub_keys(extractor)
    print(result)
