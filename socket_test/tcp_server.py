#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from  socketserver import ThreadingTCPServer, StreamRequestHandler

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('连接来自：', self.client_address)
        self.data = self.request.recv(1024).strip()
        print(self.data)
        self.wfile.write(b'200 OK')


if __name__ == '__main__':
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
