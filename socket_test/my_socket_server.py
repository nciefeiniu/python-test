#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

while True:
    with socket.socket() as server:
        # server = socket.socket()
        server.bind(('127.0.0.1', 3838))
        server.listen()

        conn,addr = server.accept()
        while True:
            data = conn.recv(1024)
            if data:
                print('Message from:', addr, '. Message is :', data)
                conn.send(data.upper())
            else:
                print('客户端断开！')
                break