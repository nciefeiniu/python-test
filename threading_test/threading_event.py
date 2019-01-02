#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time

event = threading.Event()

def trafficlight():
    count = 0
    while True:
        if count < 5:
            event.set()
            print('=======green========')
        elif count >= 5 and count < 10:
            event.clear()
            print('=======red========')
        else:
            count = 0
            continue
        time.sleep(1)
        count += 1




def car(name):
    while True:
        if event.is_set():
            print('[%s] running' % name)
            time.sleep(1)
        else:
            print('[%s] waiting' % name)
            # 等待event设置
            event.wait()


if __name__ == '__main__':
    light = threading.Thread(target=trafficlight,)
    light.start()
    c = threading.Thread(target=car, args=('Tesla',))
    c.start()