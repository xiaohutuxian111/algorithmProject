"""
@Author：stone
@Time：2023/6/5 9:32
@Description:
"""
import os
from multiprocessing import Queue, Process


def producer(q: Queue, name: str):
    print(f'{name}做出了{os.getpid()}')
    q.put(name)


def consumer(q: Queue, name: str):
    t = q.get()
    print(f'{name}吃掉了{t}')


def run():
    num = os.cpu_count()
    q = Queue()
    lis = []
    for i in range(num):
        p = Process(target=producer, args=(q, f'生产者{i}',))
        p1 = Process(target=consumer, args=(q, f'消费者{i}',))

        lis.append(p)
        p.start()
        p1.start()
    for p in lis:
        p.join()

if __name__ == '__main__':
    run()