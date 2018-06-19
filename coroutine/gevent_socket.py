#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
异步实现socket服务，多并发（协程）
'''

from gevent import monkey
import gevent
import socket

monkey.patch_all()

def socketserver():
    HOST, PORT = '127.0.0.1', 9999
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen(500)
    while True:
        cli, addr = server.accept()
        gevent.spawn(handle, cli)

def handle(conn):
    try:
        while True:
            data = conn.recv(1024)
            print('recv:', data)
            conn.send(data)
            if not data:
                conn.shutdown()
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    socketserver()
