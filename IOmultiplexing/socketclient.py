#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

def clients(host, port):
    with socket.socket() as client:
        client.connect((host, port))
        while True:
            msg = input('>>>:').strip()
            if msg:
                client.send(msg.encode('utf-8'))
                resp = client.recv(1024)
                print(resp)
            else:continue


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    clients(HOST, PORT)