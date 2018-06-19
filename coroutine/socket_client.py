#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

def clients():
    HOST, PORT = '127.0.0.1', 9999
    client = socket.socket()
    client.connect((HOST, PORT))
    while True:
        msg = input('>>>').strip()
        client.send(msg.encode('utf-8'))
        resp = client.recv(1024)
        print(resp.decode('utf-8'))

if __name__ == '__main__':
    clients()