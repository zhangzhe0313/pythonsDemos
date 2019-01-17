#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: pool_test.py
# @Time: 2019-1-17 16:33

# 进程池
from multiprocessing import Pool
import os, time, random

def run_task(name):
    print('Task %s pid=%s is running...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end...' % name)

if __name__ == '__main__':
    print('Current Process %s...' % os.getpid())
    p = Pool(processes=3)
    for j in range(5):
        p.apply_async(run_task, args=(j, ))
    print('Waiting for all subProcess over...')
    p.close()
    # Pool对象调用join()会等待所有的子进程执行完毕，在调用是必须先调用close()
    p.join()
    print('All subprocess end...')
