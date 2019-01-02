#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import wraps

def w_logs(a_type=2):
    def out_dec(func):
        @wraps(func)
        def warpper(*args, **kwargs):
            if a_type == 1:
                print('write logs:', func.__name__, 'is begining')
                func(*args, **kwargs)
        return warpper
    return out_dec

@w_logs(a_type=1)
def test(name):
    print(name)


test('liutao')
print(test.__name__)
print(test.__doc__)
print(test.__annotations__)