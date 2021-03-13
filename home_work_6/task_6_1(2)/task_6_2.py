def parse(file):
    with open(file, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            line_splited = line.split(' ')
            remote_addr = line_splited[0]
            line = f.readline()
            yield remote_addr


addr_gen = parse('nginx_logs.txt')
req_counter = {}
max = ['',0]
for addr in addr_gen:
    if addr in req_counter:
        req_counter[addr] += 1
    else:
        req_counter[addr] = 1
    if req_counter[addr] > max[1]:
        max = [addr, req_counter[addr]]
    elif req_counter[addr] == max[1]:
        max.append([addr, req_counter[addr]])

print(*max)
