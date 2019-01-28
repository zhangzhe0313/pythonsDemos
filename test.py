#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from packages import *


def hanno(n, a, b, c):
    '''
    汉诺塔递归
    :param n: 盘子总数
    :param a: 起始塔
    :param b: 中间塔
    :param c: 目标塔
    :return:
    '''
    if n == 0:
        return
    hanno(n-1, a, c, b)
    print(a, '---->', c)
    hanno(n-1, b, a, c)

if __name__ == '__main__':
    print(packages.Circle)
    print(packages.Rectangle)

    import datetime
    d = datetime.date.weekday(datetime.date.today())
    c = datetime.date.isoweekday(datetime.date.today())
    print(d, c)
    print(datetime.datetime.now())

    print('id[a]', id('a')) # id() 获取内存地址

    a = 'A'
    b = 'B'
    c = 'C'
    n = 3
    hanno(n, a, b, c)


