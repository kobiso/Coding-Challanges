# https://leetcode.com/problems/combination-sum
# Runtime: 56 ms, faster than 97.58% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.4 MB, less than 19.15% of Python3 online submissions for Combination Sum.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        print (res+[1])
        candidates.sort()
        def dfs(candidates, target, index, path, res):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
                return
            else:
                for idx in range(index, len(candidates)):
                    if candidates[idx] > target: break
                    dfs(candidates, target-candidates[idx], idx, path+[candidates[idx]], res)
        dfs(candidates, target, 0, [], res)
        return res