"""
@Author：stone
@Time：2023/6/2 10:48
@Description:
"""
import os.path
import socket
import json


def client_main():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('192.168.116.104', 8001))
    return sk



def upload_file(sk: socket, file_path: str):
    header_dict = {'filename': os.path.basename(file_path), 'size': os.path.getsize(file_path)}
    header_json = json.dumps(header_dict)
    header_bytes = header_json.encode('utf-8')
    header_h = bytes(str(len(header_bytes)), 'utf-8').zfill(4)
    sk.send(header_h)
    sk.send(header_bytes)
    count = 0
    with open(file_path, 'rb') as f:
        while count < header_dict['size']:
            data = f.read(1024)
            n = len(data)
            sk.send(data)
            count += n
            print('已上传的字符:{}'.format(count))







def comments_init():
    sk = client_main()
    while True:
        comm = input("请输入要执行的命令:").strip()
        commend = comm.split(' ')[0].strip().lower()
        # 发送命令
        commend_data = commend.encode('utf-8').zfill(4)
        sk.send(commend_data)
        if commend == 'ls':
           pass
        elif commend == 'put':
            file_path = comm.split(' ')[-1]
            if not os.path.exists(file_path):
                print("要上传的文件: {} 不存在,请重新输入命令".format(file_path))
                break
            upload_file(sk, file_path)
        elif commend == 'get':
            pass
        elif commend == 'pwd':
            pass


if __name__ == '__main__':
    comments_init()
