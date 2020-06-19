# https://leetcode.com/problems/3sum
# Runtime: 748 ms, faster than 87.09% of Python3 online submissions for 3Sum.
# Memory Usage: 16.9 MB, less than 39.04% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            if nums[i]>0: break
            if i>0 and nums[i]==nums[i-1]: continue

            l, r = i+1, length-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res