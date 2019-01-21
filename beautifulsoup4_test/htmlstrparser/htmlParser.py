#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: htmlParser.py
# @Time: 2019-1-21 14:49

from bs4 import BeautifulSoup
from lxml import html

# 页面解析器
class HtmlParser(object):
    def __init__(self, html):
        self.html = html

    # 使用beautifulsoup解析
    def htmlParserContent(self):
        novles = list()
        soup = BeautifulSoup(self.html, 'html.parser')
        for mulu in soup.find_all(class_='mulu'):
            h2 = mulu.find('h2')
            if h2 != None:
                # 获取标题
                h2_title = h2.string
                # 获取所有的a标签中url 和章节内容
                for im in mulu.find(class_='box').find_all('a'):
                    box_href = im.get('href')
                    box_title = im.get('title')
                    novles.append(
                        {
                            'title': box_title,
                            'url': box_href
                        }
                    )
        return novles

    #   使用lxml解析
    # def htmlParserContent(self):
    #     etree = html.etree
    #     htmlDiv = etree.HTML(self.html)
    #     print(htmlDiv.xpath("//meta[1]/@url"))
