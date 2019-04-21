#!/usr/bin/env python3
# library.py

#class Base:
#    def foo(self):
#        return 'foo'

# Now you are library code developer and have no access to user code. How do you ensure that user code dows not screw up?

# pattern that noone should use to check that bar in Derived is implemented
# from running dis(_) on:
# def _():
#   class Base: pass
# we have learned that python byte code follows the protocol view
# and there is a python byte code operation to build a class
# and surprise surprise we can "HOOK INTO IT" because python follows
# the protocol view. And the in-build function for this is:
#old_bc = __build_class_
#def my_bc(fun, name, base=None, **kw):
#    if base is Base:
#        print('Check if bar method defined')
#    if base is not None:
#        return old_bc(fun, name, base, **kw)
#    return old_bc(fun, name, **kw)
#
#import builtins
#builtins.__build_class__ = my_bc

# ^^ is not how people solve enforcing constraints from base classes
# to derived classes. This is how:

class BaseMeta(type):
    # meta classes allow you to intercept the construction
    # of the derived class
    def __new__(cls, name, bases, body):
        print(body)
        if not 'bar' in body:
            raise TypeError("bad user class")
        print('BaseMeta.__new__', cls, name, bases, body)
        return super().__new__(cls, name, bases, body)

class Base3(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    # the easiest solution:
    def __init_subclass__(self, *a, *kw):
        print('init_subclass', a, kw)
        return super().__init_subclass__(*a, **kw)
