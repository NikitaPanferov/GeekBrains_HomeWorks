import os


def reform(str):
    return str.replace(' ', '').replace('|', '').replace('\n', '')


cur_lvl = []
with open('config.yaml', 'r', encoding='utf-8') as conf:
    for line in conf.readlines():
        if line.find('.') == -1:
            if line.count('  ') == len(cur_lvl):
                cur_lvl.append(reform(line))
                os.makedirs(os.path.join(*cur_lvl), exist_ok=True)
            else:
                cur_lvl = cur_lvl[:line.count('  ')]
                cur_lvl.append(reform(line))
                os.makedirs(os.path.join(*cur_lvl))
        else:
            open(os.path.join(*cur_lvl, reform(line)), 'w').close()
