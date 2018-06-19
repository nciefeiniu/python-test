#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
自动的切换协程
'''

import gevent

def test1():
    print('test1 is running')
    gevent.sleep(2)
    print('test1 is running again')

def test2():
    print('Now explicit context to test2')
    gevent.sleep(1)
    print('test2 is running again')

def test3():
    print('test3 is running')
    gevent.sleep(0)
    print('test3 is running again')

if __name__ == '__main__':
    gevent.joinall(
        [
            gevent.spawn(test1),
            gevent.spawn(test2),
            gevent.spawn(test3)
        ]
    )