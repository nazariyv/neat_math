#!/usr/bin/env python3

# the context manager metaphor is very simple
# there is some set up action and there is some tear down action
# and we want to match them
# some initial action and final action that we want to match

from sqlite3 import connect

# with connect('test.db') as conn:
#     cur = conn.cursor()
#     cur.execute('create table points(x int, y int)')
#     cur.execute('insert into points (x, y) values (1, 1)')
#     cur.execute('insert into points (x, y) values (1, 2)')
#     cur.execute('insert into points (x, y) values (2, 1)')
#     cur.execute('insert into points (x, y) values (2, 2)')
#    for row in cur.execute('select x, y from points'):
#        print(row)
#    for row in cur.execute('select sum(x * y) from points'):
#        print(row)
#    cur.execute('drop table points')

# in python all of the top level syntax has a __ function
# so something like this:
# with ctx() as x:
#   pass
# will have a __ function that implements it.
# in fact the above, behind the scenes, looks like:
# x = ctx().__enter__()
# try:
#    pass
# finally:
#    x.__exit__()

class temptable:
    def __init__(self, cur):
        self.cur = cur
    def __enter__(self):
        self.cur.execute('create table points(x int, y int)')
    def __exit__(self, *args):
        self.cur.execute('drop table points')

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values (3, 3)')
        cur.execute('insert into points (x, y) values (3, 2)')
        cur.execute('insert into points (x, y) values (3, 1)')
        cur.execute('insert into points (x, y) values (3, 4)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)

def temptable(cur):
    # from the above we saw that we create the table
    # and then delete the table
    # so we needed sequencing, and we know that for that
    # we can use generators
    # so here it is:
    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')

class contextmanager:
    def __init__(self, cur):
        self.cur = cur
    def __enter__(self):
        # on enter create the generator
        self.gen = temptable(self.cur)
        next(self.gen)
    def __exit__(self, *args):
        # on exit go back into method, drop table
        # and then return None
        next(self.gen, None)

with connect('test.db') as conn:
    cur = conn.cursor()
    with contextmanager(cur):
        cur.execute('insert into points (x, y) values (3, 3)')
        cur.execute('insert into points (x, y) values (3, 2)')
        cur.execute('insert into points (x, y) values (3, 1)')
        cur.execute('insert into points (x, y) values (3, 4)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)

# a more general solution is to pass the generator
# into the __init__
class contextmanager:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)
    def __exit__(self, *args):
        # on exit go back into method, drop table
        # and then return None
        next(self.gen_inst, None)

with connect('test.db') as conn:
    cur = conn.cursor()
    with contextmanager(temptable)(cur):
        cur.execute('insert into points (x, y) values (3, 3)')
        cur.execute('insert into points (x, y) values (3, 2)')
        cur.execute('insert into points (x, y) values (3, 1)')
        cur.execute('insert into points (x, y) values (3, 4)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)

# using the decorator syntax, this can be rewritten

class contextmanager:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)
    def __exit__(self, *args):
        # on exit go back into method, drop table
        # and then return None
        next(self.gen_inst, None)

@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values (3, 3)')
        cur.execute('insert into points (x, y) values (3, 2)')
        cur.execute('insert into points (x, y) values (3, 1)')
        cur.execute('insert into points (x, y) values (3, 4)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)

# do not need to write all of the context manager garbage
# it has been written for us in contextlib
from contextlib import contextmanager

# three fundamental python features in one example
# 1. context manager - pairs the setup with a teardown
# so that teardown happens whenever after the setup happens
# 2. a generator - some form of syntax that allows us to
# enforce sequencing and inter-leaving. Notice that
# context manager requires interleaving because the setup
# and then some action in the block (user code) and the
# the tear-down in the end. Plus there is that sequencing
# that the enter has to be down before the exit. So it makes
# sense to have a generator here as well
# 3. and then we need to wrap the generator with the underscore
# methods to make it behave as we want it. And that is what the
# decorator here is for to wrap the generator. And that is not
# even a feature, but decorator in itself is a nice feature/syntax
# that helps us do that.
@contextmanager
def temptable(cur):
    print('in fancy contextlib')
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values (3, 3)')
        cur.execute('insert into points (x, y) values (3, 2)')
        cur.execute('insert into points (x, y) values (3, 1)')
        cur.execute('insert into points (x, y) values (3, 4)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)

# expert code is not the code that uses every single Python feature
# it is the code that has clarity, it is the code that has
# clarity to where and when a certain feature has to be used
# it is when the person writing the code does not waste their time
# they know there is this pattern and the feature that solves it
# It is not when you write your own protocols. It is when
# you have the understanding of the core pieces of the language
# and understand how to assemble them. Thse core pieces are
# the language itself.

# Gist
# Real lessons from the PyData 2017 - James Powell lesson:
# Python is the language oriented around protocols
# There is some behaviour, some syntax, some byte-code or some top-level
# function and there is a way for you to tell Python how to implement that
# on an arbitrary object via underscore methods. The exact correspondance
# is usually guessable, but if you cannot guess it:
# google python data-model and you will find all the different methods and
# all of the caveats of their use.
# Python is a very simplistic language in terms of its execution model.
# Code runs from toop to bottom
# And things which would not be executable statements in other languages
# like class statements, function definitions or generator definitions
# are actually executable code in Python
# Because it's executable code, not only can you hook into them
# but you can define functions within functions base off the runtime
# data. Define classes withing functions based off some runtime
# information you have about them
# How these impace specific features?
# Metaclasses - some hook into the classes construction process.
# Because classes are constructed in run-time, you hook right into
# them. And because you can hook into subclass creation, you can ask it
# some questions like: "Do you have these methods implemented?"
# But the meaning behind it is quite simple. You have the library code
# and you have user code. When you sit on the library side, how
# do you make sure that the users don't screw up. How do you enforce
# the constraint from the library code to the user code.
# All that it takes is some way to hook into the process of how
# user classes are instantiated. That's merely what the metaclass is.
# In Python standard library there are solutions to these.
# In ABC there is an ABC metaclass there are decorators to mark
# the methods and abstract methods so that you do not have to write
# the metaclass yourself.
# Generators - is a way to take a computation that would otherwise run eagerly
# from the injection of its parameters to final computation and interleave
# it with other code by adding yield points where you can yield the
# intermediate values or one small piece of computation and also yield
# back the control to the caller. In that vein you can thinkg about
# the generator as the one long code and break it into small parts
# where you run small sub units of computation, where the user can step in
# and do whatever they want
# Context Managers - a way to take set up action and tear down action
# and ensure that they happen in concordance with each other. If Set up
# action occurs, ensure that teard down action occurs, even if there is an
# error somewhere.
# Remember what the features are and what they are for! That is the most
# important thing.
