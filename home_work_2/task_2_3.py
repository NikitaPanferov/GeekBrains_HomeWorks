"""
Постарался сделать максимально по заданию. Хотел сделать через for, но в нём нельзя изменять счётчик. Создание строки
хотел сделать через join, но тогда кавычки были бы через пробел от числа. Можно было бы в разы уменьшить код
если бы кавычки можно было бы писать в одной строке с числом ('"5"').
Под основным кодом оставляю код, удовлетворяющий условию написанному выше
"""
begin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(begin_list):
    if '+' in begin_list[i] or '-' in begin_list[i]:
        if len(begin_list[i]) == 2:
            begin_list[i] = f'{begin_list[i][0]}{int(begin_list[i][1]):02d}'
    elif begin_list[i].isdigit():
        if len(begin_list[i]) == 1:
            begin_list[i] = f'{int(begin_list[i][0]):02d}'
    else:
        i += 1
        continue
    begin_list.insert(i, '"')
    i += 2
    begin_list.insert(i, '"')
    i += 1

alf = '1234567890+-'
js = begin_list[0]
for i in range(1, len(begin_list)):
    if (begin_list[i-1] == '"' and begin_list[i][0] in alf) or (begin_list[i-1][0] in alf and begin_list[i] == '"'):
        js += begin_list[i]
    else:
        js += ' ' + begin_list[i]
print(js)

"""
begin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(begin_list)):
    if begin_list[i][0] == '+' or begin_list[i][0] == '-':
        if len(begin_list[i]) > 1:
            begin_list[i] = f'"{begin_list[i][0]}{int(begin_list[i][1]):02d}"'
    if begin_list[i].isdigit():
        begin_list[i] = f'"{int(begin_list[i]):02d}"'
js = ' '.join(begin_list)
print(js)
"""