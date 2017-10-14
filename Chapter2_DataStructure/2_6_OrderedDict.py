# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 13:16
# @Author  : Sean
# @File    : 2_6_OrderedDict.py

from collections import OrderedDict
from time import time
from random import randint

players = list('ABCDEFGH')
start = time()
data = OrderedDict()

for i in range(8):
    input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print(i + 1, p, end - start)
    data[p] = (i+1, end - start)

print('- ' * 20)
for k in data:
    print(k, data[k])
