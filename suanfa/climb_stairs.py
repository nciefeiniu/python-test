#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = [0, 1, 2, 3]
        if n < 4:
            return temp[n]
        for i in range(4, n+1):
            temp.append(temp[i-1] + temp[i-2])
        return temp[n]


if __name__ == "__main__":
    s = Solution()
    print s.climbStairs(5)