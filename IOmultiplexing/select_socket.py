#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
IO多路复用-select，实现socket的多并发。
当套接字比较多的时候，每次select()都要通过遍历FD_SETSIZE个Socket来完成调度，不管哪个Socket是活跃的，都遍历一遍。这会浪费很多CPU时间
效率不高，浪费资源
'''
import socket
import select

def servers(host, port):
    server = socket.socket()
    server.bind((host, port))
    server.listen(1000)

    inputs = [server,]
    outputs = []

    while True:
        readable, writeable, exceptional = select.select(inputs, outputs, inputs)
        print(readable,writeable,exceptional)
        # 每次检测到有活跃的时候，就循环遍历整个socket,浪费资源
        for r in readable:
            if r is server:
                # 如果是server，那就把连接加入inputs，让kernel帮我们监控
                conn, addr = r.accept()
                print('有新的连接来自：%s' % str(addr))
                inputs.append(conn)
            else:
                # 如果不是server， 那肯定就是conn了
                data = r.recv(1024)
                print(data)
                r.send(data)


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    servers(HOST, PORT)