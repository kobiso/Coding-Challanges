#!/bin/python3

import sys
from collections import Counter as ctr
import math

def steadyGene(gene):
    # let's get input
    n = len(gene)
    cnt = ctr(gene)
    
    # If all element is less than n/4, substring length is 0
    if all(e<=n/4 for e in cnt.values()):
        return 0
    
    minSub = math.inf
    cnted = 0
    # Find the last sequence of the string satisfying the condition
    for i in range(n):
        cnt[gene[i]] -= 1
        while all(e<=n/4 for e in cnt.values()) and cnted <= i:
            minSub = min(minSub, i-cnted+1)
            cnt[gene[cnted]]+=1
            cnted += 1   
    return minSub    

if __name__ == "__main__":
    n = int(input().strip())
    gene = input().strip()
    result = steadyGene(gene)
    print(result)