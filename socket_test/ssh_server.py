#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import os

while True:
    with socket.socket() as sshserver:
        sshserver.bind(('127.0.0.1', 1478))
        sshserver.listen()
        conn,addr = sshserver.accept()

        while True:
            data = conn.recv(1024)
            if not data:
                print('None')
                continue
            print('Message:', data.decode('utf-8'))
            msg = os.popen(data.decode('utf-8')).read()
            conn.send(msg.encode('utf-8'))
