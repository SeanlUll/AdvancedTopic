# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 17:32
# @Author  : Sean
# @File    : 4_1_SplitString.py

import re

string = 'ab;cd,ef|gh,ij|kl;mn\top\tqrs,tuv;wx|yz'
print(re.split(r'[,;\t|]+', string))