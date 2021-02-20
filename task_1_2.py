"""
Так как задания по сути идентичные, то решил что использовать функцию будет удобнее. К тому же можно любое число
передавать для увеличения элементов списка.
"""


def summing(cub, plus):
    sum = 0
    for i in cub:
        temp_sum = 0
        temp_val = i + plus
        while temp_val > 0:
            temp_sum += temp_val % 10
            temp_val = temp_val // 10
        if temp_sum % 7 == 0:
            sum += i
    return sum


cubs = []
for i in range(1, 1000, 2):
    cubs.append(i ** 3)

print(summing(cubs, 0))

print(summing(cubs, 17))
