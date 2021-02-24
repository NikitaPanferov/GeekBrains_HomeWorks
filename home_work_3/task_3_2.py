def num_translate_adv(word):

    if not isinstance(word, str):
        return None

    is_up = word.istitle()
    word = word.lower()

    if word == 'one':
        word = 'один'
    elif word == "two":
        word = 'два'
    elif word == 'three':
        word = 'три'
    elif word == 'four':
        word = 'четыре'
    elif word == 'five':
        word = 'пять'
    elif word == 'six':
        word = 'шесть'
    elif word == 'seven':
        word = 'семь'
    elif word == 'eight':
        word = 'восемь'
    elif word == 'nine':
        word = 'девять'
    elif word == 'ten':
        word = 'десять'
    elif word == 'zero':
        word = 'нуль'
    else:
        return None

    if is_up:
        return word.capitalize()

    return word


if __name__ == '__main__':
    print(num_translate_adv(input('Введите числительное на английском: ')))
