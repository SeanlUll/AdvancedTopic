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

'''
getattr()
'''
print("*" * 80)
li = ["larry", "curly"]
li.pop()
print(li)
getattr(li, "append")("meo")
print(li)
getattr(li, "pop")()
print(li)

'''
lambda()
'''
print("*" * 80)
print((lambda x: x * 2)(3))

'''
sys modules
'''
print("*" * 80)
import sys
print("\n".join(sys.modules.keys()))
print(dir(__builtins__))


print("*" * 80)
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)


print("*" * 80)
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

print("*" * 80)
def multipliers():
    return [lambda x : i * x for i in range(4)]

print([m(2) for m in multipliers()]) #[6, 6, 6, 6]

print("*" * 80)
def multipliers():
    for i in range(4):
        yield lambda x : i * x
print([m(2) for m in multipliers()]) #[0, 2, 4, 6]

print("*" * 80)
class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass

print (Parent.x, Child1.x, Child2.x)
Child1.x = 2
print (Parent.x, Child1.x, Child2.x)
Parent.x = 3
print (Parent.x, Child1.x, Child2.x)


print("*" * 80)
def div1(x,y):
    print("%s/%s = %s" % (x, y, x/y))

def div2(x,y):
    print("%s//%s = %s" % (x, y, x//y))

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

print("*" * 80)
list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])

print("*" * 80)
list = [[]] * 5
print(list)
