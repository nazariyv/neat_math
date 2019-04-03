#!/usr/bin/env python3
def merge_two_sorted(arr1, arr2):
    len1, len2 = len(arr1), len(arr2)
    ix1, ix2 = 0, 0
    merged = []

    while (ix1 != len1 and ix2 != len2):
        if arr1[ix1] >= arr2[ix2]:
            merged.append(arr2[ix2])
            ix2 += 1
        else:
            merged.append(arr1[ix1])
            ix1 += 1

    if len2 > len1:
        merged += arr2[ix2:]
    elif len1 > len2:
        merged += arr1[ix1:]
    else:
        val1, val2 = arr1.pop(), arr2.pop()
        if val1 == merged[-1]:
            merged.append(val2)
        else:
            merged.append(val1)

    return merged

if __name__ == '__main__':
    arr1, arr2 = [1, 5, 9, 20], [2, 3, 11, 18]
    print(f'Merging two sorted arrs. arr1: {arr1}, arr2: {arr2}.')
    merged = merge_two_sorted(arr1, arr2)
    print(f'Merged sorted arrays: {merged}.')
