class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        sub = self.count - other.count
        if sub < 0:
            print('Ошибка, полученое  количество клеток меньше нуля')
        else:
            return Cell(sub)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __floordiv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, n):
        count_of_rows = self.count // n
        last_row = self.count - count_of_rows * n
        f = '\n'.join([''.join(['*' for i in range(n)]) for j in range(count_of_rows)])
        if last_row:
            f += f"\n{''.join(['*' for i in range(last_row)])}"
        return f


c1 = Cell(10)
c2 = Cell(3)
print((c1+c2).count)
print((c1-c2).count)
print((c1*c2).count)
print((c1//c2).count)
print(c1.make_order(3))
