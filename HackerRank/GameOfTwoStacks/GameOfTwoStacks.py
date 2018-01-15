#!/bin/python3

import sys

g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    # your code goes here
    
    sum = 0
    count = 0
    max_count =0
    tempA = []
    
    # Inverse 'a' and 'b' list to use as stack
    a.reverse() 
    b.reverse()
    
    # Pop from stack A and sum until it exceeds the limit
    while len(a)!=0:
        if sum + a[-1] <= x:
            sum += a[-1]
            count += 1
            tempA.append(a.pop()) # Save pop-ed element from stack A
        else:
            break
    max_count = count # Save current max_count
    
    # Pop from stack B and plus it with 'sum' 
    while len(b)!=0:
        sum += b.pop()
        count += 1
        
        # If 'sum' exceeds the limit, discard one from tempA
        while sum > x and len(tempA)!=0:
            sum -= tempA.pop()
            count -= 1
        
        if sum <= x and max_count < count:
            max_count = count
        elif sum > x:
            break

    print (max_count)