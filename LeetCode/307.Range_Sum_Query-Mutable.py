class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val
        

    def sumRange(self, i: int, j: int) -> int:
        res = 0
        for idx in range(i, j+1):
            res += self.nums[idx]
            
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
