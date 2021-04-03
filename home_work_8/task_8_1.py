import re


def is_valid(str):
    if not re.match(r'^[A-Za-z][A-Za-z0-9_-]*@[A-Za-z][A-za-z0-9.]*.[A-Za-z]+$', str):
        raise ValueError(f'wrong email: {str}')
    result = re.split('@', str)
    dic = {'username': result[0], 'domain': result[1]}
    print(dic)


is_valid(input())
