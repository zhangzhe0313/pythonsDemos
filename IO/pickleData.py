#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 对象序列化
import pickle

data = {
    'name': 'lisi',
    'gender': '男'
}

# 序列化对象
with open('ceshi.txt', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

# 反序列化对象
with open('ceshi.txt', 'rb') as f:
    dataText = pickle.load(f)
print(dataText)
