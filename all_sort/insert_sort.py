#!/usr/bin/python3

def insert_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[min_idx], seq[i] = seq[i], seq[min_idx]

import random
lst = list(range(10))
random.shuffle(lst)
print(lst)
insert_sort(lst)
print(lst)
