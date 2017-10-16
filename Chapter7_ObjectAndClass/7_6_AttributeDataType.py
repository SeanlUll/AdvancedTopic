# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 15:04
# @Author  : Sean
# @File    : 7_6_AttributeDataType.py

class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type = type_
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError('wrong type')
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)

P = Person()
P.name = 'bob'
# wrong age data type
P.age = 'abc'
P.height = 18