#!/usr/bin/python3
# -*- coding: utf-8 -*-


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
        print array
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def doit(lists, left, right):
    _base_num = left
    _base = lists[_base_num]
    while right != left:
        while right != left and lists[right] >= _base:
            right -= 1
        while right != left and lists[left] <= _base:
            left += 1
        # print left, right
        lists[left], lists[right] = lists[right], lists[left]

    lists[left], lists[_base_num] = lists[_base_num], lists[left]
    print lists
    return left


def quick_sort2(inputs, l, r):
    if l < r:
        q = doit(inputs, l, r)
        quick_sort2(inputs, l, q-1)
        quick_sort(inputs, q+1, r)


if __name__ == '__main__':
    # lists = [2,9,5,9,4,7,1,5,4]
    # quick_sort(lists,0, len(lists) - 1)
    # print(lists)

    lists2 = [1,1]
    quick_sort2(lists2, 0, len(lists2) - 1)
    print lists2