#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

while True:
    with socket.socket() as sshclient:
        sshclient.connect(('127.0.0.1', 1478))
        while True:
            msg = input('>>>>').strip()
            sshclient.send(msg.encode())
            data = sshclient.recv(1024)
            print(data.decode('utf-8'))