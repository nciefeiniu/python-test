#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import os, json

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = '''
        ls
        pwd
        cd ..
        put filename
        get filename
        '''
        print(msg)

    def connect(self, ip, port):
        '''
        连接服务器
        :param ip:
        :param port:
        :return:
        '''
        self.client.connect((ip, port))

    def interactive(self):
        while True:
            cmd = input('>>>').strip()
            if not cmd: continue
            cmd_str = cmd.split()[0]
            # 反射
            if hasattr(self, "cmd_%s" % cmd_str):
                func = getattr(self, "cmd_%s" % cmd_str)
                func(cmd)
            else:
                self.help()

    def cmd_put(self, *args):
        cmd_split = args[0].split()
        if cmd_split:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                fileinfo = {
                    "action": "put",
                    "filename": filename,
                    "size": filesize,
                }
                # 向服务器发送数据
                self.client.send(json.dumps(fileinfo).encode('utf-8'))
                # 防止粘包，等待服务器确认
                server_response = self.client.recv(1024)
                with open(filename, 'rb') as f:
                    for line in f:
                        self.client.send(line)
                    print('upload success')
            else:
                print(filename, 'is not exist')

    def cmd_get(self):
        pass