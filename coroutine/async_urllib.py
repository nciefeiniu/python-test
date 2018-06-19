#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
使用协程来进行简单的爬网站
'''

from gevent import monkey
import gevent, time
from urllib import request

monkey.patch_all()

def test(url):
    resp = request.urlopen(url)
    data = resp.read()
    print(url + "  ,over, web's data have %s" % len(data))


if __name__ == "__main__":
    # 同步爬取
    start_time = time.time()
    urls = [
        'https://github.com/',
        'https://openstack.org',
        'https://python.org'
    ]
    for i in urls:
        test(i)
    print('同步爬取花费：%s 秒' % str(time.time()-start_time))

    # 异步爬取
    async_start_time = time.time()
    gevent.joinall([
        gevent.spawn(test,'https://github.com/'),
        gevent.spawn(test, 'https://openstack.org'),
        gevent.spawn(test, 'https://python.org')
    ])
    print('异步（协程花费时间）%s 秒' % str(time.time()-async_start_time))