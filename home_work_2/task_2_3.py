"""
Постарался сделать максимально по заданию. Хотел сделать через for, но в нём нельзя изменять счётчик. Создание строки
хотел сделать через join, но тогда кавычки были бы через пробел от числа. Можно было бы в разы уменьшить код
если бы кавычки можно было бы писать в одной строке с числом ('"5"').
Под основным кодом оставляю код, удовлетворяющий условию написанному выше
"""
begin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, el in reversed(list(enumerate(begin_list))):
    el = el.replace('+' or '-', '')
    if el.isdigit():
        begin_list.insert(i + 1, '"')
        begin_list[i] = begin_list[i].replace(el, f'{int(el):02}')
        begin_list.insert(i, '"')

js = ' '.join(begin_list)
js = js.split('"')
for i in range(1, len(js), 2):
    js[i] = js[i].replace(' ', '"')
js = ''.join(js)
print(js)


