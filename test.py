#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import requests
import json

res = requests.get(url='http://192.168.137.222:5000/?question=hi')
for r in res:
    print(r)
print(res)


