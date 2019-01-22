#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: storageInfo.py
# @Time: 2019-1-22 9:36

import pickle
import sys

# 将信息保存在文件中
def saveToFile(file_name, datas):
    sys.setrecursionlimit(1000000)
    with open(file_name, 'w+', encoding='utf-8') as f:
        for dt in datas:
            pickle.dump(dt, f, pickle.HIGHEST_PROTOCOL)


def saveToTxt(file_name, datas):
    try:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(datas)
    except IOError as err:
        print('IOError: %s' % err)