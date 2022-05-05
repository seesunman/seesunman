#!/usr/bin/python3

def merge_sort(seq):
    if len(seq) < 2:
        return seq
    else:
        mid = int(len(seq) >> 1)
        left_sorted_list = merge_sort(seq[:mid])
        right_sorted_list = merge_sort(seq[mid:])
        new_list = merge_sorted_list(left_sorted_list, right_sorted_list)
        return new_list

def merge_sorted_list(sorted_a, sorted_b):
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_list = list()
    while a < length_a and b < length_b:
        if sorted_a[a] <= sorted_b[b]:
            new_list.append(sorted_a[a])
            a += 1
        else:
            new_list.append(sorted_b[b])
            b += 1
    while a < length_a:
        new_list.append(sorted_a[a])
        a += 1
    while b < length_b:
        new_list.append(sorted_b[b])
        b += 1
    return new_list
import random
lst =  list(range(100))
random.shuffle(lst)
new_lst = merge_sort(lst)
if new_lst == sorted(lst):
    print("True")
print(new_lst)
