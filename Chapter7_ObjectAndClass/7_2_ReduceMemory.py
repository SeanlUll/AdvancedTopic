# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 14:29
# @Author  : Sean
# @File    : 7_2_ReduceMemory.py

import sys

class Player(object):
    def __init__(self, uid, name, status = 0, level = 1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2(object):
    __slots__ = ['uid', 'name', 'stat', 'level']
    def __init__(self, uid, name, status = 0, level = 1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

p1 = Player('001', 'test')
p2 = Player2('001', 'test')
# __weakref__; __dict__
print(set(dir(p1)) - set(dir(p2)))

print(sys.getsizeof(p1.__dict__))