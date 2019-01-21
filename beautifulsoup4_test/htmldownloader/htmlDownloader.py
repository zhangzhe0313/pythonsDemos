#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: htmlDownloader.py
# @Time: 2019-1-21 14:46

import requests

# html下载器
class HtmlDownLoad(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    def downloadHtml(self):
        rsp = requests.get(self.url, headers=self.headers)
        rsp.encoding = requests.utils.get_encodings_from_content(rsp.text)
        return rsp.text