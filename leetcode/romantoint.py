#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        date = s
        info = {'IV': 4, 'IX':9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
