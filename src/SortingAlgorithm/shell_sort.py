"""
@Author：stone
@Time：2023/5/31 17:37
@Description:希尔排序
"""
import random


def shell_sort(lis: list) -> list:
    n = len(lis)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            x = lis[i]
            j = i
            while j >= gap:
                if x < lis[j - gap]:
                    lis[j] = lis[j - gap]
                else:
                    break
                j -= gap
            lis[j] = x
        print(lis)
        gap = gap // 2

    return lis


if __name__ == '__main__':
    lis = [random.randint(0, 100) for _ in range(10)]
    print(shell_sort(lis))
