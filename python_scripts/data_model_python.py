#!/usr/bin/env python3
# data model methods

# top-level function or top-level syntax -> corresponding __
# x + y ->   __add__
# init x ->  __init__
# repr(x) -> __repr__
# len(x) ->  __len__
# x() ->     __call__

# This is called the protocol view

# To really understand OOP in Python need to understand:
# 1. Protocol View
# 2. Iheritance Protocol
# 3. Caveats around how OOP in Python works

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        # repr is implemented in terms of calling repr on a constituent
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        # add is implemented in terms of calling add on a constituent
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        # protocol len implemented in terms of calling itself on a different
        # structure
        return len(self.coeffs)

    def __call__(self):
        pass


if __name__ == '__main__':
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(3, 4, 3)
