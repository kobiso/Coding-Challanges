"""
Author: Byungsoo Ko
Time complexity: O(nlogm) where n is nums and m is sum array of nums
Space complexity: O(n)
"""

class Solution:

    def countPieces(self, nums, mid):
        pieces = 0
        tmpSum = 0
        for num in nums:
            if tmpSum + num > mid:
                tmpSum = num
                pieces += 1
            else:
                tmpSum += num
        return pieces

    def splitArray(self, nums: List[int], m: int) -> int:

        left, right = max(nums), sum(nums)

        while (left < right):
            mid = (left + right) // 2
            pieces = self.countPieces(nums, mid)
            if pieces < m:
                right = mid
            else:
                left = mid + 1

        return left
