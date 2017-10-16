# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 11:17
# @Author  : Sean
# @File    : 6_1_CSV.py

import urllib.request
import csv

urllib.request.urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pingan.csv')

rf = open('pingan.csv', 'rb')
reader = csv.reader()

wf = open('pingan_copy.csv', 'wb')
writer = csv.writer(wf)





