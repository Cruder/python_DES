class Permutator:
    def __init__(self, offset=0):
        self.offset = offset

    def __call__(self, data, matrix):
        new_data = ''
        for index in range(len(matrix)):
            position = int(matrix[index]) + self.offset
            new_data += data[position]
        return new_data
