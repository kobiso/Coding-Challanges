# Time complexity: O(N*log(N))
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(A):
    # write your code in Python 3.6
    max = -math.inf
    A.sort()
    for i in range(0, -4, -1):
        if max < A[0 + i] * A[1 + i] * A[2 + i]:
            max = A[0 + i] * A[1 + i] * A[2 + i]

    return max