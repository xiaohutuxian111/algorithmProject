"""
@Author：stone
@Time：2023/6/2 10:47
@Description:
"""
import os.path
import socket
import json





def service_mian():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sk.bind(('192.168.116.104', 8001))
    sk.listen(5)
    while True:
        conn, addr = sk.accept()
        comment =  conn.recv(4).decode('utf-8').split('0')[-1]
        print(comment)
        if  comment == 'put':
            upload_file(conn)



def execute_command(conn):
    command = conn.recv(4).decode('utf-8')
    print(command)




def upload_file(conn):
    header_size = conn.recv(4).decode('utf-8')
    header_info = json.loads(conn.recv(int(header_size)).decode('utf-8'))
    filename = header_info['filename']
    filesize = header_info['size']
    res = b''
    count = 0
    print(header_info)
    with open(filename, 'wb') as f:
        if count < filesize:
            content_data = conn.recv(1024)
            count += len(content_data)
            f.write(content_data)
            res += content_data
    if os.path.getsize(filename) == filesize:
        print("传输完成")
    conn.close()





if __name__ == '__main__':
    service_mian()