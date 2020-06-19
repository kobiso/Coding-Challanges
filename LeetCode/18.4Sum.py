# https://leetcode.com/problems/4sum
# Runtime: 1056 ms, faster than 32.28% of Python3 online submissions for 4Sum.
# Memory Usage: 13.3 MB, less than 43.10% of Python3 online submissions for 4Sum.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        length = len(nums)
        if length < 3: return []
        if length == 4:
            if sum(nums) == target: return [nums]
            else: return []
        
        for j in range(length-3):
            if j>0 and nums[j]==nums[j-1]:
                continue
            for i in range(j+1, length-2):
                if i>j+1 and nums[i]==nums[i-1]:
                    continue
                l, r = i+1, length-1
                while l<r:
                    total = nums[j]+nums[i]+nums[l]+nums[r]
                    if total < target:
                        l = l+1
                    elif total > target:
                        r = r-1
                    else:
                        result.append([nums[j], nums[i], nums[l], nums[r]])
                        while l < r and nums[l]==nums[l+1]:
                            l += 1
                        while l < r and nums[r]==nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return result