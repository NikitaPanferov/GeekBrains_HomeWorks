def val_checker(callback):
    def _val_checker(func):
        def wrapper(arg):
            if not callback(arg):
                raise ValueError(f'wrong val {arg}')
            return func(arg)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


print(calc_cube(3))
