# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Runtime: 32 ms, faster than 63.60% of Python online submissions for Search in Rotated Sorted Array.
# Memory Usage: 12.1 MB, less than 15.68% of Python online submissions for Search in Rotated Sorted Array.

class Solution(object):
    
    def binary_search(self, nums, target):
        
        start, end = 0, len(nums)-1
        if nums[start]==target: return start
        elif nums[end]==target: return end
        
        while True:
            mid=(start+end)/2
            if mid == start or mid == end:
                if nums[mid]==target:
                    return mid
                break
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid                    
        
        return -1
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if nums[0] < nums[-1]: # binary search
            result = self.binary_search(nums, target)
        else:
            start, end = 0, len(nums)-1
            if target == nums[0]:
                return 0
            while True:
                mid = (start+end)/2
                if (nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                    pivot = mid+1
                    break
                elif (nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]):
                    pivot = mid
                    break
                
                if nums[0] < nums[mid]: # pivot is in right
                    start = mid
                else:
                    end = mid
            if target > nums[0]:
                result = self.binary_search(nums[:pivot], target)
                return result
            else:
                result = self.binary_search(nums[pivot:], target)
                if result!=-1:
                    return result + pivot
        return result
        