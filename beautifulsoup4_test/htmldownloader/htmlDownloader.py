#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: htmlDownloader.py
# @Time: 2019-1-21 14:46

import requests

# html下载器
class HtmlDownLoad(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        self.cookies_temp = '__jsluid=e1894a8f2bdd3fade626cb6b69158e15'

    def downloadHtml(self, url):
        '''
        页面下载器
        :param url: 待操作url
        :return:  页面内容
        '''
        rsp = requests.get(url, headers=self.headers)
        rsp.encoding = 'gbk'
        if rsp.status_code == 200:
            return rsp.text
        else:
            return None