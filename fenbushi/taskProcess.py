#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: taskProcess.py
# @Time: 2019-1-17 18:05

# 任务进程
import random, time, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

# 第一步 使用register方法注册获取queue对象的方法名
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 第二步 连接到服务器， 验证口令
m = QueueManager(address=('127.0.0.1', 9001), authkey='nicai')
# 网络连接
m.connect()

# 第三步 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()

# 第四步 从task中获取任务，把结果写入result中
while(not task.empty()):
    image_url = task.get(True, timeout=5)
    print('run task download %s...' % image_url)
    time.sleep(1)
    result.put('%s--->success' % image_url)

# 处理结束
print('work exit...')