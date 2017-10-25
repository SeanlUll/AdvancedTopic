# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 10:28
# @Author  : Sean
# @File    : Key_Point.py


'''
dict
'''
print("*" * 80)
d = {"server":"mpilgrim", "database":"master"}
print(d)
print(d["server"])
print(d["database"])

d["database"] = "pubs"
print(d)

'''
list
'''
print("*" * 80)
li = ['a', 'b', 'c', 'd', 'e', 'f']
print(li)
print(li[0])
print(li[2:4])
print(li[-3:-1])
li.append('g')
print(li)
li.extend(['h', 'i'])
print(li)
li.insert(2, 'test')
print(li)
li.remove('test')
print(li)

'''
tuple
'''
print("*" * 80)
t = ('1', '2', '3')
print(t)
(x, y, z) = ('a', 'b', 'c')
print(x)
print(y)
print(z)

'''
自省
'''
print("*" * 80)
def info(object, spaceing = 10, collapse = 1):
    """
    this is doc test
    """
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s %s" %
                     (method.ljust(spaceing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList]))
print(info.__doc__)
li = []
info(li)

'''
type()
'''
print("*" * 80)
x = 1
print(type(x))
li = []
print(type(li))
print(type(None))

'''
str()
'''
print("*" * 80)
x = 1
print(type(str(x)))
li = ['a', 'b']
print(type(str(li)))

'''
dir()
'''
print("*" * 80)
li = []
print(dir(li))
d  = {}
print(dir(d))

'''
callable()
'''
print("*" * 80)
print(callable(str))


'''
builtin class
'''
print("*" * 80)
info(__build_class__, 20)

