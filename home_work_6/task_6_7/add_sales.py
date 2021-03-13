import sys
FIX_MAX_LEN = 16
with open('bakery.csv', 'a', encoding='utf-8') as file:
    file.write(f'{sys.argv[1]}{" " * (FIX_MAX_LEN - len(sys.argv[1]) - 1)}\n')
exit(0)
