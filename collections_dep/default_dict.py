#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: default_dict.py
# @Time: 2019-01-15 22:32

from collections import defaultdict

# 统计出现的次数
name_dict = {}
users = ['bobby1', 'bobby1', 'bobby2', 'bobby3', 'bobby2', 'bobby3', 'bobby1']
for name in users:
    if name not in name_dict:
        name_dict[name] = 1
    else:
        name_dict[name] += 1
print(name_dict)

# 使用setdefault()方法优化,效率更高
name_dict = {}
users = ['bobby1', 'bobby1', 'bobby2', 'bobby3', 'bobby2', 'bobby3', 'bobby1']
for name in users:
    name_dict.setdefault(name, 0)
    name_dict[name] += 1
print(name_dict)

# 进一步优化使用defaultdict(可调用的类型type)，当key不存在时，将会创建key,并以该类型type初始化key的值
default_dict = defaultdict(int)
users = ['bobby1', 'bobby1', 'bobby2', 'bobby3', 'bobby2', 'bobby3', 'bobby1']
for name in users:
    default_dict[name] += 1
print(default_dict)

# dict嵌套dict可以通过传递函数实现
def gen_group():
    return {
        'name': '',
        'age': 0
    }
default_group = defaultdict(gen_group)
print(default_group['group1'])
