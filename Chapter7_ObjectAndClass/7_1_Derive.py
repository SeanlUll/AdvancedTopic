# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 14:17
# @Author  : Sean
# @File    : 7_1_Derive.py

class IntTuple(tuple):
    def __init__(self, iterable):
        super(IntTuple, self).__init__()
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

l = [1, -1, 'abc', 6, ['x', 'y'], 3]
t = IntTuple(l)
print(l)
print(t)