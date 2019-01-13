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