# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0
        left_max = [0]
        right_max = [0]
        for i in range(1, len(height)):
            left_max.append(max(left_max[i-1], height[i-1]))
        for i in range(len(height)-1, 0, -1):
            right_max.insert(0, max(right_max[0], height[i]))
        for i in range(len(height)):
            cur_sum = min(left_max[i], right_max[i]) - height[i]
            if cur_sum > 0:
                total += cur_sum

        return total
