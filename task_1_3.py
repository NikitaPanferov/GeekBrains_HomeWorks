num = int(input("Введите число"))


def dec(number):
    if number == 1:
        print(number, 'процент')
    elif 1 < number < 5:
        print(number, 'процента')
    else:
        print(number, 'процентов')


dec(num)
print('\n\nдля проверки \n-------------------')
for i in range(21):
    dec(i)
