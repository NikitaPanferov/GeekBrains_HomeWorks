import sys
from itertools import islice


with open('bakery.csv', encoding='utf-8') as file:
    if len(sys.argv) == 1:
        print(file.read())
    elif len(sys.argv) == 2:
        line_iter = islice(file, 30 - 1, None)
        for i in line_iter:
            print(i.replace('\n', ''))
    else:
        line_iter = islice(file, int(sys.argv[1]) - 1, int(sys.argv[2]))
        for i in line_iter:
            print(i.replace('\n', ''))

exit(0)
