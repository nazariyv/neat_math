#!/usr/bin/env python3
from time import sleep
# top-level syntax or function -> and there is a method that implements it
# x() -> __call__

def add1(x, y):
    return x + y

class Adder:
    def __call__(self, x, y):
        return x + y

add2 = Adder()
# type(add1) will return function
# type(add2) will return class

def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv
# this is bad
# if i only care about the first value, then it sitll takes 5 seconds to retrieve it
# if i only care about the first three, it still takes the same amount of time
# in terms of space, if I only care about the first item, it still takes 10 units of space
# if i care about the first three, still takes the sapce of 10 units
# ! wasteful from the amount of time it takes and wasteful from the amount of space it takes

# initial implementation
#class Compute:
#    def __call__(self):
#        rv = []
#        for i in range(10):
#            sleep(.5)
#            rv.append(i)
#        return rv
#
#compute = Compute()

# better implementation
class Compute:
    def __iter__(self):
        self.last = 0
        return self
    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv

# top level syntax has underlying function
# so something like:
# for x in xs:
#     pass
# has an under the hood implementation that looks like:
# x1 = iter(xs)    -> __iter__
# while True:
#    x = next(x1)  -> __next__

for val in Compute():
    print(val)

# Compute class is ugly and is hard to read. There is a better way of writing the same:
# a generator is a function that never returns eagerly
def compute():
    for i in range(10):
        sleep(.5)
        yield i

for val in compute():
    print(val)
# generators are coroutines, they yield the result and control back to the user
# interleaving the user code and the library code
# generators are built on the idea of co-routines:
# have library code run for a little bit. Have user code run for a little bit
# they are interleaved.
# in contrast to sub-routines any piece of executable code that runs
# from some starting point to the end to completion
# they have one single entry point - one single exit code and that's it.
# they run - they are done
# of exit

# a more critical use case for generators
class Api:
    # the reason api gives us three methods like this
    # is because they want us to run in this sequence
    # there are methods in between the steps that we could run!
    # this interleaving is important. If it wasn't, there would be
    # a method that runs all three at the same time.
    def run_this_first():
        first()
    def run_this_second():
        second()
    def run_this_last():
        last()

# And this is probably even a more critical mental model for the use of generators
# than the eager vs. lazy divide.
# Is that generators is a mechanism by which you can make code inter-leave with
# different code and also enforce sequencing
def api():
    first()
    # the code will run to this point, will not yield any value
    # but will yield the control back to the user
    yield
    second()
    yield
    # can guarantee that the last method was never called before the first or the
    # second
    # generator forces that sequencing on you
    # because generator is a co-routine that allows this interleaving of the user
    # code and the library code
    last()

