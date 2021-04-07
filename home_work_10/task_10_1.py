from itertools import zip_longest


class Matrix:
    def __init__(self, mat):
        max_len = 0
        for i in mat:
            if len(i) > max_len:
                max_len = len(i)
        self.matrix = []
        for i in mat:
            self.matrix.append([lis for lis, loop in zip_longest(i, range(max_len), fillvalue=0)])

    def __add__(self, other):
        matrix = []
        for row1, row2 in zip_longest(self.matrix, other.matrix, fillvalue=list()):
            matrix.append(list())
            for i, j in zip_longest(row1, row2, fillvalue=0):
                matrix[-1].append(i + j)
        return Matrix(matrix)

    def __str__(self):
        r = []
        for i in self.matrix:
            r.append('  '.join(list(map(str, i))))
        return '\n'.join(r)


m1 = Matrix([[2, 2, 2], [3, 3, 3], [4, 4, 4, 5]])
m2 = Matrix([[2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]])
print(m2+m1)
