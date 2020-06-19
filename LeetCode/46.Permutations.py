# https://leetcode.com/problems/permutations/
# Runtime: 48 ms, faster than 88.99% of Python3 online submissions for Permutations.
# Memory Usage: 13.3 MB, less than 41.61% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res_list = []
        input_len = len(nums)
        def dfs(cur_list, remain, res_list):
            if len(cur_list) == input_len:
                res_list.append(cur_list)
                return
            for idx in range(len(remain)):
                remain_copy = remain.copy()
                del remain_copy[idx]
                dfs(cur_list+[remain[idx]], remain_copy, res_list)
        dfs([], nums, res_list)
        return res_list