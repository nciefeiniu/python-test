#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        result = dict()
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        for v in result.values():
            if v > 1:
                return True

        return False


if __name__ == "__main__":
    test = [1, 2, 3, 4, 1]
    s = Solution()
    print s.containsDuplicate(test)