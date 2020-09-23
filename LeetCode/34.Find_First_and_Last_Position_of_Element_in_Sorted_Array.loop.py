class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res[0] = mid
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if res[0] == -1:
            return res        

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res[1] = mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return res