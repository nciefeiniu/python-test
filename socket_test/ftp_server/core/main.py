#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
没有基于MD5来进行文件验证
auther: feiniu
'''

import socketserver
import json, os

class TcpServer(socketserver.BaseRequestHandler):

    def put(self, infos:dict):
        # 上传数据
        # 给客户端回应，表示可以开始接收数据了
        self.request.send(b'200 OK')
        filename = infos['filename']
        filesize = infos['size']
        with open(filename, 'wb') as f:
            oversize = 0
            while oversize<filesize:
                data = self.request.recv(1024)
                f.write(data)
                oversize += len(data)
            print('file has uploaded.')

    def get(self, infos:dict):
        # 下载数据
        # 应该传入文件名 以及文件路径
        # 现在是测试，先不传文件路径，默认就在当前文件同路径
        filename = infos['filename']
        filesize = os.stat(filename).st_size
        # 给客户端发送文件信息
        msg = {
            "filename": filename,
            "size": filesize
        }
        self.request.send(json.dumps(msg).encode('utf-8'))
        # 防止粘包，等待客户端给一个响应再发送数据
        self.request.recv(1024)
        # 开始发数据
        with open(filename, 'rb') as f:
            for line in f:
                self.request.send(line)
            print('send over')

    def login(self, login_data):
        datas = ''
        with open('../conf/account.json', 'r') as f:
            data = json.load(f)
        datas = data['account']
        self.username = login_data['username']
        self.passwd = login_data['passwd']
        for data in datas:
            if self.username == data['username'] and self.passwd == data['passwd']:
                print('OK')
                return True
        print('account is unable')
        return False

    def handle(self):
        while True:
            try:
                # 验证登陆
                login_data = json.loads(self.request.recv(1024).strip().decode('utf-8'))
                print(login_data)
                if self.login(login_data):
                    msg = {
                        "state": 1
                    }
                    self.request.send(json.dumps(msg).encode('utf-8'))
                    # if hasattr(self, login_data['action']):
                    #     func = getattr(self, login_data['action'])
                    #     # 验证方法返回True or False
                    #     if not func(login_data):
                    #         continue
                    print('客户端： %s 连接成功' % self.client_address[0])
                    self.cmd_data = self.request.recv(1024).strip()
                    cmd = json.loads(self.cmd_data.decode())
                    # filename = cmd['filename']
                    # filesize = cmd['size']
                    if hasattr(self, cmd['action']):
                        func = getattr(self, cmd['action'])
                        func(cmd)
                else:
                    msg = {
                        "state": 0
                    }
                    self.request.send(json.dumps(msg).encode('utf-8'))
                    continue
            except Exception as e:
                print('err:', e)
                break


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), TcpServer)
    server.serve_forever()
