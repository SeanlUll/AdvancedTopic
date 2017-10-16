# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 11:23
# @Author  : Sean
# @File    : 6_2_JSON.py

import json

l = [1, 2, 'abc', {'name': 'Sean', 'age': 24}]
print(json.dumps(l))
print(json.dumps(l, separators=[',', ':']))

d = {'b': None, 'a':5, 'c': 'abc'}
print(json.dumps(d))
print(json.dumps(d, sort_keys=True))