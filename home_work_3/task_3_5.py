from random import sample, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=False):
    """
    всего уникальных слов 5 для каждой позиции, поэтому максимум без повторений 5 шуток
    :param n: количество шуток
    :param flag(не обязательный, по умолчанию False: True если хотите чтобы слова не повторялись
    :return: список шуток типа str
    """
    if flag:
        if n > 5:
            print('Так как в списках по пять слов, я могу сгенерировать без повторения всего пять шуток!')
            n = 5
        nou = sample(nouns, n)
        adv = sample(adverbs, n)
        adj = sample(adjectives, n)
    else:
        nou = [choice(nouns) for i in range(n)]
        adv = [choice(adverbs) for i in range(n)]
        adj = [choice(adjectives) for i in range(n)]

    return list(map(' '.join, [[a, b, c] for a, b, c in zip(nou, adv, adj)]))


if __name__ == '__main__':
    print(get_jokes(4, True))
