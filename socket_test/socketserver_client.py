#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

def socket_client():
    with socket.socket() as client:
        client.connect(('127.0.0.1', 9999))
        while True:
            msg = input('>>>:').strip()
            if not msg: continue
            client.send(msg.encode('utf-8'))
            data = client.recv(1024)
            print(data.decode())


if __name__ == '__main__':
    socket_client()