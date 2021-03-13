def parse(file):
    with open(file, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            line_splited = line.split(' ')
            remote_addr = line_splited[0]
            request_type = line_splited[5][1::]
            requested_resource = line_splited[6]
            line = f.readline()
            yield remote_addr, request_type, requested_resource


print(*parse('nginx_logs.txt'))
