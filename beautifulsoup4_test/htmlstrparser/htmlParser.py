#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: htmlParser.py
# @Time: 2019-1-21 14:49

from bs4 import BeautifulSoup
from lxml import html
from urllib.parse import urljoin
import re

# 页面解析器
class HtmlParser(object):
    def __init__(self):
        pass

    def parserHrefs(self, baseUrl, html_str):
        '''
        根据已下载的html文件解析标题和链接地址
        :param html_str:
        :return: 返回标题和链接地址
        '''
        if html_str == None or baseUrl == None:
            return None, None
        else:
            soup = BeautifulSoup(html_str, 'lxml')
            return self._get_new_urls_datas(soup, baseUrl)

    def _get_new_urls_datas(self, soup, base_url):
        '''
        解析href与title
        :param soup:
        :return:
        '''
        new_ulrs = list()
        new_datas = list()
        for im in soup.select('dd > a'):
            href_im = im.get('href')
            title_im = im.string
            if href_im != None and title_im != None:
                box_href = urljoin(base_url, im.get('href'))
                if box_href not in new_ulrs and title_im not in new_datas:
                    new_ulrs.append(box_href)
                    new_datas.append(title_im)
        return new_ulrs, new_datas

    def parserContent(self, html_str):
        if html_str == None:
            return None, None
        else:
            soup = BeautifulSoup(html_str, 'lxml')
            h1 = soup.select('h1')
            if h1 != None:
                title_url = h1[0].get_text()
            content = soup.select('#content')
            if content != None:
                content_url = content[0].get_text()
        return title_url, content_url
