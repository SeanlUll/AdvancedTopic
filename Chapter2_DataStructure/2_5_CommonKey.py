# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 13:00
# @Author  : Sean
# @File    : 2_5_CommonKey.py

from random import randint, sample
from functools import reduce

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s1, s2, s3)

##############################
# solution 1
##############################
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print(res)

##############################
# solution 2
##############################
common_key = s1.keys() & s2.keys() & s3.keys()
print(common_key)

##############################
# solution 3
##############################
common_key = reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3]))