# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 13:25
# @Author  : Sean
# @File    : 2_7_HistoryLog.py

from collections import deque
from random import randint

N = randint(0, 100)
history = deque([], 5)

def guess(k):
    if k== N:
        print('right')
        return True
    if k < N:
        print('%s is less-than N' % k)
    else:
        print('%s is greater-than N' % k)
    return False

while True:
    line = input('please input a number: ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(list(history))

