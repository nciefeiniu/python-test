#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

def timer(func):
    def warpper(*arg, **kwargs):
        start_time = time.time()
        print()
        func()
        stop_time = time.time()
        print('这个方法运行了：%s' % (stop_time - start_time))
    return warpper

@timer
def test1(name):
    time.sleep(3)
    print('测试')


test1('liutao')