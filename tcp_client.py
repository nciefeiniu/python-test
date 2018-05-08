#!/usr/bin/python3
from socket import socket, AF_INET, SOCK_STREAM

def client():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 15000))
    info_num = s.send(b'hello')
    infos = s.recv(65536)
    print(info_num,infos)


