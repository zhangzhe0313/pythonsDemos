#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: html_downloader.py
# @Time: 2019-1-24 13:52

# 页面下载器

import requests

class HtmlDownLoader(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    def downLoadHtml(self, url):
        if url is None:
            return None
        res = requests.get(url,headers=self.headers)
        if res.status_code == 200:
            res.encoding = 'utf-8'
            return res.text
        return None
