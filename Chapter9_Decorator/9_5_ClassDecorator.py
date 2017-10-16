# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 18:12
# @Author  : Sean
# @File    : 9_5_ClassDecorator.py

import logging
import time
from random import choice

class CallingInfo(object):
    def __init__(self, name):
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)
        fh = logging.FileHandler(name + '.log')
        log.addHandler(fh)
        log.info('start'.center(50, '-'))
        self.log = log
        self.formatter = '%(func)s -> [%(time)s - %(used)s - %(ncalls)s]'

    def info(self, func):
        def wrapper(*args, **kargs):
            wrapper.ncalls += 1
            lt = time.localtime()
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start

            info = {}
            info['func'] = func.__name__
            info['time'] = time.strftime('%x %X', lt)
            info['used'] = used
            info['ncalls'] = wrapper.ncalls
            msg = self.formatter % info
            self.log.info(msg)
            return res
        wrapper.ncalls = 0
        return wrapper

cinfo1 = CallingInfo('mylog1')
cinfo2 = CallingInfo('mylog2')

@cinfo1.info
def f():
    print("in f")
@cinfo1.info
def g():
    print("in g")
@cinfo2.info
def h():
    print("in h")

for _ in range(50):
    choice([f,g,h])()
    time.sleep(choice([0.5, 1, 1.5]))

