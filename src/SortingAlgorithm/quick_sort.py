"""
@Author：stone
@Time：2023/5/31 17:25
@Descriptio:快排
"""
import random


def quick_sort_pivot(lis, start, end):
    pivot = start
    j = start + 1
    for i in range(start + 1, end + 1):
        if lis[i] < lis[pivot]:
            lis[i], lis[j] = lis[j], lis[i]
            j += 1
    lis[pivot], lis[j - 1] = lis[j - 1], lis[pivot]
    pivot = j - 1
    print(lis[pivot], lis[start:pivot], lis[pivot + 1:end + 1])
    return pivot


def quick_sort(lis: list, start: int, end: int):
    if start >= end:
        return
    pivot = quick_sort_pivot(lis, start, end)
    quick_sort(lis, start, pivot - 1)
    quick_sort(lis, pivot + 1, end)


if __name__ == '__main__':
    lis = [random.randint(0, 100) for _ in range(10)]
    print(quick_sort(lis, 0, 9))
    print(lis)
