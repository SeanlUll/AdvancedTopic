# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 17:46
# @Author  : Sean
# @File    : 4_2_MatchString.py

import os, stat

string = os.listdir('.')[0]
print(string, string.endswith(('.sh', '.py')))

print(os.stat(os.listdir('.')[0]).st_mode)