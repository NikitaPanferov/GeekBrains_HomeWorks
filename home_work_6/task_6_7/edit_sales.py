import sys
FIX_MAX_LEN = 16
with open('bakery.csv', 'r+', encoding='utf-8') as file:
    file.seek((FIX_MAX_LEN + 1) * (int(sys.argv[1]) - 1))
    print(file.tell())
    file.write(f'{sys.argv[2]}{" " * (FIX_MAX_LEN - len(sys.argv[2]) -1)}\n')
exit(0)
