# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 12:48
# @Author  : Sean
# @File    : 2_4_DictSort.py

from random import randint

data = {x: randint(60, 100) for x in 'xyzabc'}
print(data)

sorted_data1 = sorted(data)
print(sorted_data1)

sorted_data2 = sorted(zip(data.values(), data.keys()))
print(sorted_data2)

sorted_data3 = sorted(data.items(), key=lambda x: x[1])
print(sorted_data3)