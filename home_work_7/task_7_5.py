import json
import os

folder_name = input('Введите имя папки: ')
files_dict = {
    100: [0, set()],
    1000: [0, set()],
    10000: [0, set()],
    100000: [0, set()]
}
if not os.path.exists(folder_name):
    print('Такой папки не существует')
    exit(-1)

for root, dirs, files in os.walk(folder_name, topdown=False):
    for name in files:
        size = os.stat(os.path.join(root, name)).st_size
        for sizes in files_dict:
            if size < sizes:
                files_dict[sizes][0] += 1
                files_dict[sizes][1].add(name[name.rfind('.')+1::])
                break

for i in files_dict:
    files_dict[i][1] = list(files_dict[i][1])
    files_dict[i] = tuple(files_dict[i])

with open(f'{folder_name}_summary.json', 'w') as f:
    json.dump(files_dict, f)
