#!/usr/bin/env python3
# library.py

class Base:
    def foo(self):
        return 'foo'

# Now you are library code developer and have no access to user code. How do you ensure that user code dows not screw up?
class Base2:
    def foo(self):
        return self.bar()
