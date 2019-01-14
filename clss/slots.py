#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# __slots__ 将实例中分配的属性名限定为指定的名称
class Account(object):
    __slots__ = ('name', 'sex')

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def printAccount(self):
        print('name: %s, sex: %s' % (self.name, self.sex))
