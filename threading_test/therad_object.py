#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name):
        # 调用父类的构造方法
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print('Threading %s is running' % self.name)
        time.sleep(5)

# # 这种方式无意义，相当于单线程
# for i in range(50):
#     t = MyThread('t-%s' % str(i+1))
#     t.start()
#     # 等待这个线程执行完毕，程序再继续往下走
#     t.join()
# print('over')

# 并发，且主线程等待子线程结束再结束
start_time = time.time()
thread_lists = []
for i in range(50):
    t = MyThread('t-%s' %i)
    t.start()
    thread_lists.append(t)
print(thread_lists)
for m in thread_lists:
    print(m)
    m.join()
print('over')
print(time.time()-start_time)