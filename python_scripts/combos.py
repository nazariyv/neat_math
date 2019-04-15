#!/usr/bin/env python3

def print_all_k_length(arr, k):
    n = len(arr)
    print_all_k_length_rec(arr, "", n, k)

def print_all_k_length_rec(arr, prefix, n, k):

    # base case if k is 0
    if (k == 0):
        print(prefix)
        return

    # one by one add all characters from set and recursively
    # call for k equals to k - 1
    for i in range(n):
        new_prefix = prefix + arr[i]
        # k decreases because we have added a new character
        print_all_k_length_rec(arr, new_prefix, n, k - 1)

if __name__ == '__main__':
    set1 = ['a', 'b']
    k = 3
    print_all_k_length(set1, k)
