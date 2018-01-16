#!/bin/python3

import sys

def fibonacciModified(t1, t2, n):
    # t_{i+2}=t_{i}+(t_{i+1})^2
    lookup=[t1, t2]
    for i in range(2, n):
        lookup.append(lookup[i-2] + (lookup[i-1]*lookup[i-1]))
        
    return lookup[n-1]    

if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)