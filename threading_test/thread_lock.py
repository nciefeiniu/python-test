#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time

number = 0
# 线程锁
lock = threading.Lock()

def run(n):
    lock.acquire()
    global number
    number += 1
    lock.release()

if __name__ == '__main__':
    thr_lists = []
    for i in range(10):
        t = threading.Thread(target=run, args=('t-%s' % i,))
        t.start()
        thr_lists.append(t)
    for th in thr_lists:
        t.join()

    print(number)
