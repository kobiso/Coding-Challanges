# Time Complexity: O(N)
# Space Complexity: O(N)
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    std, max_pf = 0, 0
    
    for i in range(len(A)):
        if A[std] >= A[i]: std = i
        else: max_pf = max(max_pf, A[i]-A[std])
    
    return max_pf