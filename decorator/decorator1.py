#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

def timer(auth_type):
    def out_warpper(func):
        print(auth_type)
        def warpper(*args, **kwargs):
            if auth_type == 'lamp':
                start_time = time.time()
                print(args)
                func(*args,  **kwargs)
                stop_time = time.time()
                print('这个方法运行了：%s' % (stop_time - start_time))
            elif auth_type == 'lnmp':
                print('NONONONO')
        return warpper
    return out_warpper

@timer(auth_type='lnmp')
def test1(name):
    time.sleep(3)
    print('测试员： %s' % name)


test1('liutao')