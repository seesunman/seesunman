#!/usr/bin/python3
def select_sort(seq):
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
select_sort(lst)
print(lst)
