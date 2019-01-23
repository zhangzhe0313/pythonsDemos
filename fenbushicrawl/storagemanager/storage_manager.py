#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: storage_manager.py
# @Time: 2019-1-23 17:41

# 数据存储器
import codecs
import time

class StorageManager(object):

    def __init__(self):
        '''
        初始化
        '''
        self.file_path = 'baike_%s.html' % (time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        self._outputHeader(self.file_path)
        self.datas = []

    def _outputHeader(self, file_path):
        '''
        把html头部写进去
        :param file_path:
        :return:
        '''
        fout = codecs.open(file_path, 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        fout.close()

    def storeData(self, data):
        '''
        拼接数据
        :param data:
        :return:
        '''
        if data == None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self._outputHtml(self.file_path)

    def _outputHtml(self, file_path):
        '''
        把数据写入html文件中
        :param file_path:
        :return:
        '''
        fout = codecs.open(file_path, 'a', encoding='utf-8')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.close()

    def outputEnd(self, file_path):
        '''
        把html结束标签写进去
        :param file_path:
        :return:
        '''
        fout = codecs.open(file_path, 'w', encoding='utf-8')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()