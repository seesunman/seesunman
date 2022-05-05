#!/usr/bin/python3
# 选出最小的数放到序列首部
def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if i != min_idx:
            seq[min_idx], seq[i] = seq[i], seq[min_idx]
import random
lst = list(range(10))
random.shuffle(lst)
print(lst)
select_sort(lst)
print(lst)
