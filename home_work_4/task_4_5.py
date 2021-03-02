import requests
from datetime import date
import decimal
import sys


def currency_rates(val):
    val = f'<CharCode>{val.upper()}</CharCode>'

    xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    try:
        i = xml.text.index(val)
    except ValueError:
        return None
    index = xml.text[i::].index('<Value>') + 7 + i
    index2 = xml.text[index::].index('<') + index
    a = xml.text[index:index2]
    a = decimal.Decimal(a.replace(',', '.'))
    date_index = xml.text.index('Date="') + 6
    date_index2 = xml.text[date_index::].index('"') + date_index
    data_arr = list(map(int, xml.text[date_index:date_index2].split('.')))

    d = date(data_arr[2], data_arr[1], data_arr[0])
    return a, d

if __name__ == '__main__':
    print(*currency_rates(sys.argv[1]))
