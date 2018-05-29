#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time

def test():
    for i in range(5):
        with socket(AF_INET, SOCK_STREAM) as s:
            # s = socket(AF_INET, SOCK_STREAM)
            s.connect(('127.0.0.1', 20000))
            print(s.sendall(b'hello'))
            print(s.recv(8192))
            s.close()
            time.sleep(1)

if __name__ == '__main__':
    t_num = 5
    for i in range(t_num):
        t = Thread(target=test, name='T{}'.format(i))
        print(t.getName(), 'run')
        t.start()

