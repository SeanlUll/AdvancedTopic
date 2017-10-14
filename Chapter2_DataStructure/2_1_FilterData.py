# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 12:08
# @Author  : Sean
# @File    : 2_1_FilterData.py

from random import randint

#generate a random list
data = [randint(-10, 10) for _ in range(10)]
print(data)

#filter item which greater than 0 using "filter"
filter_data = filter(lambda x: x >= 0, data)
print(list(filter_data))

#filter item which greater than 0 using List parsing
parse_data = [x for x in data if x >= 0 ]
print(parse_data)

#generate a random directory
data = {x: randint(60, 100) for x in range(1, 21)}
print(data)

#filter item which greater than 0 using Directory parsing
parse_data = {k: v for k, v in data.items() if v > 90}
print(parse_data)

#generate a random set
data = [randint(-10, 10) for _ in range(10)]
s = set(data)

#filter item which greater than 0 using Set parsing
parse_data = {x for x in s if x % 3 == 0}
print(parse_data)

