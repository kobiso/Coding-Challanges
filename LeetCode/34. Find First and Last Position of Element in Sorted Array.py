# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
# Runtime: 36 ms, faster than 87.63% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 14 MB, less than 20.44% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

class Solution(object):
    min_first = -1
    max_last = -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pivot = self.binary_search(nums, target, 0, len(nums)-1)
        if pivot == -1:
            result = (-1,-1)
        else:
            self.min_first = pivot
            self.max_last = pivot
            self.binary_up(nums, target, pivot+1, len(nums)-1)
            self.binary_down(nums, target, 0, pivot-1)
            result = (self.min_first,self.max_last)

        return result
    
    def binary_search(self, nums, target, first, last):
        if last >= first:
            mid = (first+last)//2
            
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return self.binary_search(nums, target, first, mid-1)
            else:
                return self.binary_search(nums, target, mid+1, last)
        else:
            return -1

    def binary_up(self, nums, target, first, last):
        if last >= first:
            mid = (first+last)//2
            if nums[mid] == target: # do up
                self.max_last = max(self.max_last, mid)
                return self.binary_up(nums, target, mid+1, last)
            else: # do down
                return self.binary_up(nums, target, first, mid-1)

    def binary_down(self, nums, target, first, last):
        if last >= first:
            mid = (first+last)//2
            if nums[mid] == target: # do down
                self.min_first = min(self.min_first, mid)
                return self.binary_down(nums, target, first, mid-1)
            else:
                return self.binary_down(nums, target, mid+1, last)