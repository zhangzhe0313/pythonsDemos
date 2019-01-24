#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: spider_worker.py
# @Time: 2019-1-24 14:19

from multiprocessing.managers import BaseManager
from fenbushicrawl.htmldownloader.html_downloader import HtmlDownLoader
from fenbushicrawl.htmlparser.html_parser import HtmlParser
# 爬虫调度器
class SpiderWorker(object):

    def __init__(self):
        BaseManager.register('getTaskQueue')
        BaseManager.register('getResultQueue')

        ip_port = ('127.0.0.1', 9999)
        self.mng = BaseManager(address=ip_port, authkey='baike')
        self.mng.connect()

        self.task = self.mng.getTaskQueue()
        self.result = self.mng.getResultQueue()

        self.downloader = HtmlDownLoader()
        self.parser = HtmlParser()

        print('init is over!!!')

    def crawl(self):
        while True:
            try:
                if not self.task.empty():
                    url = self.task.get()

                    if url == 'end':
                        print('控制节点通知爬虫节点停止工作!!!')
                        self.result.put({'new_urls': 'end', 'data': 'end'})
                        return
                    print('爬虫节点正在解析: %s' % url.encode('utf-8'))
                    content = self.downloader.downLoadHtml(url)
                    new_urls, data = self.parser.parser(url, content)
                    self.result.put({'new_urls': new_urls, 'data': data})
            except EOFError as err:
                print('连接工作点失败')
                return
            except Exception as e:
                print('error: %s' % e)
                print('Crawl Failed!!!')

if __name__ == '__main__':
    spiderWorker = SpiderWorker()
    spiderWorker.crawl()

