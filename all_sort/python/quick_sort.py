#!/usr/bin/python3

def quick_sort(seq):
    if len(seq) < 2:
        return seq
    pivot_index = 0
    pivot = seq[pivot_index]
    less_part = [x for x in seq[pivot_index+1:] if x <= pivot]
    great_part = [x for x in seq[pivot_index+1:] if x > pivot]
    return quick_sort(less_part) + [pivot] + quick_sort(great_part)
import random
lst = list(range(100))
random.shuffle(lst)
if quick_sort(lst) == sorted(lst):
    print("True")
