#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socketserver

class tcptest(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print('client from: {}' . format(self.client_address[0]))
            if not self.data:
                print('等待客户端连接......')
            print(self.data)
            self.request.send(self.data.upper())

if __name__ == '__main__':
    ip,port = '127.0.0.1', 9999
    # 单
    # myserver = socketserver.TCPServer((ip,port), tcptest)
    # 多并发
    myserver = socketserver.ThreadingTCPServer((ip, port), tcptest)
    print('running')
    myserver.serve_forever()
