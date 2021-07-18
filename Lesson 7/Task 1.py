class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        beauty_matrix = []
        for row in self.matrix:
            beauty_matrix.append(' '.join([f'{item:>4}' for item in row]))
        return '\n'.join(beauty_matrix)

    def __add__(self, other):
        result_list = []
        if len(self.matrix) != len(other.matrix):
            print('Размер матриц не совпадает!')
            return None
        for self_row, other_row in zip(self.matrix, other.matrix):
            if len(self_row) != len(other_row):
                print('Размер матриц не совпадает!')
                return None
            result_list.append([x + y for x, y in zip(self_row, other_row)])
        return Matrix(result_list)


m1 = Matrix([[1, 267], [3, 5], [768, 2]])
m2 = Matrix([[2, 4], [5, 78], [0, 7]])
print(m1 + m2)
