#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty

class Stackable(metaclass=ABCMeta):
    @abstractmethod
    def push(self, item):
        pass
    @abstractproperty
    def length(self):
        pass

class StackInfo(Stackable):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def length(self):
        return len(self.items)

if __name__ == '__main__':
    s = StackInfo()
    s.push(1)
    s.push(2)
    print(s.length())
