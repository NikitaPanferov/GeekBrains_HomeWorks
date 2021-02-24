"""
Сможете ли вы вернуть отсортированный по ключам словарь?
-Отсортированный словарь быть не может, так как словарь - неизменяемый тип данных
"""
def thesaurus_adv(*args):
    args = list(map(str.title, args))  # Если вдруг напишут с маленькой буквы
    args = list(map(str.split, args))

    stuff_dict = {a[1][0]: {} for a in args}

    for el in args:
        if el[0][0] in stuff_dict[el[1][0]].keys():
            stuff_dict[el[1][0]][el[0][0]].append(' '.join(el))
        else:
            stuff_dict[el[1][0]][el[0][0]] = [' '.join(el)]

    return stuff_dict


if __name__ == '__main__':
    stuff = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

    for surname, name in sorted(stuff.items()):#Красивый вывод в алфовитном порядке
        print(surname)
        for key, item in sorted(name.items()):
            print(f'\t{key}: {sorted(item)}')
