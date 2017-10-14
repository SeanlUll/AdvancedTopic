# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 16:08
# @Author  : Sean
# @File    : 3_6_StudentScore.py

from random import randint
from itertools import chain

chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]

##############################
# solution 1
##############################
total = []
for i in range(len(math)):
    total.append(chinese[i] + math[i] + english[i])

print(total)
##############################
# solution 2
##############################
total = []
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)
print(total)

#chain of itertools
e1 = [randint(60, 100) for _ in range(42)]
e2 = [randint(60, 100) for _ in range(44)]
e3 = [randint(60, 100) for _ in range(45)]
e4 = [randint(60, 100) for _ in range(40)]
count = 0
for s in chain(e1, e2, e3, e4):
    if s > 90:
        count += 1
print(count)