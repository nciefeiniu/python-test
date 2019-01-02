#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
auther: nicefeiniu
selectors是封装好了的IO多路复用
selectors.DefaultSelector会自动选择是用select还是epool
windows不支持epool，所以用的是select
'''

import selectors
import socket

host, port = '127.0.0.1', 9999

# 创建一个selectors
sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print('accepted', conn, 'from:', addr)
    # 把socket设置为非阻塞
    conn.setblocking(False)
    # 注册一个文件对象进行选择，监视它以查找i/o事件。
    sel.register(conn, selectors.EVENT_READ, asmsg)

def asmsg(conn, mask):
    try:
        data = conn.recv(1024)
        print(data)
        conn.send(data)
    except Exception as e:
        print(e)
        sel.unregister(conn)

def servers():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(1024)
        server.setblocking(False)
        # print(server)
        # accept是回调函数，就是有活动的链接（即有新的链接连接进来的时候）就调用accept这个方法

        sel.register(server, selectors.EVENT_READ, accept)
        while True:
            # 默认阻塞的，有活动链接连接，就返回活动的连接列表
            try:
                events = sel.select()
                print(events)
                for key, mask, in events:
                    print(mask)
                    print(key.data)
                    callback_func = key.data
                    callback_func(key.fileobj, mask)
            except OSError as e:
                print(e)
                continue


if __name__ == "__main__":
    servers()


