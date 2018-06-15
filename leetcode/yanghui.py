#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            if i == 0:
                lists = [1]
            else:
                lists = [1]
                for j in range(1, i):
                    lists += [result[i - 1][j - 1] + result[i - 1][j]]
                lists += [1]
            result.append(lists)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.generate(10))