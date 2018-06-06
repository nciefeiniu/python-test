#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import os
from datetime import datetime

def write_logs(func):
    def wrapper(*args, **kwargs):
        msg = func.__name__ + ' is begining at   ' + (datetime.now()).__format__('%Y-%m-%d %H')+ '\r\n'
        print(msg)
        with open('sshlogs.txt', 'at') as f:
            f.write(msg)
        func(*args, **kwargs)
        # msg2 = func.__name__ + ' closed at   ' + (datetime.now()).__format__('%Y-%m-%d %H')+ '\r\n'
        # with open('sshlogs.txt', 'at') as f:
        #     f.write(msg2)
    return wrapper

@write_logs
def ssh_server():
    print('>>>begining')
    while True:
        with socket.socket() as sshserver:
            sshserver.bind(('127.0.0.1', 1478))
            sshserver.listen()
            while True:
                conn, addr = sshserver.accept()
                data = conn.recv(1024)
                if not data:
                    print('None')
                    continue
                print('Message:', data.decode('utf-8'))
                msg = os.popen(data.decode('utf-8')).read()
                conn.send(str(len(msg.encode('utf-8'))).encode('utf-8'))
                conn.sendall(msg.encode('utf-8'))
                print('send over')

if __name__ == "__main__":
    ssh_server()