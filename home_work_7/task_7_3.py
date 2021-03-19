import os, shutil

gen = os.walk('my_project')
print(os.getcwdb())
os.makedirs(os.path.join('my_project', 'templates'), exist_ok=True)
for tup in gen:
    if tup[0].endswith('templates') and not tup[0].endswith(os.path.join('my_project', 'templates')):
        for dir in tup[1]:
            try:
                shutil.copytree(os.path.join(tup[0], dir), os.path.join('my_project', 'templates', dir))
            except FileExistsError as e:
                print(e)
