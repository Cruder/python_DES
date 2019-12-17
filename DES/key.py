class Key:
    @staticmethod
    def from_file(filename):
        with open(filename) as file:
            return Key(file.read())

    def __init__(self, key):
        self.key = key

    def __str__(self):
        string = ''
        for i in range(0, 8):
            for j in range(0, 8):
                if j == 7: string += ' | '
                string += self.key[i * 8 + j] + ' '
            string += "\n"
        return string

    def extract_sub_keys(self, extractor):
        """
        Remove security bits then transmute the 56 bits key
        Finally divide the permuted key into 16 keys.
        :return: a list of the 16 sub-keys of the key
        """
        return extractor(self.key)
