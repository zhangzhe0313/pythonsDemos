#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: multiprocessing_test.py
# @Time: 2019-1-17 16:19

# 实现多进程的方式有两种，1：os.fork(); 2: multiprocessing

from multiprocessing import Process
import os

# 子进程执行的代码
def run_process(name):
    print('Child Process %s (%s) running...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent Process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_process, args=(str(i), ))
        print('Process will start')
        p.start()
    p.join()
    print('Process end...')