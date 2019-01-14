#!usr/bin/env pathon
# -*- coding: UTF-8 -*-


# 程序运行时服务
import atexit

def exitProgress():
    print('程序退出')

atexit.register(exitProgress)
