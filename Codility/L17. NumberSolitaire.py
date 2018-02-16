# In Python 3.6
# Time complexity: O(N)
# Space complexity: O(N)
import math
def solution(A):
    max_ = 0
    n = len(A)
    dp = [[-math.inf]*7 for _ in range(n)]
    dp[0] = [-math.inf] + [A[0]]*6
    
    for i in range(1, n):
        for k in range(1, 7):
            if i-k >= 0:
                dp[i][k] = max(dp[i][k-1], max(dp[i-k])+A[i])
            else:
                dp[i][k] = dp[i][k-1]
    
    return dp[n-1][6]