# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 14:43
# @Author  : Sean
# @File    : 7_4_Property.py

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    def setRadius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('wrong type')
        self.radius = float(value)
    def getArea(self):
        return self.radius ** 2 * 3.14

    R = property(getRadius, setRadius)

c = Circle(3.4)
print(c.R)
c.R = 5.9
print(c.R)