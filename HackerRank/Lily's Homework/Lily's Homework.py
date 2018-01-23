#!/bin/python3

import sys

def lilysHomework(arr):
    org = list(arr)
    arr.sort()

    dic = {}
    for i in range(len(arr)):
        dic[org[i]]=i

    swp = 0
    for i in range(len(arr)):
        if arr[i] != org[i]:
            swp += 1
            #index = org.index(arr[i])
            index = dic[arr[i]]
            dic[org[i]] = index
            org[i], org[index] = org[index], org[i]

    return swp

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    rev = list(arr)
    rev.reverse()
    asc = lilysHomework(arr)
    desc = lilysHomework(rev)
    print (min(asc,desc))
