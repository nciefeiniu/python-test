#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
进程之间通信，Queue
'''

from multiprocessing import Process, Queue

def test(qq):
    qq.put(['test','123'])
    print('test')

if __name__ == '__main__':
    # 这是进程的queue，不是线程中的queue
    # 这里的q是通过克隆传递的，父进程克隆q，给子进程
    q = Queue()
    p = Process(target=test, args=(q,))
    p.start()

    print(q.get())
    p.join()
