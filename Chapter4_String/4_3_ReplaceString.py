# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 18:07
# @Author  : Sean
# @File    : 4_3_ReplaceString.py

import re

string = """
        2017-07-12 xxxxx
        2017-08-22 .....
        2018-10-11 ,,,,,
        """
print(string)
string = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', string)
print(string)