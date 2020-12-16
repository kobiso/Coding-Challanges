# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        
        start, end = 0, 1
        while reader.get(end) < target:
            start = end
            end <<= 1

        end += 1
        while start < end:
            mid = (start + end) // 2
            val = reader.get(mid)
            if target < val:
                end = mid
            elif target > val:
                start = mid + 1
            else:
                return mid
        return -1
