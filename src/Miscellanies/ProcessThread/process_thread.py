"""
@Author：stone
@Time：2023/6/3 16:03
@Description:
"""
import os
from multiprocessing import Process





def func(name):
    print(os.getpid())
    print(f'{name}函数')






def run():
    lis = []
    for i in range(3):
        p = Process(target=func, kwargs={'name': f'哈哈{i}'})
        lis.append(p)
    for p in lis:
        p.start()


if __name__ == '__main__':
    run()
