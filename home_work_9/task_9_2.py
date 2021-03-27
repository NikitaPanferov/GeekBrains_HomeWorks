class Road:

    __weight_for_square = 25
    __depth = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight_calc(self):
        return self.__length * self.__width * self.__weight_for_square * self.__depth


m1 = Road(5000, 20)
print(f'{m1.weight_calc()} kg')
