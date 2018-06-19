#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
进程池
'''

from multiprocessing import Pool
import time

def test(num):
    time.sleep(2)
    print('This is process-%s' % num)

def test2(num):
    print('process-%s over' % num)

if __name__ == '__main__':
    # 创建一个池
    pool = Pool(3)
    for i in range(10):
        # 异步执行，相当于并行. callback是回调函数
        pool.apply_async(func=test, args=(i,), callback=test2)
        # 同步执行,相当于串行
        # pool.apply(func=test, args=(i,))

    pool.close()
    pool.join()

