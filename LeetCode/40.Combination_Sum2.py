# https://leetcode.com/problems/combination-sum-ii/
# Runtime: 120 ms, faster than 28.48% of Python3 online submissions for Combination Sum II.
# Memory Usage: 13.2 MB, less than 70.92% of Python3 online submissions for Combination Sum II.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print (candidates)
        
        result = []
        def dfs(candidates, target, index, cur_list, result):
            if target < 0:
                return
            elif target == 0:
                if cur_list in result:
                    return
                else:
                    result.append(cur_list)
                    return
            for i in range(index, len(candidates)):
                if candidates[index] > target: return
                dfs(candidates, target-candidates[i], i+1, cur_list+[candidates[i]], result)
        dfs(candidates, target, 0, [], result)
        return result