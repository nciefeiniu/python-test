#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
greentlet是协程，但是是手动切换
'''

from greenlet import greenlet


def test1():
    print('1')
    gr2.switch()
    print(2)
    gr2.switch()

def test2():
    print('3')
    gr1.switch()
    print(4)

if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()