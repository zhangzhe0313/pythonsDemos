#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: tools_helper.py
# @Time: 2019-1-23 17:12


# 工具类
import hashlib


def hashUrlHandler(url):
    '''
    将url进行md5处理，并返回[8:-8]取中间的128位
    :param url:
    :return:
    '''
    if url == None:
        return None
    m = hashlib.md5()
    m.update(url)
    url_rst = m.hexdigest()[8:-8]
    return url_rst
