#!/bin/python3
# Input: the first line will contain two integer n and m seperated by a single space.
#  - Next m lines will contain three integers a,b and k separated by a single space.
#  - Numbers in list are numbered from 1 to n.
# Output: print in a single line the maximum value in the updated list.

import sys
from itertools import accumulate

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = [0]*(n+1)
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        arr[a-1] += k # Save one time and accumulate it later
        arr[b] -= k

    '''
    max = x = 0
    for i in arr:
        x = x+i
        if max < x:
            max = x
    '''
    print (max(accumulate(arr)))
