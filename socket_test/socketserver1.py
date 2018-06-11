#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socketserver

class tcptest(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print('client from: {}' . format(self.client_address[0]))
        print(self.data)
        self.request.send(self.data.upper())

if __name__ == '__mian__':
    ip,port = '127.0.0.1', 9999
    myserver = socketserver((ip,port), tcptest)
    myserver.server_forever()
