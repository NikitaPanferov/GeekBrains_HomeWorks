"""
Написал два генератора, первый через проверку if, а второй через try-except
"""
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def tup_gen(tut, klass):
    for i in range(0, len(tut)):
        if len(klass) < i + 1:
            yield tut[i], None
        else:
            yield tut[i], klass[i]


def tup_gen_2(tut, klass):
    for i in range(0, len(tut)):
        try:
            yield tut[i], klass[i]
        except IndexError:
            yield tut[i], None


a = tup_gen_2(tutors, klasses)
print(*a)
