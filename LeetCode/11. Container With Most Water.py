# https://leetcode.com/problems/container-with-most-water/
# Runtime: 68 ms, faster than 59.31% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.5 MB, less than 5.18% of Python3 online submissions for Container With Most Water.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0
        i, j = 0, len(height)-1
        max_area = min(height[i], height[j]) * (j-i)
        while (i != j):
            if height[i] < height[j]:
                i=i+1        
            else:
                j=j-1
            max_area = max(max_area, min(height[i], height[j])*(j-i))
        return max_area