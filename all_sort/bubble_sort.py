#!/usr/bin/python3

def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]

import random
lst = list(range(10))
random.shuffle(lst)
print(lst)
bubble_sort(lst)
print(lst)
