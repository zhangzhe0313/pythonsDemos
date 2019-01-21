#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: http_test.py
# @Time: 2019-1-21 8:50

# urllib3的使用
import urllib3


http = urllib3.PoolManager()
res = http.request('GET', 'http://www.baidu.com')

print(res.status)