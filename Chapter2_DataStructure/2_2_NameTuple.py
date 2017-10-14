# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 12:30
# @Author  : Sean
# @File    : 2_2_NameTuple.py

from collections import namedtuple

##############################
# solution 1
##############################
NAME, AGE, SEX, EMAIL = range(4)
student = ('Sean', 24, 'male', 'seanhe@qq.com')

print(student[NAME])
print(student[AGE])
print(student[SEX])
print(student[EMAIL])


##############################
# solution 2
##############################
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
student = Student('Sean', 24, 'male', 'seanhe@qq.com')

print(student.name)
print(student.age)
print(student.sex)
print(student.email)

