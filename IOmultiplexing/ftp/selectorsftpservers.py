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
        self.rootdir = '/home/selftp/'
        self.createdir()

    def createdir(self):
        if not os.path.exists(self.rootdir):
            os.makedirs(self.rootdir, )

    def servers(self):
        with socket,socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.host,self.port))
            server.setblocking(False)
            server.listen()
            # 有活跃的连接就交给helder这个方法处理
            self.sel.register(server,selectors.EVENT_READ, self.helder)

            while True:
                events = self.sel.select()
                for key, mask in events:
                    callback = key.data
                    callable(key.fileobj, mask)

    def helder(self, sock, mask):
        conn, addr = sock.accept()
        print(addr,' connection success ')
        conn.setblocking(False)
        self.sel.register(conn,selectors.EVENT_READ, self.actions)

    def actions(self, conn, mask):
        # 把json转换为字典
        c_data = json.loads(conn.recv(1024).decode('utf-8'))
        filename = c_data['filename']
        if c_data['action'] == 'put':
            self.upload(conn, filename)
        elif c_data['action'] == 'get':
            self.download(conn, filename)

    def download(self, conn, filename):
        if os.path.isfile(self.rootdir+filename):
            msg = {
                "filename": filename,
                "size": os.stat(self.rootdir+filename).st_size
            }
            # 给客户端发送文件信息,等待客户端回应再发送数据
            conn.send(json.loads(msg).encode('utf-8'))
            client_response = conn.recv(1024)
            with open(self.rootdir+filename) as f:
                for line in f:
                    conn.send(1024)
                print('send done')

    def upload(self):
        pass