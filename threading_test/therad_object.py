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
        print('%s over' % self.name)


if __name__ =='__main__':
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
        # 设置为守护线程，主线程退出不等待守护线程，只等待非守护线程结束(即，主线程退出，守护线程也跟着全部退出)
        t.setDaemon(True)
        # 运行进程
        t.start()
        thread_lists.append(t)

    # for m in thread_lists:
    #     m.join()
    print('over')
    print(time.time()-start_time)