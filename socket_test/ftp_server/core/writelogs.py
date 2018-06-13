#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
暂时出错
装饰类中的方法就会出错
'''

import time

def login_logs(func):
    def wrapper(self, *args, **kwargs):
        print('write logs begin')
        username = args[0]['username']
        login_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log_result = func(self, *args, **kwargs)
        yield log_result
        if log_result:
            login_str = '{} {} login success'.format(login_time, username)
        else:
            login_str = '{} {} login fales'.format(login_time, username)
        with open('../log/login.log', 'ab') as f:
            f.write(login_str)
        print('write logs success')
    return wrapper