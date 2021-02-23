"""
По заданию не сказано, что B, C, D должны выводится как А. Но если это требуется то достаточно из А сделать функцию
"""
price = [10.8, 2569.78, 4.97, 5, 89.65, 536.25, 5.03, 59.24, 3.74, 1695.05, 0.9]
#A
for i in price[:-1:]:
    print(f'{int(i)} руб {int(i*100%100):02} коп', end=', ')
print(f'{int(price[-1])} руб {int(price[-1]*100%100):02} коп')
#B
print(sorted(price))
print(price)
#C
new_price = sorted(price, reverse=True)
print(new_price)
#D
print(new_price[4::-1])
