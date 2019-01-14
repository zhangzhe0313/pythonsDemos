#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 生成器表达式： 不能生成列表对象，不能进项常规列表的索引操作等，只能被内置list()转成可迭代对象后
try:
    f = open('../bibao/bibao.py', 'r', encoding='utf-8')
    # 生成器表达式
    lines = (t for t in f)

    # 生成器表达式
    comments = (c for c in lines if c[0] == '#')
    for n in comments:
        print(n, end='')

    f.close()
except Exception as err:
    print('err: %s' % err)