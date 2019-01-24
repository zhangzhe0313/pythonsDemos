#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: dispatch_manager.py
# @Time: 2019-1-23 18:01

# 分布式--控制调度器
from multiprocessing.managers import BaseManager
from multiprocessing import Process
from fenbushicrawl.urlmanager.url_manager import UrlManager
from fenbushicrawl.storagemanager.storage_manager import StorageManager
import time, queue

class DispatchManager(object):

    def __init__(self):
        pass

    def startDispatchManager(self, url_q, reault_q):
        '''
        创建一个分布式管理器
        :param url_q: url队列
        :param reault_q: result队列
        :return:
        '''
        # 把创建的队列注册到网络上，使用register方法，callable参数关联queue对象
        # 把queue对象在网络中暴露
        BaseManager.register('getTaskQueue', callable=lambda: url_q)
        BaseManager.register('getResultQueue', callable=lambda: reault_q)
        # 绑定端口9001， 设置验证口令 'baike', 这个过程相当于对象的初始化
        manager = BaseManager(address=('', 9999), authkey='baike')
        # 返回manager对象
        return manager

    def urlManagerProc(self, url_q, conn_q, root_url):
        urlManager = UrlManager()
        urlManager.addNewUrl(root_url)
        while True:
            while(urlManager.hasNewUrl()):
                # 从URL管理器获取新的URL
                new_url = urlManager.getNewUrl()
                # 将新的URL发给工作节点
                url_q.put(new_url)
                print('old_url_size: %d' % urlManager.oldUrlsSize())
                # 加一个判断条件，2000条记录结束
                if (urlManager.oldUrlsSize() > 2000):
                    # 通知节点工作结束
                    url_q.put('end')
                    print('控制节点发起结束通知')
                    # 关闭管理节点，同时存储set状态
                    urlManager.saveProcess('new_urls.txt', urlManager.new_urls)
                    urlManager.saveProcess('old_urls.txt', urlManager.old_urls)
                    return
            # 将从resultSolveProc获取到的url添加到url管理器
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    urlManager.addNewUrls(urls)
            except BaseException as e:
                # 延迟休息
                time.sleep(0.1)

    def resultSolveProc(self, result_q, conn_q, store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        print('分析进程接收通知后结束')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])  # url为set
                    store_q.put(content['data'])     # data 为dict
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)

    def storeProc(self, store_q):
        output = StorageManager()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('存储进程接收到结束通知')
                    output.outputEnd(output.file_path)
                    return
                output.storeData(data)
            else:
                time.sleep(0.1)


# 启动分布式管理
if __name__ == '__main__':
    # 初始化四个队列
    url_q = queue.Queue()
    reult_q = queue.Queue()
    store_q = queue.Queue()
    conn_q = queue.Queue()

    # 创建分布式调度管理器
    dispatchManager = DispatchManager()
    manager = dispatchManager.startDispatchManager(url_q, reult_q)

    # 创建url管理进程，数据提取进程，数据存储进程
    url_manager_proc = Process(target=dispatchManager.urlManagerProc, args=(url_q, conn_q, 'http://baike.baidu.com/view/284853.htm',))
    result_solve_proc = Process(target=dispatchManager.resultSolveProc, args=(reult_q, conn_q, store_q,))
    store_proc = Process(target=dispatchManager.storeProc, args=(store_q,))

    # 启动进程和分布式调度器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()

    manager.get_server().serve_forever()