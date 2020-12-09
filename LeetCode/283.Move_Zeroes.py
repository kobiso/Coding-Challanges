class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=0
        for i in range(len(nums)):
            if nums[idx] == 0:
                del nums[idx]
                nums.append(0)
            else:
                idx += 1
        return nums
