# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 17:27
# @Author  : Sean
# @File    : 9_1_FunctionDecorator.py

import time

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci2(n, cache = None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = fibonacci2(n - 1, cache) + fibonacci2(n - 2, cache)
    return cache[n]

#decorator
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
@memo
def fibonacci3(n):
    if n <= 1:
        return 1
    return fibonacci3(n - 1) + fibonacci3(n - 2)


start = time.time()
print(fibonacci(40)) #57 second
print("fibonacci time ", time.time() - start)
start = time.time()
print(fibonacci2(40)) #0.00004 second
print("fibonacci2 time ", time.time() - start)
start = time.time()
print(fibonacci3(40)) #0.000000001 second
print("fibonacci3 time ", time.time() - start)