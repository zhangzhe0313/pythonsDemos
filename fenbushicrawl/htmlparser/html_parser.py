#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: html_parser.py
# @Time: 2019-1-24 14:00

# 页面解析器

import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self, page_url, html_cont):
        '''
        解析网页内容，抽取url和数据
        :param page_url:
        :param html_cont:
        :return:
        '''
        if page_url is None or html_cont is None:
            return None
        soup = BeautifulSoup(html_cont, 'lxml', from_encoding='utf-8')
        new_urls = self._getNewUrls(page_url, soup)
        new_datas = self._getNewData(page_url, soup)

        return new_urls, new_datas

    def _getNewUrls(self, page_url, soup):
        '''
        抽取新的url
        :param page_url:
        :param soup:
        :return:
        '''
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+/.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _getNewDatas(self, page_url, soup):
        '''
        提取新的数据
        :param page_url:
        :param soup:
        :return:
        '''
        data = {}
        data['url'] = page_url
        title = soup.find_all('a', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data
