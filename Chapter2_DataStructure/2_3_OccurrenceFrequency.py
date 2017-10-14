# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 12:40
# @Author  : Sean
# @File    : 2_3_OccurrenceFrequency.py

from random import randint
from collections import Counter

data = [randint(0, 20) for _ in range(30)]
print(data)

##############################
# solution 1
##############################
c1 = dict.fromkeys(data, 0)

for x in data:
    c1[x] += 1
print(c1)

##############################
# solution 2
##############################
c2 = Counter(data)
print(c2)
print(c2.most_common(3))
