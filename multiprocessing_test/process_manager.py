#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
进程之间通过Manager 实现数据共享
'''

from multiprocessing import Process, Manager
import os

def test(dicts, lists):
    dicts['pid'] = os.getpid()
    lists.append(os.getpid())

if __name__ == '__main__':
    with Manager() as manager:
        # 生成一个可在多进程之间传递和共享信息的字典
        m_dic = manager.dict()
        # 生成一个可在多进程之间传递和共享信息的列表
        m_list = manager.list()

        # 多进程
        process_lists = []
        for i in range(10):
            p = Process(target=test, args=(m_dic, m_list))
            p.start()
            process_lists.append(p)
        # 主进程等待子进程运行结束
        for p in process_lists:
            p.join()

        print(m_dic)
        print(m_list)