# -*- coding: utf-8 -*-


def merge_array(arr1, arr2, n):
    """
    arr1的长度等于两个列表中数据的总和
    ex: arr1 = [1, 3, 4, 0, 0, 0]
        arr2 = [2, 3, 6]
        return [1, 2, 3, 3, 4, 6]
    :param arr1: list
    :param arr2: list
    :param n: number arr1中有效数据的个数
    :return: arr1
    """
    if len(arr2) == 0:
        return arr1
    if len(arr2) + n > len(arr1):
        raise RuntimeError('Insufficient space')
    index1, index2 = n - 1, len(arr2) - 1
    index_r = len(arr1) - 1
    while index1 > -1 and index2 > -1:
        if arr1[index1] <= arr2[index2]:
            arr1[index_r] = arr2[index2]
            index2 -= 1
        else:
            arr1[index_r], arr1[index1] = arr1[index1], 0
            index1 -= 1
        index_r -= 1
    return arr1


if __name__ == '__main__':
    a1 = [1, 2, 5, 0, 0, 0]
    a2 = [1, 3, 4]
    print merge_array(a1, a2, 3)