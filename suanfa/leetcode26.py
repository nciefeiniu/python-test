# -*- coding: utf-8 -*-


def remove_duplicates(nums):
    length = len(nums)
    if length < 2:
        return length
    index_m = 0
    index_n = 1
    while index_n < length:
        if nums[index_n] != nums[index_m]:
            index_m += 1
            nums[index_n], nums[index_m] = nums[index_m], nums[index_n]
        index_n += 1
    return index_m + 1


if __name__ == "__main__":
    test = [1, 1, 2]
    print remove_duplicates(test)
    print test
