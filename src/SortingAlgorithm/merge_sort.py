"""
@Author：stone
@Time：2023/5/31 16:28
@Description:归并排序 分治的思想
"""
import random


def merge(a, start, mid, end):
    tmp = []
    l = start
    r = mid + 1
    # 对两个数组按照顺序添加
    while l <= mid and r <= end:
        if a[l] <= a[r]:
            tmp.append(a[l])
            l += 1
        else:
            tmp.append(a[r])
            r += 1
    tmp.extend(a[l:mid + 1])
    tmp.extend(a[r:end + 1])
    # 将临时数组中的数据添加到列表
    for i in range(start, end + 1):
        a[i] = tmp[i - start]
    print(start, end, tmp)


def merge_sort(lis: list, start: int, end: int) -> list:
    if start == end:
        return
    mid = (end - start) // 2 + start
    merge_sort(lis, start, mid)
    merge_sort(lis, mid + 1, end)
    merge(lis, start, mid, end)


if __name__ == '__main__':
    lis = [random.randint(0, 20) for _ in range(10)]
    merge_sort(lis, 0, 9)
