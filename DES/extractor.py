class Extractor:
    """
    Extract 16 sub key from a key
    """

    def __init__(self, cp1, cp2):
        self.cp1 = cp1
        self.cp2 = cp2

    def __call__(self, key):
        print("=============")
        print("Extract start")

        key_58 = self.__extract_security(key)
        print(len(key_58))
        print(self.cp1[0])
        permuted = self.__permute(key, self.cp1[0])
        print(permuted)
        print(self.cp2[0])
        left = permuted[0:28]
        right = permuted[28:]

        print("Left : ", left)
        print("Right : ", right)

        sub_keys = [None] * 16
        for index in range(16):
            left = self.__left_str_rotation(left)
            right = self.__left_str_rotation(right)
            print("permutation key", index)
            sub_keys[index] = self.__permute(left + right, self.cp2[0])

        print("Extract end")
        print("=============")
        return sub_keys

    @staticmethod
    def __extract_security(string):
        new_str = ''
        for i, char in enumerate(string):
            if i % 8 != 7:
                new_str += char
        return new_str

    @staticmethod
    def __permute(key, permutation_mat):
        new_str = ''
        for pos in permutation_mat:
            new_str += key[int(pos)]
        return new_str

    @staticmethod
    def __left_str_rotation(string):
        return string[1:] + string[0]
