"""
@Author：stone
@Time：2023/5/31 17:07
@Description:计数排序
"""
import random


def counting_sort(lis: list) -> list:
    count_len = max(lis) + 1
    cnt = [0] * count_len
    for val in lis:
        cnt[val] += 1
    print(cnt)

    n = 0
    for val in range(0, count_len):
        while cnt[val] > 0:
            cnt[val] -= 1
            lis[n] = val
            n +=1
    return lis
if __name__ == '__main__':
    lis = [random.randint(0, 100) for i in range(10)]
    print(counting_sort(lis))