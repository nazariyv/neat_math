#!/usr/bin/env python3
from typing import List, Any

# how should this work?
# recursion
# what is the base case?
# base case is that you have n-1 elements and you are just adding the last item and printing
# what should each recursion call be like?
# each item should appear in n positions, therefore there must be a loop that
# runs length number of times that varies the position of the current option

# a then all of the options from [b, c, d]
# b then all of the options from [a, c ,d]
# c then all of the options from [a, b, d]

# a, b then all of the options from [c, d]

# a, b, c then d
# a, b, d, then c

# Each elem is used length number of times

def permute(s, insert_index: int, constructed_arr: List[Any]):
    if not s:
        print(constructed_arr)

    len_s = len(s)
    elem = s.pop()
    # now use for
    for i in range(len_s):


    pass

if __name__ == '__main__':
    print(permute('owl'))
