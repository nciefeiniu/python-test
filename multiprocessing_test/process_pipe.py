#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
进程通信，管道pipe
这只是进程的信息传递，还没共享
'''

from multiprocessing import Process, Pipe

def test(conn):
    conn.send('message from chid')
    print(conn.recv())

if __name__ == '__main__':
    # 创建管道，会返回两个节点，相当于电话线，每一端都可以发送接受
    parent_conn, child_conn = Pipe()
    p = Process(target=test, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send('200 OK')