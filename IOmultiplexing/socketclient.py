#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

def clients(host, port):
    client = socket.socket()
    client.connect((host, port))
    while True:
        msg = input('>>>:').strip()
        client.send(msg.encode('utf-8'))
        resp = client.recv(1024)
        print(resp)


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    clients(HOST, PORT)