#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 导入类
from clss.property import Circle

from clss.slots import Account

# 主函数
if __name__ == '__main__':

    # 类的特性测试
    cl = Circle(20)
    # cl = Circle(20) 会执行两个阶段：
    #     cl = Circle.__new__(20)
    #     if isinstance(cl, Circle):
    #         Circle.__init__(cl, 20)
    print('圆的面积是: %s' % format(cl.area, '.2f'))
    print('圆的周长是: %s' % format(cl.perimeter, '.2f'))

    cl.lgth = 20

    # 测试__slots__
    act = Account('xiaoming', 'man')
    act.printAccount()
    #  为act添加新的属性，则会报错，因为属性名不存在于__slots__中
    act.age = 10