#!/usr/bin/python3
# -*- coding: utf-8 -*-

# def quick_sort(array, left, right):
#     if len(array) > 1:
#         pass
#
#
# def partition(array):
#     x = array[-1]
#     i = -1
#     for j in range(len(array) - 1):
#         if array[j] <= x:


def quick_sort(array, left, rigth):
    if left < rigth:
        q = partition(array, left, rigth)
        quick_sort(array, left, q - 1)
        quick_sort(array, q + 1, rigth)


def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


lists = [2,9,5,4,7,6,3,1]
quick_sort(lists,0, len(lists) - 1)
print(lists)