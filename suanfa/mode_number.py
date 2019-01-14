# -*- coding: utf-8 -*-


def get_mode_number(nums):
    result, count = 0, 0
    for num in nums:
        if result == num:
            count += 1
        else:
            count -= 1
        if count < 0:
            result = num
            count = 0
    return result


if __name__ == '__main__':
    nums = [3,3,4,4,4]
    print get_mode_number(nums)