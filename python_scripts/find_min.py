#!/usr/bin/env python3
from typing import List
import numpy as np

def find_min(arr: List[int]):
    min_ = arr[0]
    for i in np.arange(1, len(arr), 1):
        if arr[i] < min_:
            min_ = arr[i]
    return min_

def find_second_min(arr: List[int]):
    min1, min2 = arr[0], arr[1]
    # need to know which one is smallest. so that min1 is smallest
    min1 = min2 if min2 < min1 else min1

    for i in np.arange(2, len(arr), 1):
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    return min1, min2

if __name__ == '__main__':
    arr = [2, 5, 1, 0]
    print(f'arr: {arr}')
    print(f'min: {find_min(arr)}')
    print(f'min1, min2: {find_second_min(arr)}')
