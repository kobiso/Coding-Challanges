#!/bin/python3

import sys

def steadyGene(s):

    limit=len(s)/4
    min=len(s)
    dic ={'G':0,'A':0,'C':0,'T':0}
    duct={}
    for i in range(len(s)):
        #print (i, s[i])
        if dic[s[i]]+1<=limit:
            dic[s[i]]+=1
            dict=dic.copy()
        else:
            break
        for j in range(len(s)-1,i,-1):
            #print (s[j])
            if dict[s[j]]+1<=limit:
                dict[s[j]]+=1
                if min>j-i-1:
                    min=j-i-1
            else:
                break			
    return min

if __name__ == "__main__":
    n = int(input().strip())
    gene = input().strip()
    result = steadyGene(gene)
    print(result)
