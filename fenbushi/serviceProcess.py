#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: serviceProcess.py
# @Time: 2019-1-17 17:46

# 服务进程
import random, time, queue
from multiprocessing.managers import BaseManager

# 第一步 建立task_queue 和 result_queue 用来存放任务和结果
task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

# 第二步 把创建的队列注册到网络上，使用register方法，callable参数关联queue对象
# 把queue对象在网络中暴露
QueueManager.register('get_task_queue', callable=lambda : task_queue)
QueueManager.register('get_result_queue', callable=lambda : result_queue)

# 第三步 绑定端口9001， 设置验证口令 'nicai', 这个过程相当于对象的初始化
manager = QueueManager(address=('127.0.0.1', 9001), authkey='nicai')

# 第四步 启动管理，监听信息通道
manager.start()

# 第五步 通过管理实例的方法获取网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 第六步 添加任务
for url in ["imageUrl_" + i for i in range(10)]:
    print('put task %s...' % url)
    task.put(url)

# 第七步 获取返回结果
print('try get result...')
for i in range(10):
    print('result is %s...' % result.get(timeout=10))

# 第八步 关闭管理
manager.shutdown()