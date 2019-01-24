#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: url_manager.py
# @Time: 2019-1-23 15:49

# 分布式----url管理器
import pickle
from fenbushicrawl.tools.tools_helper import hashUrlHandler

class UrlManager(object):

    def __init__(self):
        '''
        初始化未爬取url集合和已爬取url集合
        '''
        # 未爬取url集合
        self.new_urls = self.loadProcess('new_urls.txt')
        # 已爬取url集合
        self.old_urls = self.loadProcess('old_urls.txt')

    def hasNewUrl(self):
        '''
        判断是否有待爬取url
        :return: True or False
        '''
        return self.newUrlsSize() != 0

    def newUrlsSize(self):
        '''
        获取未爬取url集合大小
        :return:
        '''
        return len(self.new_urls)

    def oldUrlsSize(self):
        '''
        获取已爬取url集合
        :return:
        '''
        return len(self.old_urls)

    def getNewUrl(self):
        '''
        取出一个新的url
        :return:
        '''
        new_url = self.new_urls.pop()
        hashed_url = hashUrlHandler(new_url)
        if hashed_url != None:
            self.old_urls.add(hashed_url)
        return new_url

    def addNewUrl(self, url):
        '''
        添加新的url
        :param url:
        :return:
        '''
        hashed_url = hashUrlHandler(url)
        if hashed_url != None:
            if url not in self.new_urls and hashed_url not in self.old_urls:
                self.new_urls.add(url)

    def addNewUrls(self, urls):
        '''
        批量添加新的url
        :param urls:
        :return:
        '''
        if urls != None and len(urls) > 0:
            for ul in urls:
                if ul != None:
                    self.addNewUrl(ul)

    def loadProcess(self, path):
        '''
        从本地文件加载进度
        :param path: 文件路径
        :return: set()
        '''
        print('[+] 从文件加载进度：%s' % path)
        try:
            with open(path, 'rb') as f:
                tmp = pickle.load(f)
                return tmp
        except:
            print('[!] 无进度文件， 创建：%s' % path)
        return set()

    def saveProcess(self, path, data):
        '''
        保存进度
        :param path:文件路径
        :param data:数据
        :return:
        '''
        with open(path, 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)




