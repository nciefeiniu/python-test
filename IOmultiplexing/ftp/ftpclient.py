#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import json
import os
import sys

def ftpclients(host, port):
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
            cmd_info = data.split()
            if cmd_info[0] == 'get':
                filename = cmd_info[1]
                msg = {
                    "action": cmd_info[0],
                    "filename": filename,
                    "size": 0
                }
            elif cmd_info[0] == 'put':
                filename = cmd_info[1].split('/')[-1]
                msg = {
                    "action": cmd_info[0],
                    "filename": filename,
                    "size": os.stat(cmd_info[1]).st_size
                }
            else:
                continue
            client.send(json.dumps(msg).encode('utf-8'))
            # 接收服务端的返回数据
            server_resp = client.recv(1024)

def download(conn, ):
    pass

def upload():
    pass



if __name__ == "__main__":
    HOST, PORT = '140.143.96.219', 9999
    ftpclients(HOST, PORT)