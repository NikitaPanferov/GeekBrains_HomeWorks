def num_translate_adv(word):
    if not isinstance(word, str):
        return None

    is_up = word.istitle()
    word = word.lower()
    if not (word in word_dict.keys()):
        return None
    if is_up:
        return word_dict[word].capitalize()

    return word_dict[word]


word_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'

}

if __name__ == '__main__':
    print(num_translate_adv(input('Введите числительное на английском: ')))
