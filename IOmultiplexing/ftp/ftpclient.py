#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import json
import os
import sys

class FtpClient:
    def ftpclients(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            try:
                client.connect((host, port))
            except Exception as e:
                print("连接服务端失败,稍后再试")
                print(e)
                sys.exit(1)
            while True:
                print("需要输入完整路径~")
                data = input('>>>:').strip()
                self.interactive(client, data)

    def interactive(self, client, data):
        cmd_info = data.split()
        if cmd_info[0] == 'get':
            # 下载   get test.txt /home/test/    下载test.txt到/home/test/这个目录下
            filename = cmd_info[1]
            storage_dir = "/download/"
            if len(cmd_info) == 3:
                storage_dir = cmd_info[2]
            msg = {
                "action": cmd_info[0],
                "filename": filename,
                "size": 0
            }
            # 向服务器发送数据
            client.send(json.dumps(msg).encode('utf-8'))
            if hasattr(self, cmd_info[0]):
                func = getattr(self, cmd_info[0])
                func(client, filename, storage_dir)
        elif cmd_info[0] == 'put':
            if os.path.exists(cmd_info[1]):
                # 上传 put /home/test.txt
                filename = cmd_info[1].split('/')[-1]
                msg = {
                    "action": cmd_info[0],
                    "filename": filename,
                    "size": os.stat(cmd_info[1]).st_size
                }
                client.send(json.dumps(msg).encode('utf-8'))
                if hasattr(self, cmd_info[0]):
                    func = getattr(self, cmd_info[0])
                    func(client, filename, cmd_info[1])
            else:
                print("文件不存在，请检查后再上传")
        else:
            print("指令错误")

    def get(self, conn, filename, dir):
        # 接收服务端的返回数据
        server_resp = conn.recv(8192)
        data_info = json.loads(server_resp.decode('utf-8'))
        if data_info["existence"] == "True":
            # 给服务端确认，可以开始收取数据
            msg = {
                "size": data_info["size"]
            }
            conn.send(json.dumps(msg).encode('utf-8'))
            cur_filesize = 0
            with open(dir+filename, 'wb') as f:
                while cur_filesize < data_info['size']:
                    data = conn.recv(8192)
                    f.write(data)
                    cur_filesize += len(data)
            print('download done')
        else:
            print("文件不存在，请从新输入！！！！！！")








    def put(self, conn, filename, dir):
        # 接收服务端的确认信息
        server_resp = conn.recv(8192)
        # 开始传输数据
        with open(dir, 'rb') as f:
            for line in f:
                conn.send(line)
        print('upload done')




if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    ftp = FtpClient()
    ftp.ftpclients(HOST, PORT)