"""
@FileName：insert_sort.py
@Author：stone
@Time：2023/5/31 16:22
@Description:插入排序
"""
import random


def insert_sort(lis: list) -> list:
    n = len(lis)
    for i in range(1, n):
        x = lis[i]
        j = i - 1
        while j >= 0:
            if x < lis[j]:
                lis[j + 1] = lis[j]
                j -= 1
            else:
                break
        lis[j + 1] = x
        print(lis)
    return lis


if __name__ == '__main__':
    lis = [random.randint(0, 100) for _ in range(10)]
    print(insert_sort(lis))
