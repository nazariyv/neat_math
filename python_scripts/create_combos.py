#!/usr/bin/env python3
from typing import List, Any

# Given a set of characters and a positive integer k, print all possible strings of length k that can be formed from the given set.
# set[] = {'a', 'b'}, k = 3
# aaa, aab, aba, abb, baa, bab, bba, bbb

def combos(input_set: List[Any], k) -> List[Any]:
    # The pattern can be replicated in the following way
    # base - a. Add two options to it: aa, ba
    # base - b. Similarly: ab, bb
    # continue adding to each of the above until required length is obtained

    if len(input_set) == 1:
        return input_set

    permuted_set = []

    if len(input_set) > 1:
        for ix, elem in enumerate(input_set):
            all_permutes = combos(input_set[:ix] + input_set[ix + 1:], k - 1)
            permuted_set += [input_set[ix]] + all_permutes
            print(permuted_set)

    return permuted_set

if __name__ == '__main__':
    print(combos(['a', 'b', 'c', 'd'], 3))
