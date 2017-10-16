# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 18:02
# @Author  : Sean
# @File    : 9_4_AttributeModify.py

from functools import wraps
from random import randint
import time
import logging

def warn(timeout):
    def decorator(func):
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout:
                msg = '"%s" : %s  >  %s' % (func.__name__, used, timeout)
                logging.warn(msg)
            return res
        def setTimeout(k):
            nonlocal timeout
            timeout = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator

@warn(1.0)
def test():
    print("in test")
    while randint(0, 1):
        time.sleep(0.5)

for _ in range(30):
    test()

test.setTimeout(1.5)
for _ in range(30):
    test()

