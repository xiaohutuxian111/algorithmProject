"""
@Author：stone
@Time：2023/5/31 17:43
@Description:堆排序
"""
import random


def max_heapify(heap, start, end):
    son = start * 2
    while son <= end:
        if son + 1 <= end and heap[son + 1] > heap[son]:
            son += 1
        if heap[son] > heap[start]:
            heap[start], heap[son] = heap[son], heap[start]
            start, son = son, son * 2
        else:
            break


def heap_sort(lis: list) -> list:
    heap = [None] + lis
    root = 1
    l = len(heap)
    for i in range(l // 2, root - 1, -1):
        max_heapify(heap, i, l - 1)
    for i in range(l - 1, root, -1):
        heap[i], heap[root] = heap[root], heap[i]
        max_heapify(heap, root, i - 1)
    return heap[root:]


if __name__ == '__main__':
    lis = [random.randint(0, 100) for _ in range(10)]
    print(heap_sort(lis))
