#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: dispatch_manager.py
# @Time: 2019-1-23 18:01

# 分布式--调度器
from multiprocessing.managers import BaseManager

class DispatchManager(object):

    def __init__(self):
        pass

    def start_dispatch_manager(self, url_q, reault_q):
        '''
        创建一个分布式管理器
        :param url_q: url队列
        :param reault_q: result队列
        :return:
        '''
        # 把创建的队列注册到网络上，使用register方法，callable参数关联queue对象
        # 把queue对象在网络中暴露
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_result_queue', callable=lambda: reault_q)
        # 绑定端口9001， 设置验证口令 'baike', 这个过程相当于对象的初始化
        manager = BaseManager(address=('', 9999), authkey='baike')
        # 返回manager对象
        return manager
