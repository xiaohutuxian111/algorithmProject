"""
@FileName：bubble_sort.py
@Author：stone
@Time：2023/5/31 15:30
@Description:冒泡排序
"""
import random


def bubble_sort(lis: list) -> list:
    size = len(lis)

    for i in range(size - 1, -1, -1):
        for j in range(0, i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
        print(lis)
    return lis


if __name__ == '__main__':
    lis = [random.randint(0, 100) for i in range(10)]
    print(bubble_sort(lis))
