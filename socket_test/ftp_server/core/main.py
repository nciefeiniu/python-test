#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socketserver
import json, os

class TcpServer(socketserver.BaseRequestHandler):

    def put(self, filename, filesize):
        # 给客户端回应，表示可以开始接收数据了
        self.request.send(b'200 OK')
        with open(filename, 'wb') as f:
            oversize = 0
            while oversize<filesize:
                data = self.request.recv(1024)
                f.write(data)
                oversize += len(data)
            print('file has uploaded.')

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('客户端： %s 连接成功' % self.client_address[0])
                cmd = json.loads(self.data.decode())
                filename = cmd['filename']
                filesize = cmd['size']
                if hasattr(self, cmd['action']):
                    func = getattr(self, cmd['action'])
                    func(filename, filesize)
            except Exception as e:
                print('err:', e)
                break


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), TcpServer)
    server.serve_forever()
