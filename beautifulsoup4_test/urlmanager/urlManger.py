#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: urlManger.py
# @Time: 2019-1-22 10:08

class UrlManager(object):
    def __init__(self):
        # 用于存放已操作过的url
        self.old_urls = list()
        # 用于存放待操作的url
        self.new_urls = list()

    def has_new_url(self):
        '''
        判断是否有未操作的url
        :return
        '''
        return len(self.new_urls) != 0

    def add_new_url(self, url):
        '''
        未操作url集合中添加新的url
        :param url: 未操作的url对象
        :return:
        '''
        if url != None and url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)
        else:
            return

    def add_new_urls(self, urls):
        '''
        批量添加新的url到待操作url集合中
        :param urls:
        :return:
        '''
        if urls != None and len(urls) != 0:
            for ul in urls:
                self.add_new_url(ul)
        else:
            return

    def add_old_url(self, url):
        '''
        将已操作的url放入已操作url集合中
        :param url:
        :return:
        '''
        if url != None and url not in self.old_urls:
            self.old_urls.append(url)
        else:
            return

    def get_new_url(self):
        '''
        获取一个待操作的url
        :return:
        '''
        new_url = self.new_urls.pop()
        self.old_urls.append(new_url)
        return new_url

    def get_new_urls_size(self):
        '''
        获取待处理集合的大小
        :return:
        '''
        return len(self.new_urls)

    def get_index_zero_url(self):
        '''
        获取index = 0 的url
        :return:
        '''
        return self.new_urls.pop(0)
