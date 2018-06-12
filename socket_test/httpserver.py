#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

def httpserver():
    with socket.socket() as server:
        server.bind(('127.0.0.1', 80))
        server.listen()
        conn,addr = server.accept()

        msg = b'''<html><head></head><body>Hello world!!</body></html>'''

        while True:
            request = conn.recv(1024)
            print(request)

            conn.sendall(msg)



if __name__ == "__main__":
    httpserver()