class Extractor:
    """
    Extract 16 sub key from a key
    """

    def __init__(self, cp1, cp2):
        self.cp1 = cp1
        self.cp2 = cp2

    def first_perm(self, key):

        return self.__permute(key, self.cp1[0])

    def __call__(self, key):
        permuted = self.__permute(key, self.cp1[0])
        left = permuted[0:28]
        right = permuted[28:]

        sub_keys = []
        for index in range(16):
            left = self.__left_str_rotation(left)
            right = self.__left_str_rotation(right)
            sub_keys.append(self.__permute(left + right, self.cp2[0]))

        print("\033[0;33;40mInitial key ", key)
        print("Permutations")
        [print(key) for key in sub_keys]
        print("\033[0;0;40m")

        return sub_keys

    @staticmethod
    def __permute(key, permutation_mat):
        new_str = ''
        for pos in permutation_mat:
            new_str += key[int(pos)]
        return new_str

    @staticmethod
    def __left_str_rotation(string):
        return string[1:] + string[0]
