#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import selectors
import socket
import json
import os

class ftpservers:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        # 存放路径,私有变量
        self.__rootdir = '/home/selftp/'
        self.createdir()
        # 同一个conn，同时只有一个消息在字典里面
        self.__message = {}

    def createdir(self):
        if not os.path.exists(self.__rootdir):
            os.makedirs(self.__rootdir, )

    def servers(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.host, self.port))
            server.setblocking(False)
            server.listen(1000)
            # 有活跃的连接就交给helder这个方法处理
            self.sel.register(server,selectors.EVENT_READ, self.helder)
            while True:
                events = self.sel.select()
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)

    # 建立连接,注册EVENT_READ事件
    def helder(self, sock, mask):
        conn, addr = sock.accept()
        print(addr,' connection success ')
        conn.setblocking(False)
        self.sel.register(conn,selectors.EVENT_READ, self.actions)

    def actions(self, conn, mask):
        # 把json转换为字典
        c_data = json.loads(conn.recv(8192).decode('utf-8'))
        if c_data:
            filename = c_data['filename']
            if c_data['action'] == 'put':
                # 上传
                size = c_data['size']
                print('准备上传')
                self.__message[conn] = [filename,size]
                # 更新注册的事件
                self.sel.modify(conn, selectors.EVENT_READ, self.upload)
                # 给客户端确认信息
                msg = {
                    "state": 200,
                    "size": size
                }
                conn.send(json.dumps(msg).encode('utf-8'))
            elif c_data['action'] == 'get':
                print('准备下载')
                # 给客户端发送数据信息
                if os.path.exists(self.__rootdir + filename):
                    msg = {
                        "filename": filename,
                        "size": os.stat(self.__rootdir + filename).st_size,
                        "existence": "True"
                    }
                    # 下载,吧需要下载的文件名放在message字典中，用conn为key, filename为value
                    self.__message[conn] = filename
                    # 更新注册的事件
                    self.sel.modify(conn, selectors.EVENT_READ, self.download)
                else:
                    print("文件不存在")
                    msg = {
                        "filename": filename,
                        "existence": "False"
                    }
                    self.sel.modify(conn, selectors.EVENT_READ, self.actions)
                # 给客户端发送文件信息,等待客户端回应再发送数据
                conn.send(json.dumps(msg).encode('utf-8'))
        else:
            print(conn, ' losing')
            self.sel.unregister(conn)
            conn.close()

    def download(self, conn, mask):
        # 从客户端接收确认信息，开始传数据
        client_response = conn.recv(8192)
        print('开始下载')
        filename = self.__message[conn]
        if os.path.isfile(self.__rootdir+filename):
            with open(self.__rootdir+filename, 'rb') as f:
                for line in f:
                    conn.send(line)
                print('send done')
        # 删除字典中当前连接的消息, 以及注销事件
        del self.__message[conn]
        # 更新注册的事件
        self.sel.modify(conn, selectors.EVENT_READ, self.actions)

    def upload(self, conn, mask):
        # 开始上传
        print("开始上传")
        filename = self.__message[conn][0]
        size = self.__message[conn][1]
        with open(self.__rootdir+filename, 'wb') as f:
            cur_size = 0
            while cur_size < size:
                data = conn.recv(8192)
                f.write(data)
                cur_size += len(data)
        print('upload done')



if __name__ == "__main__":
    HOST, PORT = '127.0.0.1',9999
    s = ftpservers(HOST, PORT)
    s.servers()