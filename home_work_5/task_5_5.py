src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
"""
вариант через try-except
uniq = set()
for i in src:
    try:
        uniq.remove(i)
    except KeyError:
        uniq.add(i)

for i in src:
    if i in uniq:
        print(i, end=' ')
"""


uniq = set()
for i in src:
    if i in uniq:
        uniq.discard(i)
    else:
        uniq.add(i)

for i in src:
    if i in uniq:
        print(i, end=' ')

