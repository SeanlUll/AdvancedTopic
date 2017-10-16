# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 17:50
# @Author  : Sean
# @File    : 9_3_DecoratorParameter.py

from inspect import signature

def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments
        def wrapper(*args, **kargs):
            for name, obj in sig.bind_partial(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name]))
            return func(*args, **kargs)
        return wrapper
    return decorator

@typeassert(int, str, list)
def f(a, b, c):
    print(a, b, c)

f(1, 'abc', [1, 2, 3])
f(1, 23, [1, 2]) #error