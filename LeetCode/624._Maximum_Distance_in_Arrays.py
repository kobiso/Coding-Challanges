class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins = [sub[0] for sub in arrays]
        maxs = [sub[-1] for sub in arrays]
        
        max_res = -10000
        for i, min_val in enumerate(mins):
            max_res = max(max_res, abs(max(maxs[:i]+maxs[i+1:]) - min_val))

        return max_res