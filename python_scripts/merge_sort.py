#!/usr/bin/env python3
from typing import List
from merge_two_sorted import merge_two_sorted

def merge_sort(arr: List[int]):

    if len(arr) <= 1:
        return arr

    if len(arr) > 1:
        mid = len(arr) // 2
        #print(arr[:mid])
        #print(arr[mid:])
        l, r = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        print(f'merging: {l}, {r}')
        merged = merge_two_sorted(l, r)
        print(f'merged:{merged}')

    return merged

if __name__ == '__main__':
    unsorted_arr = [1, 5, 2, 4, 9]
    print(merge_sort(unsorted_arr))
