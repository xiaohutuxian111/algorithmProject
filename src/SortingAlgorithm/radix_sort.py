"""
@Author：stone
@Time：2023/5/31 17:16
@Description:基数排序
"""
import random


def radix_sort(lis: list) -> list:
    base = 1
    maxv = max(lis)
    while base < maxv:
        bucket = []
        for idx in range(10):
            bucket.append([])
        for num in lis:
            idx = num // base % 10
            bucket[idx].append(num)
        l = 0
        for idx in range(10):
            for v in bucket[idx]:
                lis[l] = v
                l += 1
        print(lis)
        base *= 10
    return lis



if __name__ == '__main__':
    lis = [random.randint(0, 100) for _ in range(10)]
    print(radix_sort(lis))
