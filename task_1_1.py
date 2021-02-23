"""
Определяет количество лет, месяцев, дней, часо, минут, секунд по заданному количеству секунд
"""


# написал функцию для склонения единиц измерения, хотя в задании этого и не было, но подумал что будет неплохая практика
def dec(number, variable):
    if 10 < number % 100 < 20:
        return variable[2]
    elif number % 10 == 1:
        return variable[0]
    elif 1 < number % 10 < 5:
        return variable[1]
    else:
        return variable[2]


time = int(input("Введите количество секунд"))
words = [
    ['секунда', 'секунды', 'секунд'],
    ['минута', 'минуты', 'минут'],
    ['час', 'часа', 'часов'],
    ['день', 'дня', 'дней'],
    ['месяц', 'месяца', 'месяцев'],
    ['год', 'года', 'лет']
]
k = [60, 60, 24, 30, 12]
ans = []
for i in k:
    ans.append(time % i)
    time = time // i
    if time == 0:
        break
else:
    ans.append(time)

for i in range(len(ans)):
    print(f'{ans[i]} {dec(ans[i], words[i])}', end=' ')
