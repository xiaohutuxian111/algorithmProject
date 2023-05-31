"""
@Author：stone
@Time：2023/5/31 16:50
@Description:桶排序
"""
import random


def select_sort(lis: list) -> list:
    n = len(lis)
    for i in range(n - 1):
        min = i
        for j in range(i, n):
            if lis[min] > lis[j]:
                min = j
        lis[min], lis[i] = lis[i], lis[min]
        print(lis)
    return lis


def bucket_sort(lis: list) -> list:
    minv = min(lis)
    maxv = max(lis)
    bucket_count = 3
    bucket = [[] for _ in range(bucket_count)]
    pre_bucket = (maxv - minv + bucket_count) // bucket_count

    for num in lis:
        bucket_index = (num - minv) // pre_bucket
        bucket[bucket_index].append(num)

    for i in range(bucket_count):
        select_sort(bucket[i])

    idx = 0
    for i in range(bucket_count):
        for v in bucket[i]:
            lis[idx] = v
            idx += 1
    print(bucket)
    print(lis)


if __name__ == '__main__':
    lis = [random.randint(0, 100) for i in range(10)]
    print(bucket_sort(lis))
