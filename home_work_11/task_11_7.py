class Complex_number:
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'

    def __add__(self, other):
        return Complex_number(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex_number(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)


a = Complex_number(1, 2)
b = Complex_number(2, 3)
print(a + b)
print(a * b)
