#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

def ftpserver():
    '''
    :return: None
    '''
    with socket.socket() as ftp:
        ftp.bind(('127.0.0.1', 9999))
        ftp.listen()
        while True:
            conn,addr = ftp.accept()
            print('conn from %s' % addr)
