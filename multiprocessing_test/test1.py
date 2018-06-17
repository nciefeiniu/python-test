#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
import time
import threading
import os

def thread_test():
    print('this is thread')
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print(name)
    print('============%s============' )
    print('parent pid:%s' % os.getppid())
    print('current pid: %s' % os.getpid())
    # 在进程中启动线程
    t = threading.Thread(target=thread_test,)
    t.start()

if __name__ == '__main__':
    # 启动进程
    # p = Process(target=run, args=('p1',))
    # p.start()

    # 多进程
    for i in range(10):
        p = Process(target=run, args=('p-%s' % i,))
        p.start()


