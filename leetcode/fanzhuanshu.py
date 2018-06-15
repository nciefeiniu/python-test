#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>2**31-1 or x<(-2)**31:
            return 0
        n_type = 0
        if x > 0:
            x = str(x)
        else:
            x = str(x * -1)
            n_type = -1

        result = x[::-1]
        if n_type == 0:
            print(int(result))
            return int(result)
        else:
            print(int(result) * -1)
            return int(result) * -1


if __name__ == '__main__':
    s = Solution()
    s.reverse(1534236469)