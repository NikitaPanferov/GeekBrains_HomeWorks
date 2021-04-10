class ZeroDivision(Exception):
    def __init__(self, msg='Нельзя делить на 0'):
        super().__init__(msg)


def division(a, b):
    try:
        if b == 0:
            raise ZeroDivision
        else:
            print(a / b)
    except ZeroDivision as err:
        print(err)


division(int(input('Введите делитель: ')), int(input('Введите делимое: ')))
