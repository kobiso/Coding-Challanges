class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [math.inf] * (n+1)
        squares = []
        for i in range(1, len(dp)):
            if sqrt(i) % 1 == 0:
                squares.append(i)
                dp[i] = 1
            else:
                for square in squares:
                    dp[i] = min(dp[i], dp[i-square]+1)

        return dp[-1]
