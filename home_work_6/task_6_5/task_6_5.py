from itertools import zip_longest
import argparse


parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('file1', type=str, help='file with users')
parser.add_argument('file2', type=str, help='file with hobby')
parser.add_argument('out_file', type=str, help='output file')
args = parser.parse_args()


def parser(file):
    with open(file, 'r', encoding='utf-8') as f:
        line = f.readline().replace('\r', '').replace('\n', '')
        while line:
            yield line
            line = f.readline().replace('\r', '').replace('\n', '')

users = parser(args.file1)
hobby = parser(args.file2)
data_file = open(args.out_file, 'w', encoding='utf-8')
for u, h in zip_longest(users, hobby):
    if u:
        data_file.write(f'{u}: {h}\n')
    else:
        exit(1)
data_file.close()
exit(0)
# with open('output.txt', 'wb') as out:
#     pickle.dump(data, out)

