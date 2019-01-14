#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math

# 特性
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    # 添加特性--求圆的面积
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    # 添加特性--求圆的周长
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
