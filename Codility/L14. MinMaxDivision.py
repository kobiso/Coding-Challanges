# In Python 3.6
# Time complexity: O(N*log(N+M))
# Space complexity: O(1)
import math
def check(K, A, mid):
    n = len(A)
    ls = 0
    sum = 0
    block = 0
    for i in range(n):
        if sum+A[i]>mid:
            ls = max(ls, sum)
            block += 1
            sum = A[i]
        elif sum+A[i]==mid:
            sum = sum + A[i]
            ls = max(ls, sum)
            block += 1
            sum = 0
        else:
            sum+=A[i]
        if i == n-1 and sum != 0:
            ls = max(ls, sum)
            block += 1
            
    return block, ls

def solution(K, M, A):
    n = len(A)
    beg = 1
    end = M*n
    min_ = sum(A)
    while beg <= end:
        mid = (beg+end)//2
        block, ls = check(K, A, mid)
        #print (mid, block, ls)
        if block <= K:
            end = mid - 1
            min_ = min(min_, ls)
        else:
            beg = mid + 1
            
    return min_