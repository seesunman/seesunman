#!/usr/bin/python3
# 插入排序：使局部有序，将元素插入有序的序列里
def insert_sort(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and seq[pos-1] > value:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value
import random
lst = list(range(10))
random.shuffle(lst)
print(lst)
insert_sort(lst)
print(lst)
