#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import os, json
import hashlib

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()
        self.dir = '/'

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
        # 监控客户端的命令，跳转到对应的方法
        # 验证登陆
        state_login = False
        while not state_login:
            state_login = self.login()
        print('登陆成功')

        while True:
            cmd = input('>>>').strip()
            if not cmd: continue
            cmd_str = cmd.split()[0]
            # 反射
            if hasattr(self, "cmd_%s" % cmd_str):
                func = getattr(self, "cmd_%s" % cmd_str)
                func(cmd)
            elif cmd_str[0] == 'cd':
                self.dir = cmd_str[1]
            else:
                func = getattr(self, 'cmd_others')
                func(cmd)
                # help()

    def login(self):
        print('请登录')
        username = input('请输入账号：').strip()
        passwd = input('密码：').strip()
        # 用md5加密传输
        # h1 = hashlib.md5()
        h2 = hashlib.md5()
        # username = h1.update(username.encode('utf-8'))
        passwd = h2.update(passwd.encode('utf-8'))
        msg = {
            'action': 'login',
            'username': username,
            'passwd': h2.hexdigest()
        }
        # 向服务器验证
        self.client.send(json.dumps(msg).encode('utf-8'))
        server_response = self.client.recv(1024).strip().decode('utf-8')
        # print(json.loads(server_response))
        # 从服务器返回的json中
        try:
            if json.loads(server_response)['state'] == 1 :
                if json.loads(server_response)['systeminfo']:
                    print('Welcome to %s' % json.loads(server_response)['systeminfo'])
                return True
            return False
        except Exception as e:
            print('err: %s' %e)

    def cmd_others(self, *args):
        cmd_head = args[0].split()
        if cmd_head[0] == 'ls':
            cmd_info = {
                "action": "cmd_others",
                "head":cmd_head[0],
                "cmd": args[0],
                "currentdir": self.dir
            }
            print(cmd_info)
            self.client.send(json.dumps(cmd_info).encode('utf-8'))
            server_response = self.client.recv(1024).strip().decode('utf-8')
            data = json.loads(server_response)
            print(data['result'])
        elif cmd_head == 'cd':
            self.dir = args[1]
        elif cmd_head == 'pwd':
            print(self.dir)


    def cmd_put(self, *args):
        '''
        上传文件
        :param args:
        :return:
        '''
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
        else:
            print('命令不存在')
            self.help()


    def cmd_get(self, *args):
        cmd_split = args[0].split()
        if cmd_split:
            fileinfo = {
                "action": "get",
                "filename": cmd_split[1],
                "size": 0
            }
            # 给服务端发生请求下载数据
            self.client.send(json.dumps(fileinfo).encode('utf-8'))
            # 接受服务端的文件信息
            data = self.client.recv(1024).strip()
            server_response = json.loads(data.decode('utf-8'))
            filesize = server_response['size']
            filename = server_response['filename']
            # 告诉服务端可以开始传数据了。能防止粘包
            self.client.send(b'200 OK')
            # 开始接收数据
            oversize = 0
            with open(filename, 'wb') as f:
                while oversize < filesize:
                    data = self.client.recv(1024)
                    f.write(data)
                    oversize += len(data)
                print('Download success')
        else:
            print('命令不存在')
            self.help()

        def cmd_others():
            pass

if __name__ == '__main__':
    client = FtpClient()
    client.connect('111.230.243.174', 9999)
    # client.connect('127.0.0.1', 9992)
    client.interactive()