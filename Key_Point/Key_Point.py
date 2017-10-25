# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 10:28
# @Author  : Sean
# @File    : Key_Point.py

'''
strings, tuples, 和numbers是不可更改（immutable）的对象，而list,dict等则是可以修改（mutable）的对象。
'''
a = 1
def fun(a):
    a = 2
fun(a)
print(a) #1

a = []
def fun(a):
    a.append(1)
fun(a)
print(a) #[1]

