#!/usr/bin/env python3
from typing import List
import numpy as np
from copy import deepcopy as dc
import time

def rearrange_neg_pos(arr: List[int]):
    arr = dc(arr)

    len1 = len(arr)
    prev_neg_idx = 0
    for ix in np.arange(1, len1, 1):
        if arr[ix] < 0:
            val = arr.pop(ix)
            arr = arr[:prev_neg_idx] + [val] + arr[prev_neg_idx:]
            prev_neg_idx += 1
    return arr

if __name__ == '__main__':
    arr = [1, 7, -5, 9, -12, 15]
    print(f'Rearranging: {arr}')
    start = time.time()
    rearranged_list = rearrange_neg_pos(arr)
    print(f'Rearranged: {rearrange_neg_pos(arr)}, it took: {time.time()-start}')
