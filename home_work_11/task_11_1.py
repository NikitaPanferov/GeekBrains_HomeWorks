import re


class Data:
    max_day = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, str_data):

        self.str_data = re.findall(r'^\d+-\d+-\d+$', str_data)
        if not self.str_data:
            raise Exception('Неверная дата (ДД-ММ-ГГ или ДД-ММ-ГГГГ)')
        self.str_data = self.str_data[0]

    @classmethod
    def to_int_data(cls, data):
        data_list = re.split('-', cls(data).str_data)

        return tuple(map(int, data_list))

    @staticmethod
    def is_valid(data):
        data_tup = Data.to_int_data(data)
        return 0 < data_tup[1] <= 12 and data_tup[0] <= Data.max_day[data_tup[1]] and data_tup[2] > 0


print(Data.is_valid('066-55-22'))
print(Data.is_valid('66-55-22'))
print(Data.is_valid('030-03-22'))