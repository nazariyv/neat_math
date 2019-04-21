#!/usr/bin/env python3

from time import time

def timer(func):
    def f(x, y=10):
        before = time()
        rv = func(x, y)
        after = time()
        print('elapsed', after - before)
        return rv
    return f

def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print('running {.__name__}'.format(f))
                rv = f(*args, **kwargs)
            return rv
        return wrapper
    return inner

#add = timer(add)

#@ntimes(2)
#@timer
def add(x, y=10):
    return x + y
add = ntimes(2)(add)
# python interpreter can tell you all sort of useful things about add
# add.__name__
# add.__module__
# add.__defaults__
# add.__code__
# add.__code__.co_code <- bytecodes
# add.__code__.co_nlocals
# add.__code__.co_varnames

# every python object has its runtime lifetime
# it sits in memory so you can ask it all sorts of questions
# for example:
# from inspect import getsource
# getsource(add)
# from inspect import getfile
# getfile(add)


print('add(10)',       add(10))
print('add(20, 30)',   add(20, 30))
print('add("a", "b")', add("a", "b"))
