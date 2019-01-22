#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: main.py
# @Time: 2019-1-21 14:52

# 主入口
from beautifulsoup4_test.htmldownloader.htmlDownloader import HtmlDownLoad
from beautifulsoup4_test.htmlstrparser.htmlParser import HtmlParser
from urllib.parse import urljoin
from beautifulsoup4_test.storageresult.storageInfo import saveToTxt, saveToFile
from beautifulsoup4_test.urlmanager.urlManger import UrlManager

class MainHandler(object):
    def __init__(self, baseUrl, targetUrl):
        self.base_url = baseUrl
        self.target_url = targetUrl
        self.urlManager = UrlManager()
        self.htmlDownLoader = HtmlDownLoad()
        self.htmlParser = HtmlParser()
        self.urls_list = []

    # 获取所有的章节
    def crawlByUrl(self):
        # step1 获取所有的章节href和title
        self.urlManager.add_new_url(urljoin(self.base_url, self.target_url))
        # 获取一个待操作的url
        new_url = self.urlManager.get_new_url()
        # 页面下载器根据url下载对应的页面
        html_str = self.htmlDownLoader.downloadHtml(new_url)
        html_hrefs, html_title = self.htmlParser.parserHrefs(self.base_url, html_str)
        # 将得到的新的urls添加到url集合中
        self.urlManager.add_new_urls(html_hrefs)

        # step2 循环所有的章节href下载对应的内容
        cnt = 0
        while self.urlManager.has_new_url():
            # 获取一条待处理的url
            new_url = self.urlManager.get_new_url()
            # 页面下载器根据url下载响应页面
            html_str = self.htmlDownLoader.downloadHtml(new_url)
            # 处理待处理的url，获取响应的内容与标题
            if html_str != None:
                # 统计下载数量
                cnt += 1
                print('new_url %d: %s' % (cnt, new_url))

                title_url, content_url = self.htmlParser.parserContent(html_str.replace('<br>', '').replace('\n', ''))
                if title_url != None and content_url != None:
                    # 将解析结果存在文件中
                    saveToTxt('fuTianJi.txt', title_url+'\n'+ content_url.replace(' ', '')+'\n')
            else:
               continue



# 爬小说测试
if __name__ == '__main__':
    base_url = 'http://www.biquyun.com'
    test_target = '/8_8568/'

    mainHandler = MainHandler(base_url, test_target)
    mainHandler.crawlByUrl()
