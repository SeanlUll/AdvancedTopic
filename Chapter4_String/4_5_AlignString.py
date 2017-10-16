# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 9:57
# @Author  : Sean
# @File    : 4_5_AlignString.py

string1 = 'abc'

print(string1.ljust(20))
print(string1.ljust(20, '*'))
print(string1.rjust(20))
print(string1.center(20))

print(format(string1, '<20'))
print(format(string1, '>20'))
print(format(string1, '^20'))

