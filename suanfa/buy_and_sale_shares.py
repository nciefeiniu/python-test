#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
买卖股票两个题
1. 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

2.给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

"""


# 第一题
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            result = 0
            min_n = prices[0]
            for i in range(1, len(prices)):
                result = max(result, prices[i] - min_n)
                if prices[i] < min_n:
                    min_n = prices[i]
            return result
        else:
            return 0


# 第二题
class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for day in range(len(prices) - 1):
            if prices[day + 1] - prices[day] > 0:
                profit += prices[day + 1] - prices[day]
        return profit