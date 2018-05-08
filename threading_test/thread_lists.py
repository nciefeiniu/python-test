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
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection")
    sock.close()

def echo_server(addr, nworkers:int):
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start()
    # Run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(15)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))

# 创建126个线程
echo_server(('',15000), 126)