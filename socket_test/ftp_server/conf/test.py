#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

with open('account.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(data['account'][0])