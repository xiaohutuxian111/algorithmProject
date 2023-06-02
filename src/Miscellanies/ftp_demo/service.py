"""
@Author：stone
@Time：2023/6/2 10:47
@Description:
"""

import socket
import json

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk.bind(('127.0.0.1', 8890))
sk.listen(5)
while True:
    conn, addr = sk.accept()
    header_size = int(conn.recv(4).decode('utf-8'))
    print(header_size)
    header_info = json.loads(conn.recv(header_size).decode('utf-8'))
    print(header_info)
    filename = header_info['filename']
    filesize = header_info['size']
    res = b''
    count = 0
    with open(filename, 'wb') as f:
        if count < filesize:
            content_data = conn.recv(1024)
            count += len(content_data)
            res += content_data
        f.write(res)
