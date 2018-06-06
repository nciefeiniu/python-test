#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

while True:
    with socket.socket() as sshclient:
        sshclient.connect(('127.0.0.1', 1478))
        while True:
            msg = input('>>>>').strip()
            sshclient.send(msg.encode())
            # 返回命令结果长度
            res_size = sshclient.recv(1024)
            print(res_size)
            res = b''
            recevied_size = 0
            while recevied_size < int(res_size):
                res += sshclient.recv(1024)
                recevied_size = len(res)
            print(res.decode())