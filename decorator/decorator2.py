#!/usr/bin/env python3
# -*- coding:utf-8 -*-



def w_logs(a_type=2):
    def out_dec(func):
        def warpper(*args, **kwargs):
            if a_type == 1:
                print('write logs:', func.__name__, 'is begining')
                func(*args, **kwargs)
        return warpper
    return out_dec

@w_logs(a_type=2)
def test(name):
    print(name)


test('liutao')