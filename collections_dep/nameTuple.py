#!usr/bin/env pathon
# -*- coding: UTF-8 -*-

from collections import namedtuple

# 创建类
User = namedtuple('User', ['name', 'age', 'height'])
user_tuple = ('lisi', 20, 180)
userinfo = User(*user_tuple)
print(userinfo)

# *user_tuple->对应tuple类型；
name, age, height = User(*user_tuple)
print('name: %s, age: %d, height: %d' % (name, age, height))

# **user_tuple->对应dict类型
user_dict = {
    'name': 'lisi',
    'age': 30,
    'height': 179
}
name, age, height = User(**user_dict)
print('name: %s, age: %d, height: %d' % (name, age, height))

# namedtuple 的方法
# _make(可迭代对象)
name, age, height = User._make(user_tuple)
print('name: %s, age: %d, height: %d' % (name, age, height))

# 使用dict貌似不能正确解析数据
# user = User._make(user_dict)
# print('name: %s, age: %s, height: %s' % (user.name, user.age, user.height))

# _asdict()
user = User(*user_tuple)
userinfo = user._asdict()
print(userinfo)


