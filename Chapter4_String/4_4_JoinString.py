# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 9:48
# @Author  : Sean
# @File    : 4_4_JoinString.py

l = ['abc', 123, 45, 'xyz']

# list
print(''.join([str(x) for x in l]))

# generator
print(''.join(str(x) for x in l))
