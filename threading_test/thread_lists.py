#!/usr/bin/python3
'''
# 手动创建自己的线程池
'''

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue

def echo_client(q):
    sock, client_addr = q.get()
    print("Got connection from", client_addr)
    while True:
        msg = sock.recv(1024)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection")
    sock.close()

def echo_server(addr, nworkers:int):
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        # 设置为守护线程，随主线程退出
        t.daemon = True
        t.start()
    # Run the server
    sock = socket(AF_INET, SOCK_STREAM)
    # 绑定
    sock.bind(addr)
    # 监听
    sock.listen(15)
    while True:
        # socket.accept返回两个值
        client_sock, client_addr = sock.accept()
        # 放在队列中
        q.put((client_sock, client_addr))

if __name__ =='__main__':
    # 创建126个线程
    echo_server(('127.0.0.1',15000), 126)