from DES.permutator import Permutator


class Round:
    def __init__(self, key, perm_matrix, expension_matrix, substitutions_matrix):
        self.key = key
        self.expension_matrix = expension_matrix
        self.perm_matrix = perm_matrix
        self.substitutions_matrix = substitutions_matrix

    def __call__(self, left, right):
        # 1 Expand
        e_right = self.expand(right)

        # 2 XOR
        new_block = ''
        for index in range(48):
            new_block += self.xor(e_right[index], self.key[index])

        print(new_block)

        # 3.1 Cut into 8 block 6 bits
        blocks_pair = [new_block[i:i + 6] for i in range(0, len(new_block), 6)]

        print('block pair', blocks_pair)

        # 3.2 Get numbers
        block_pair_str = ""
        for block_index in range(0, 8):
            block = blocks_pair[block_index]
            line_number = int(block[0] + block[5], 2)
            column_number = int(block[1:5], 2)
            substitution_matrix = self.substitutions_matrix[block_index]
            intersect = bin(substitution_matrix[line_number][column_number])[2:]
            for _ in range(len(intersect), 4):
                intersect = "0" + intersect
            print("intersect", intersect)
            block_pair_str += intersect

        # 4 Substitution matrix
        permutator = Permutator(offset=-1)
        print('block_pair_str', block_pair_str)
        substitution_numbers = permutator(block_pair_str, self.perm_matrix)

        # 5 XOR droite
        val = ''
        for i in range(32):
            val += self.xor(substitution_numbers[i], left[i])

        return right, val

    def expand(self, block):
        new_block = ''
        for index in range(48):
            position = int(self.expension_matrix[index])
            new_block += block[position]
        return new_block

    @staticmethod
    def xor(a, b):
        return "0" if a == b else "1"
