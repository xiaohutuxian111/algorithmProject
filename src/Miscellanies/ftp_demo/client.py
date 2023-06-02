"""
@Author：stone
@Time：2023/6/2 10:48
@Description:
"""
import os.path
import socket
import json

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk.connect(('127.0.0.1', 8890))


def create_info_head(file_path:str)->dict:
    header_dict = {}
    if os.path.exists(file_path):
        header_dict['filename'] = os.path.basename(file_path)
        header_dict['size'] =  os.path.getsize(file_path)
    return  header_dict



header_dict = create_info_head('/data/aaa.pdf')
header_json =  json.dumps(header_dict)
header_bytes = header_json.encode('utf-8')
header_h =  bytes(str(len(header_bytes)),'utf-8').zfill(4)


sk.send(header_h)
sk.send(header_bytes)











if __name__ == '__main__':
    print(create_info_head('/data/aaa.pdf'))





