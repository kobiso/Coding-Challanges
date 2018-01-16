#!/bin/python3

import sys
import itertools as it
import math

def maxScore(lt):
    maxS = 0
    for i in range(len(lt)-1):
        maxS = max(maxS, (lt[i]^lt[i+1]))
    return maxS
    
def anotherMinimaxProblem(a):
    # It has to be Min among the permutation, and Max among XOR operation
    # For each permutation, check the max score
    minS = math.inf
    perm = it.permutations(a)
    for p in perm:
        #score = maxScore(p)
        minS = min(minS, maxScore(p))
    return minS
    

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = anotherMinimaxProblem(a)
    print(result)