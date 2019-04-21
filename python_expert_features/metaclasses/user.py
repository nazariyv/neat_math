#!/usr/bin/env python3
# user.py
from library import Base3

# derived class enforcing constraint on base class. user level enforcing constraint on the library level
#assert hasattr(Base, 'foo'), "you broke it, you fool!"

#class Derived(Base):
#    def bar(self):
#        return self.foo()

class Derived2(Base3):
    def bar(self):
        return 'bar'

#for _ in range(10):
#    class Base: pass

# this statement is executable code
# thus Python accepts it
#class Base:
#    for _ in range(10):
#        def bar(self):
#           pass

# for wrapping purposes
#def _():
#    class Base:
#        pass

#from dis import dis
#dis(_)

b = Base3()
