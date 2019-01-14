#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# 闭包
def countDown(n):
    def next():
        nonlocal n
        r = n
        n -= 1
        return r
    return next

# 调用
m = 10
next = countDown(m)
while True:
    v = next()
    print(v)
    if not v:
        break
print(m)


# 闭包
def my_sum(*arg):
    return sum(arg)

def dec(func):
    def innerCheck(*arg):
        if len(arg) == 0:
            return 0
        for s in arg:
            if not isinstance(s, int):
                return 0
        return func(*arg)
    return innerCheck

my_sum = dec(my_sum)
print('my_sum: %d' % my_sum(1, 2, 3, 4, 5, '6'))
print('my_sum: %d' % my_sum(1, 2, 3, 4, 5))


# 装饰器---返回一个函数，被所定义的函数接收，这里被my_newsum所接收
@dec
def my_newsum(*args):
    return sum(args)

print('my_newsum: %d' % my_newsum(1, 2, 3, 4, 5, 6, 7, 8, 9))
