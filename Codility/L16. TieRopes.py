# Python 3.6
# Time complexity: O(N)
# Space complexity: O(N)

def solution(K, A):
    tied = []
    i=0
    for _ in range(len(A)):
        temp = 0
        while temp < K and i<len(A):
            temp += A[i]
            i += 1
        
        if temp < K:
            break
        else: tied.append(temp)
        
    return len(tied)