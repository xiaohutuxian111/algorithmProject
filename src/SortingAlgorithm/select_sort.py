"""
@FileName：select_sort.py
@Author：stone
@Time：2023/5/31 15:54
@Description:选择排序
"""
import random


from typing import List


def select_sort(lis: List) -> List:
    size: int = len(lis)
    for i in range(size - 1):
        # 找到最小的数的坐标
        min_index = i
        for j in range(i + 1, size):
            if lis[min_index] > lis[j]:
                min_index = j

        lis[i], lis[min_index] = lis[min_index], lis[i]
        print(lis)
    return lis


if __name__ == '__main__':
    lis = [random.randint(0, 100) for _ in range(10)]
    print(select_sort(lis))

