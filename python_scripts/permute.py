#!/usr/bin/env python3

# Python function to print permutations of a given list
def permutation(lst):

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]


    l = [] # empty list that will store current permutation

    for i in range(len(lst)):
       m = lst[i]

       remLst = lst[:i] + lst[i+1:]

       for p in permutation(remLst):
           l.append([m] + p)
    return l


if __name__ == '__main__':
    data = list('123')
    for p in permutation(data):
        print p
