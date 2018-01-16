#!/bin/python3

import sys

def anotherMinimaxProblem(a):
    # Convert the input list into binary list
    bin_l = list(map(lambda x: bin(x)[2:], a))
    
    # Make a set of length of bin_l
    while True:
        len_s = set(map(lambda x: len(x), bin_l))
        if len(len_s) > 1:
            break
        if bin_l[0] == '0':
            return 0
        bin_l = list(map(lambda x: bin(int(x[1:], 2)), bin_l))
        
    big_s = set(map(lambda x: int(x,2), filter(lambda x: len(x)==max(len_s), bin_l)))
    small_s = set(map(lambda x: int(x,2), filter(lambda x: len(x)!=max(len_s), bin_l)))
    return min(big_c ^ small_c for big_c in big_s for small_c in small_s)

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = anotherMinimaxProblem(a)
    print(result)