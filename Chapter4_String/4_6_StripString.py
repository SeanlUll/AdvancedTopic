# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 10:07
# @Author  : Sean
# @File    : 4_6_StripString.py

import re

string1 = '  abc  123   '

print(string1)
print(string1.strip())
print(string1.lstrip())
print(string1.rstrip())

string2 = '---abc+++'
print(string2)
print(string2.strip('-+'))

string3 = 'abc:123'
print(string3)
print(string3[:3] + string3[4:])

string4 = '\tabc\t123\txyz'
print(string4)
print(string4.replace('\t', ''))

string5 = '\tabc\t123\txyz\ropq'
print(string5)
string5 = re.sub('[\t\r]', '', string5)
print(string5)



