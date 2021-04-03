def type_logger(func):
    def wrapper(*args):
        print(f'{func.__name__}({args[0]}: {type(args[0])}', end='')
        for i in args[1::]:
            print(f', {i}: {type(i)}', end='')
        print(')')
    return wrapper


@type_logger
def cube_q(a, b, c, d):
    print(a ** 3)


cube_q(5, 'a', True, 34.5)
