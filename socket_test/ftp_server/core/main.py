#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socketserver
import json

class TcpServer(socketserver.BaseRequestHandler):

    def put(self):
        pass

    def handle(self):
        while True:
            try:
                self.date = self.request.recv(1024).strip()
                print('客户端： %s 连接成功' % self.client_address[0])
                cmd = json.loads(self.data.decode())
                filename = cmd['filename']
                filesize = cmd['size']
            except Exception as e:
                print('err:', e)
                break


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    server = socketserver.ThreadingTCPServer
