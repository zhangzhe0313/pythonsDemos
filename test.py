#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from packages import *

if __name__ == '__main__':
    print(packages.Circle)
    print(packages.Rectangle)

    import datetime
    d = datetime.date.weekday(datetime.date.today())
    c = datetime.date.isoweekday(datetime.date.today())
    print(d, c)
    print(datetime.datetime.now())
