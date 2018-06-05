#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket


with socket.socket() as client:

    client.connect(('127.0.0.1', 3838))
    while True:
        msg = input('Please input:').strip()
        if msg == 'exit' or msg == '':
            break
        else:
            client.send(msg.encode('utf-8'))
            data = client.recv(1024) #接收大小
            print(data)
